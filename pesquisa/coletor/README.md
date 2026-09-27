# COLETOR AUTOMATIZADO — CTESÍBIO

Coletor reproduzível para ampliar a pesquisa documental sobre o relógio de água de Ctesíbio.

A V1 consulta APIs públicas, normaliza metadados, deduplica resultados e produz JSONL/CSV e log de execução. Não tenta raspar indiscriminadamente a Internet nem contornar autenticação, CAPTCHA, paywalls, robots.txt ou limites de serviço.

## Execução

Python 3.11+:

    python pesquisa/coletor/ctesibio_collector.py

Opções:

    python pesquisa/coletor/ctesibio_collector.py --queries pesquisa/consultas/CONSULTAS_CTÉSIBIO_V1.md
    python pesquisa/coletor/ctesibio_collector.py --output pesquisa/dados/rodada-001
    python pesquisa/coletor/ctesibio_collector.py --max-results 50

## Provedores V1

- OpenAlex
- Crossref
- Internet Archive Advanced Search

## Saídas

pesquisa/dados/rodada-XXX/
- results.jsonl
- results.csv
- errors.jsonl
- execution.json
- README.md

Os resultados são candidatos. A etapa seguinte é a validação de evidências em pesquisa/validacao/.
