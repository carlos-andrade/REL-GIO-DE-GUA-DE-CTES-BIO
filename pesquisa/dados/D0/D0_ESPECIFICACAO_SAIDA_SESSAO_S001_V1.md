# ESPECIFICAÇÃO DE SAÍDA — D0-S001

## Objetivo

Definir antecipadamente os artefatos que deverão existir após a primeira
sessão física D0, evitando lacunas de documentação e impedindo que resultados
sejam declarados antes da execução.

## Pacote esperado

### 1. Registro da sessão
Arquivo:
`D0_REGISTRO_SESSAO_MEDICAO_V1.md`

Deve conter:
- identificador D0-S001;
- data e hora;
- operador;
- protótipo/configuração;
- ambiente;
- instrumentos;
- procedimentos executados;
- ocorrências.

### 2. Dados brutos
Arquivo-base:
`D0_GEOMETRIA_BRUTO.csv`

Deve conter somente observações efetivamente coletadas.

### 3. Validação automática
Arquivo:
`D0_RELATORIO_VALIDACAO_AUTOMATICA_V1.md`

Deve registrar a execução real de:
`D0_VALIDACAO_AUTOMATIZADA_V1.py`

### 4. Processamento
Arquivo-base:
`D0_GEOMETRIA_PROCESSADO.csv`

Deve conter resultados derivados dos dados brutos, nunca valores inventados.

### 5. Integridade
Registro SHA-256 do conjunto bruto e dos artefatos formalmente controlados.

### 6. Rastreabilidade
Cada resultado deve permitir reconstruir:

`resultado → bruto → instrumento → método → sessão → configuração`

### 7. Revisão
Formulário:
`D0_FORMULARIO_ACEITACAO_REVISAO_V1.md`

Nenhum fechamento D0 será declarado sem revisão.

## Critérios mínimos para processamento

O processamento de D0-S001 somente poderá ocorrer quando:

- houver dados reais;
- IDs forem únicos;
- instrumentos estiverem identificados;
- unidades estiverem definidas;
- data/hora estiverem registradas;
- repetições críticas estiverem disponíveis ou justificadas;
- anomalias estiverem documentadas.

## Critérios mínimos para encerramento D0

Além dos critérios acima:

- H↔V deverá estar estabelecida experimentalmente;
- incertezas deverão estar documentadas;
- inconsistências deverão estar resolvidas ou formalmente registradas;
- processamento deverá ser reproduzível;
- revisão deverá estar concluída.

## Estado

**D0-S001 — PACOTE DE SAÍDA PREPARADO.**

A existência desta especificação não significa que D0-S001 tenha sido
executada.
