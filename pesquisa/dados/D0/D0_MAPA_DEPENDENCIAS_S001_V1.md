# MAPA DE DEPENDÊNCIAS E BLOQUEIOS — D0-S001

## Objetivo

Mostrar quais etapas dependem de evidência anterior e impedir avanço lógico
sem dados suficientes.

## Cadeia

`S001 → P01/P02 → RAW → VALIDAÇÃO → PROCESSAMENTO → INCERTEZA → REVISÃO → DECISÃO`

## Dependências

| Etapa | Depende de | Bloqueio |
|---|---|---|
| Sessão | identificação/configuração | sem sessão não há coleta |
| P01 | instrumentos/protótipo | sem instrumentação não medir |
| P02 | método H↔V | sem pontos definidos não processar |
| RAW | P01/P02 | sem medição não há dados |
| Validação | RAW | sem RAW não validar |
| Processamento | RAW válido | sem dados válidos não calcular |
| Incerteza | medições/processamento | sem dados não estimar |
| Revisão | pacote completo | sem evidência não decidir |
| Fechamento D0 | revisão aceita | critérios não atendidos bloqueiam |

## Bloqueios absolutos

1. Dados ausentes não podem ser substituídos por estimativas.
2. Dados não rastreáveis não podem ser usados como evidência.
3. Resultado processado não substitui RAW.
4. Validação automática não equivale a validação metrológica.
5. Um alerta não pode ser apagado para obter aprovação.
6. O fechamento D0 não ocorre enquanto os critérios de aceitação não forem
   demonstrados.

## Estado

**MAPA DEFINIDO — TODOS OS BLOQUEIOS ATIVOS ATÉ A COLETA S001.**
