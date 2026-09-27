# FASE D0 — GEOMETRIA E VOLUME DE REFERÊNCIA

**Projeto:** Relógio de Água de Ctesíbio
**Repositório:** carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO
**Fase:** D0 — Geometria e volume de referência
**Estado:** INICIADA — aguardando medições físicas
**Data de abertura:** 27/09/2026

## 1. Objetivo
Estabelecer a geometria mensurável do protótipo e a relação entre nível, volume e área hidráulica. D0 é a referência quantitativa para as fases posteriores de vazão, estabilidade de nível, flutuador, calibração e ciclo automático.

## 2. Regra de evidência
Nenhuma dimensão, volume, tolerância ou precisão física será considerada medida até existir registro experimental. Valores provenientes de desenho, CAD, fabricante ou estimativa devem ser identificados separadamente como PROJETO, REFERÊNCIA ou ESTIMATIVA.

## 3. Grandezas mínimas
| Código | Grandeza | Unidade | Método mínimo |
|---|---|---:|---|
| D0-G01 | altura interna útil | mm | paquímetro/régua calibrada |
| D0-G02 | diâmetro/largura interna | mm | paquímetro/micrómetro |
| D0-G03 | área transversal A(H) | mm² | cálculo a partir da geometria |
| D0-G04 | volume útil V | mL/L | medição gravimétrica ou volumétrica |
| D0-G05 | níveis de referência H | mm | escala de referência |
| D0-G06 | volume por incremento de nível ΔV/ΔH | mL/mm | série de enchimento controlado |
| D0-G07 | volume de descarga | mL | coleta e medição |
| D0-G08 | volume residual após descarga | mL | coleta/medição |

## 4. Reservatórios a caracterizar
- reservatório de alimentação;
- reservatório/regulador de nível constante;
- reservatório de referência do flutuador;
- linha e volume hidráulico entre reservatórios;
- câmara ou recipiente de descarga/sifão;
- recipiente de contenção, quando fizer parte do circuito experimental.

## 5. Procedimento D0-P01 — levantamento geométrico
1. Identificar cada componente com código único.
2. Registrar material, fabricante/modelo quando existente e desenho/referência.
3. Medir dimensões internas relevantes em pelo menos três posições quando a geometria puder variar.
4. Registrar resolução e identificação do instrumento.
5. Repetir cada dimensão crítica no mínimo três vezes.
6. Registrar temperatura ambiente e condição do componente.
7. Calcular média, dispersão e intervalo observado.
8. Fotografar ou esquematizar os pontos de medição.
9. Separar dimensão nominal de dimensão efetivamente medida.

## 6. Procedimento D0-P02 — relação nível-volume
Para geometrias prismáticas simples: V(H) = integral de A(H)dH.
Para seção transversal constante: V = A·H.
Para geometria variável, determinar experimentalmente a curva V(H) por incrementos conhecidos de volume e leitura do nível.
A curva deverá ser registrada em pontos suficientes para representar mudanças de seção, entradas, saídas, zonas mortas e regiões próximas ao nível operacional.

## 7. Controle metrológico
Cada medição deve conter: instrumento; resolução; unidade; operador; data/hora; temperatura, quando relevante; número da repetição; valor bruto; valor processado; observação/anomalia.
Não aplicar arredondamento antes do processamento final.

## 8. Critérios de aceitação D0
D0 somente será considerado CONCLUÍDO quando:
- todos os reservatórios críticos tiverem identificação e geometria registrada;
- dimensões críticas tiverem repetição suficiente;
- volume útil e volume residual forem medidos ou formalmente classificados como ainda não medidos;
- existir curva ou tabela H ↔ V ↔ A para o reservatório de medição;
- as incertezas ou limitações de cada medição estiverem registradas;
- os dados brutos forem preservados;
- uma revisão independente dos cálculos confirmar a consistência dimensional.

## 9. Saídas esperadas
- D0_GEOMETRIA_BRUTO.csv
- D0_GEOMETRIA_PROCESSADO.csv
- D0_RELATORIO_MEDICOES_V1.md
- desenhos/esquemas identificados, quando necessários;
- tabela de referência H ↔ V ↔ A.

## 10. Relação com Ctesíbio
Princípio histórico: controle da condição hidráulica e utilização do nível do fluido como variável física para produzir uma indicação temporal estável.
Solução moderna D0: quantificar a geometria real e sua relação nível-volume antes de atribuir desempenho ao sistema. A modernização não substitui o princípio hidráulico; torna-o mensurável, calibrável e auditável.

## 11. Estado atual
D0 = INICIADA.
Ainda não existem medições físicas D0 registradas neste documento. Portanto, não há precisão, tolerância experimental ou curva V(H) validada a declarar.