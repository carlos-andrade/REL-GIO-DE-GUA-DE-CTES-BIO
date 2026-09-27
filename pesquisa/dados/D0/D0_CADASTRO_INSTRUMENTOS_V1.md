# D0 — Cadastro de Instrumentos V1

**Projeto:** Relógio de Água de Ctesíbio  
**Repositório:** carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO  
**Fase:** D0 — Geometria e volume de referência  
**Estado:** PREPARADO — aguardando identificação dos instrumentos físicos

## Objetivo

Estabelecer a rastreabilidade dos instrumentos usados na coleta D0 antes que qualquer valor físico seja considerado válido.

## Regra de rastreabilidade

Nenhuma medição D0 deverá ser homologada sem que o instrumento utilizado esteja identificado no registro correspondente.

O campo `instrumento_id` do arquivo bruto deverá apontar para um registro desta ficha.

## Cadastro mínimo

| Instrumento ID | Grandeza | Fabricante | Modelo | Nº série | Resolução | Faixa | Exatidão/especificação | Calibração/verificação | Validade | Estado |
|---|---|---|---|---|---|---|---|---|---|---|
| INST-D0-001 | NÃO CADASTRADO | NÃO CADASTRADO | NÃO CADASTRADO | NÃO CADASTRADO | NÃO CADASTRADO | NÃO CADASTRADO | NÃO CADASTRADO | NÃO CADASTRADO | NÃO CADASTRADO | PENDENTE |

## Instrumentos esperados

- medição de comprimento/diâmetro;
- medição de volume;
- temperatura;
- referência temporal independente, quando aplicável;
- balança, caso massa seja usada para determinar volume;
- outros instrumentos efetivamente utilizados.

## Evidências a preservar

Para cada instrumento, registrar quando disponíveis:

1. fotografia ou identificação visual;
2. fabricante e modelo;
3. número de série;
4. resolução;
5. faixa de medição;
6. certificado de calibração ou verificação;
7. data da calibração/verificação;
8. condição de uso;
9. operador;
10. observações sobre o método.

## Critério de aceitação

O instrumento somente poderá ser marcado como **APTO PARA D0** quando sua identificação e características metrológicas relevantes estiverem registradas.

## Estados

- PENDENTE
- IDENTIFICADO
- APTO PARA D0
- NÃO APTO
- ENCERRADO

**Observação:** esta ficha não contém resultados experimentais.
