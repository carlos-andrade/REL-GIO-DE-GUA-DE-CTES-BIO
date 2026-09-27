#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit
from urllib.request import Request, urlopen

USER_AGENT = "CtesibioResearchCollector/1.0 (+research project)"
DEFAULT_QUERIES = Path(__file__).resolve().parents[1] / "consultas" / "CONSULTAS_CTÉSIBIO_V1.md"
FIELDS = ["id","provider","query","title","url","authors","published","source_type","language","abstract","retrieved_at","evidence_class"]

def now():
    return datetime.now(timezone.utc).isoformat()

def request_json(url, timeout=30):
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))

def normalize_url(url):
    if not url:
        return ""
    p = urlsplit(url.strip())
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip("/"), "", ""))

def record_id(provider, url, title):
    raw = f"{provider}|{normalize_url(url)}|{title.strip().lower()}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

def parse_queries(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("##"):
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        if line and not line.startswith("Arquivo gerado"):
            out.append(line.strip('"'))
    return list(dict.fromkeys(out))

def classify(title, abstract, url):
    text = f"{title} {abstract} {url}".lower()
    if any(x in text for x in ("vitruvius","de architectura","heron","hero of alexandria")):
        return "A"
    if any(x in text for x in ("doi.org","journal","university","museum","jstor")):
        return "B"
    if any(x in text for x in ("archive.org","wikimedia","wikipedia","github")):
        return "C"
    return "E"

def openalex(query, limit):
    url = ("https://api.openalex.org/works?search=" + quote(query) +
           "&per-page=" + str(limit) +
           "&select=id,display_name,publication_year,doi,authorships,primary_location,abstract_inverted_index")
    data = request_json(url)
    out = []
    for item in data.get("results", []):
        loc = item.get("primary_location") or {}
        landing = loc.get("landing_page_url") or item.get("doi") or item.get("id") or ""
        authors = "; ".join(a.get("author",{}).get("display_name","") for a in item.get("authorships",[]) if a.get("author"))
        inv = item.get("abstract_inverted_index") or {}
        words = [(pos, word) for word, positions in inv.items() for pos in positions]
        abstract = " ".join(w for _, w in sorted(words))
        out.append({"provider":"openalex","query":query,"title":item.get("display_name") or "",
                    "url":landing,"authors":authors,"published":item.get("publication_year") or "",
                    "source_type":"academic_work","language":"","abstract":abstract})
    return out

def crossref(query, limit):
    url = ("https://api.crossref.org/works?query.bibliographic=" + quote(query) +
           "&rows=" + str(limit) + "&select=DOI,title,author,published,URL,type")
    data = request_json(url)
    out = []
    for item in data.get("message",{}).get("items",[]):
        title = (item.get("title") or [""])[0]
        authors = "; ".join((a.get("given","") + " " + a.get("family","")).strip() for a in item.get("author",[]))
        parts = item.get("published",{}).get("date-parts",[[]])
        year = parts[0][0] if parts and parts[0] else ""
        url_value = item.get("URL") or (("https://doi.org/" + item["DOI"]) if item.get("DOI") else "")
        out.append({"provider":"crossref","query":query,"title":title,"url":url_value,"authors":authors,
                    "published":year,"source_type":item.get("type","bibliographic"),"language":"",
                    "abstract":item.get("abstract","")})
    return out

def internet_archive(query, limit):
    url = ("https://archive.org/advancedsearch.php?q=" + quote(query) +
           "&fl[]=identifier&fl[]=title&fl[]=creator&fl[]=date&fl[]=description&rows=" +
           str(limit) + "&page=1&output=json")
    data = request_json(url)
    out = []
    for doc in data.get("response",{}).get("docs",[]):
        ident = doc.get("identifier","")
        out.append({"provider":"internet_archive","query":query,"title":doc.get("title",""),
                    "url":("https://archive.org/details/" + ident) if ident else "",
                    "authors":doc.get("creator",""),"published":doc.get("date",""),
                    "source_type":"digital_archive","language":"","abstract":doc.get("description","")})
    return out

PROVIDERS = [("openalex",openalex),("crossref",crossref),("internet_archive",internet_archive)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-results", type=int, default=20)
    parser.add_argument("--delay", type=float, default=0.5)
    args = parser.parse_args()
    if not args.queries.exists():
        print("Arquivo de consultas não encontrado: " + str(args.queries), file=sys.stderr)
        return 2
    run_id = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    output = args.output or Path(__file__).resolve().parents[1] / "dados" / ("rodada-" + run_id)
    output.mkdir(parents=True, exist_ok=True)
    queries = parse_queries(args.queries)
    seen, results, errors = set(), [], []
    for query in queries:
        for provider, fn in PROVIDERS:
            started = time.monotonic()
            try:
                for item in fn(query, args.max_results):
                    item["url"] = normalize_url(item.get("url",""))
                    item["id"] = record_id(provider,item["url"],item.get("title",""))
                    item["retrieved_at"] = now()
                    item["evidence_class"] = classify(item.get("title",""),item.get("abstract",""),item["url"])
                    key = (item["url"],item["title"].strip().lower())
                    if key not in seen:
                        seen.add(key); results.append(item)
            except Exception as exc:
                errors.append({"provider":provider,"query":query,"error":repr(exc),"at":now()})
            finally:
                time.sleep(max(0,args.delay-(time.monotonic()-started)))
    with (output/"results.jsonl").open("w",encoding="utf-8") as f:
        for item in results: f.write(json.dumps(item,ensure_ascii=False)+"\n")
    with (output/"results.csv").open("w",encoding="utf-8",newline="") as f:
        w = csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(results)
    with (output/"errors.jsonl").open("w",encoding="utf-8") as f:
        for item in errors: f.write(json.dumps(item,ensure_ascii=False)+"\n")
    execution = {"run_id":run_id,"finished_at":now(),"queries":len(queries),
                 "providers":[p for p,_ in PROVIDERS],"unique_results":len(results),
                 "errors":len(errors),"max_results_per_provider_query":args.max_results}
    (output/"execution.json").write_text(json.dumps(execution,ensure_ascii=False,indent=2),encoding="utf-8")
    (output/"README.md").write_text("# Rodada " + run_id + "\n\nResultados únicos: " + str(len(results)) + "\n\nValidação pendente.\n",encoding="utf-8")
    print(json.dumps(execution,ensure_ascii=False,indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
