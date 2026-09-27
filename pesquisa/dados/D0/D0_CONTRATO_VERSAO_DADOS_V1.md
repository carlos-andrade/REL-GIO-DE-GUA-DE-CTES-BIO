# CONTRATO DE VERSIONAMENTO DOS DADOS — D0

## Objetivo

Impedir que dados experimentais, resultados processados e versões de
configuração sejam confundidos entre si.

## Classes

### RAW
Dados diretamente coletados no protótipo.

Exemplo:
`D0_GEOMETRIA_BRUTO.csv`

Regra: somente adicionar novos registros ou criar nova versão documentada.

### PROCESSED
Resultados calculados a partir dos dados RAW.

Exemplo:
`D0_GEOMETRIA_PROCESSADO.csv`

Regra: nunca é fonte primária.

### REPORT
Relatórios de validação, revisão e aceitação.

### CONFIG
Procedimentos, instrumentos, configuração do protótipo e parâmetros.

## Identificação recomendada

Sessão:
`D0-S###`

Conjunto bruto:
`D0-RAW-S###-V##`

Processamento:
`D0-PROC-S###-V##`

Relatório:
`D0-REPORT-S###-V##`

## Regra de dependência

`RAW → PROCESSADO → RELATÓRIO`

Nunca:

`RELATÓRIO → RAW`

Um relatório não pode gerar ou alterar dados brutos.

## Reprodutibilidade

Todo resultado processado deve permitir identificar:

- sessão;
- versão do conjunto bruto;
- hash, quando formalizado;
- versão do processador;
- parâmetros de processamento;
- data/hora;
- responsável.

## Regra de não substituição

Uma nova versão não invalida silenciosamente a anterior.

Quando houver correção:

`VERSÃO ANTERIOR → MOTIVO → CORREÇÃO → NOVA VERSÃO → NOVA VALIDAÇÃO`

## Estado

**CONTRATO DEFINIDO — AGUARDANDO PRIMEIRA SESSÃO FÍSICA D0.**
