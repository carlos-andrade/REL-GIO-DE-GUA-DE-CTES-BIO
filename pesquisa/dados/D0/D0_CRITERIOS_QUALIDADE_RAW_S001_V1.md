# D0 — CRITÉRIOS DE QUALIDADE RAW S001 V1

## Cada observação RAW deve permitir identificar
1. o que foi medido;
2. unidade;
3. método;
4. instrumento;
5. repetição;
6. data/hora;
7. condição relevante;
8. observação/anomalia, quando existente.

## Erros críticos
- ID duplicado;
- valor sem unidade;
- grandeza sem definição;
- instrumento inexistente;
- valor impossível de interpretar;
- perda de rastreabilidade;
- alteração silenciosa do RAW.

## Tratamento
Erro crítico → BLOQUEIO.

Alerta não crítico → registrar e avaliar.

## Regra
O arquivo RAW é evidência primária e não deve ser sobrescrito para esconder erro.
