# VALIDAÇÃO DA PESQUISA — CTESÍBIO

## Etapa 3

Esta pasta contém a validação estrutural das rodadas produzidas pelo coletor.

### Execução

`python pesquisa/validacao/validate_ctesibio.py`

Ou, para uma rodada específica:

`python pesquisa/validacao/validate_ctesibio.py --round pesquisa/dados/rodada-001`

O relatório é gravado em `pesquisa/relatorios/RELATORIO_VALIDACAO_V1.md`.

## Regra de evidência

Uma fonte retornada pelo coletor é uma **candidata**. Validação estrutural não equivale a validação histórica.

A revisão deve separar: fato documentado; interpretação acadêmica; reconstrução moderna; hipótese de engenharia; afirmação sem evidência suficiente; contradição entre fontes.

## Rastreabilidade obrigatória

Toda afirmação relevante deve permitir o percurso: consulta → provedor → fonte candidata → validação documental → afirmação → evidência → síntese.

## Automação

O workflow `.github/workflows/pesquisa-ctesibio.yml` permite execução manual e semanal do coletor, seguida de validação estrutural e registro dos resultados no repositório.

## Próxima etapa

Após a validação documental, executar a **Etapa 4 — Síntese Técnica e Reconstrução**, usando `pesquisa/sintese/README.md` como contrato.
