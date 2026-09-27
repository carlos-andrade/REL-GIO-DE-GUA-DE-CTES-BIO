# MATRIZ DE REPETIBILIDADE — D0-S001

## Objetivo

Definir antecipadamente como será demonstrada a repetibilidade das medições
críticas da primeira sessão física.

## Regra geral

Cada repetição deve ser registrada como observação independente no conjunto
RAW, mantendo o mesmo identificador de sessão e um identificador próprio de
observação.

## Dimensões críticas

| Grupo | Grandeza | Repetições mínimas | Estado |
|---|---|---:|---|
| D0-G01 | altura | 3 | PENDENTE |
| D0-G02 | diâmetro/largura | 3 | PENDENTE |
| D0-G03 | área A(H) | derivada | PENDENTE |
| D0-G04 | volume útil | 3 quando medido diretamente | PENDENTE |
| D0-G05 | níveis H | 3 por ponto crítico, quando aplicável | PENDENTE |
| D0-G06 | ΔV/ΔH | derivada | PENDENTE |
| D0-G07 | volume de descarga | 3 | PENDENTE |
| D0-G08 | volume residual | 3 | PENDENTE |

## Registro

Para cada repetição devem existir:

- ID único;
- grandeza;
- unidade;
- método;
- instrumento_ID;
- resolução;
- temperatura, quando relevante;
- data/hora;
- valor bruto;
- observação;
- status.

## Tratamento

Quando houver pelo menos duas observações numéricas comparáveis, poderão ser
calculados:

- média;
- desvio-padrão amostral;
- incerteza Tipo A.

Nenhuma repetição será descartada apenas por aumentar a dispersão. Qualquer
exclusão deverá ser tecnicamente justificada e registrada.

## Critério preliminar

A repetibilidade será avaliada após a coleta, usando a dispersão observada e
a incerteza associada. Não será estabelecido um limite artificial antes de
conhecer a resolução dos instrumentos, o método e a finalidade da grandeza.

## Estado

**MATRIZ PREPARADA — NENHUMA REPETIÇÃO EXPERIMENTAL REALIZADA.**
