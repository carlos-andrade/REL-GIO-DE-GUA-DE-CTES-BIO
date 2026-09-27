#!/usr/bin/env python3
"""Validador estrutural da coleta Ctesíbio.

Valida metadados, integridade e duplicidade. Não transforma fonte candidata em fato histórico validado.
"""
import argparse, json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

REQUIRED={"id","provider","query","title","url","retrieved_at","evidence_class"}

def latest_round(base):
    rounds=sorted(p for p in Path(base).glob("rodada-*") if p.is_dir())
    if not rounds: raise FileNotFoundError(f"Nenhuma rodada encontrada em {base}")
    return rounds[-1]

def load_jsonl(path):
    rows=[]
    with Path(path).open(encoding="utf-8") as f:
        for n,line in enumerate(f,1):
            if not line.strip(): continue
            try: rows.append((n,json.loads(line)))
            except json.JSONDecodeError as e: rows.append((n,{"__parse_error__":str(e)}))
    return rows

def validate(rows):
    issues=[]; valid=[]; seen=set()
    for line,row in rows:
        if "__parse_error__" in row:
            issues.append((line,"JSON inválido",row["__parse_error__"])); continue
        missing=sorted(REQUIRED-set(row))
        if missing: issues.append((line,"Campos ausentes",", ".join(missing)))
        url=row.get("url",""); parsed=urlparse(url)
        if parsed.scheme not in {"http","https"} or not parsed.netloc: issues.append((line,"URL inválida",url))
        key=(url.lower().rstrip("/"),str(row.get("title","")).strip().lower())
        if key in seen: issues.append((line,"Duplicata na rodada",url))
        else: seen.add(key); valid.append(row)
        if row.get("evidence_class") not in {"A","B","C","D","E"}: issues.append((line,"Classe de evidência inválida",str(row.get("evidence_class"))))
    return valid,issues

def report(round_dir, rows, valid, issues):
    counts={}; providers={}
    for r in valid:
        c=r.get("evidence_class","?"); p=r.get("provider","?")
        counts[c]=counts.get(c,0)+1; providers[p]=providers.get(p,0)+1
    out=Path(round_dir).parent.parent/"relatorios"/"RELATORIO_VALIDACAO_V1.md"
    out.parent.mkdir(parents=True,exist_ok=True)
    lines=["# Relatório de Validação V1 — Ctesíbio","",f"- Rodada: {Path(round_dir).name}",f"- Data UTC: {datetime.now(timezone.utc).isoformat()}",f"- Registros lidos: **{len(rows)}**",f"- Registros aproveitáveis estruturalmente: **{len(valid)}**",f"- Ocorrências: **{len(issues)}**","","## Limite metodológico","","Esta etapa valida integridade estrutural, metadados, URLs e duplicidade. Ela não comprova que uma afirmação histórica sobre Ctesíbio seja verdadeira. A confirmação histórica exige leitura da fonte, rastreamento bibliográfico e revisão crítica.","","## Classes preliminares",""]
    lines += [f"- {k}: {counts[k]}" for k in sorted(counts)] or ["- Nenhuma"]
    lines += ["","## Provedores",""] + [f"- {k}: {providers[k]}" for k in sorted(providers)]
    lines += ["","## Ocorrências",""]
    lines += [f"- Linha {n} — **{kind}** — {detail}" for n,kind,detail in issues[:500]] or ["Nenhuma ocorrência estrutural encontrada."]
    lines += ["","## Próxima ação obrigatória","","1. Ler as fontes candidatas.","2. Confirmar autoria, data, natureza e contexto documental.","3. Extrair cada afirmação histórica relevante.","4. Associar cada afirmação à evidência correspondente.","5. Registrar contradições e hipóteses separadamente.","6. Alimentar a síntese técnica somente após a revisão documental.","","Fluxo: consulta → provedor → fonte candidata → validação documental → afirmação → evidência → síntese."]
    out.write_text("\n".join(lines)+"\n",encoding="utf-8"); return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--round"); ap.add_argument("--base",default="pesquisa/dados"); args=ap.parse_args()
    rd=Path(args.round) if args.round else latest_round(args.base)
    rows=load_jsonl(rd/"results.jsonl"); valid,issues=validate(rows); out=report(rd,rows,valid,issues)
    print(json.dumps({"round":str(rd),"records":len(rows),"valid":len(valid),"issues":len(issues),"report":str(out)},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
