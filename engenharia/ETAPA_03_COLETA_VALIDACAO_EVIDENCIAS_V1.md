# ETAPA 03 — COLETA, VALIDAÇÃO E CONTROLE DAS EVIDÊNCIAS

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Versão:** V1  
**Data:** 27/09/2026

## 1. Objetivo

Transformar a pesquisa histórica em um processo reproduzível de coleta, normalização, deduplicação e validação documental.

## 2. Infraestrutura existente

A etapa utiliza:

- `pesquisa/coletor/README.md`;
- `pesquisa/coletor/ctesibio_collector.py`;
- `pesquisa/coletor/requirements.txt`;
- `.github/workflows/pesquisa-ctesibio.yml`;
- `pesquisa/validacao/validate_ctesibio.py`;
- `pesquisa/validacao/README.md`.

## 3. Fluxo

```text
CONSULTA → PROVEDOR → FONTE CANDIDATA → NORMALIZAÇÃO → DEDUPLICAÇÃO → CLASSIFICAÇÃO → VALIDAÇÃO → EVIDÊNCIA
```

## 4. Provedores previstos

- OpenAlex;
- Crossref;
- Internet Archive Advanced Search.

A coleta automatizada é mecanismo de descoberta e não substitui a validação documental da fonte.

## 5. Registro mínimo

Cada resultado deverá conservar, quando disponível:

- identificador;
- consulta;
- provedor;
- título;
- autor;
- instituição;
- data;
- idioma;
- tipo documental;
- URL/identificador;
- classe de evidência;
- afirmação relevante;
- confiança;
- duplicidade;
- observações.

## 6. Resultado esperado

Gerar rodadas identificáveis de coleta, erros, metadados e relatórios de validação, preservando a cadeia de auditoria.

## 7. Critério de conclusão

A etapa será concluída quando uma rodada puder ser reproduzida e seus resultados classificados sem apresentar a coleta automática como prova histórica definitiva.

## 8. Relação com a Etapa 04

Os resultados validados alimentam a síntese técnica e a separação entre história, reconstrução e engenharia moderna.
