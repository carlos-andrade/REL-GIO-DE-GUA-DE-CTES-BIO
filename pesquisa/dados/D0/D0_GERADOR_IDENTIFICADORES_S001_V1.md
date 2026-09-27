# PADRÃO DE IDENTIFICADORES — D0-S001

## Objetivo

Padronizar identificadores antes da coleta para evitar ambiguidades entre
sessão, observação, instrumento, ponto H↔V e resultado processado.

## Identificadores

### Sessão

`D0-S001`

### Observação bruta

Formato:

`D0-S001-R###`

Exemplos:
- D0-S001-R001
- D0-S001-R002

Cada linha de observação física deve possuir um ID único.

### Instrumento

Formato:

`D0-S001-I##`

Exemplos:
- D0-S001-I01
- D0-S001-I02

O cadastro do instrumento permanece no documento próprio de instrumentos.

### Ponto H↔V

Formato:

`D0-S001-HV##`

Exemplos:
- D0-S001-HV01
- D0-S001-HV02

### Resultado processado

Formato:

`D0-S001-P###`

Cada resultado processado deve apontar para um ou mais IDs RAW.

## Regra de unicidade

Nenhum identificador pode ser reutilizado para representar outra observação.

## Regra de rastreabilidade

Todo resultado deverá permitir:

`resultado → grupo → RAW → instrumento → sessão`

## Estado

**PADRÃO DEFINIDO — AGUARDANDO EXECUÇÃO S001.**
