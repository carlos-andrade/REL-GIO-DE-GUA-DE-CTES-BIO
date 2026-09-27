# D0 — PROCESSADOR DE DADOS V1

## Finalidade
Fornecer um processador reproduzível para transformar dados brutos reais em resultados estatísticos separados.

## Regra de segurança
O processador não cria dados físicos. Com o CSV atual, que contém apenas registro de preparação, nenhuma medição válida será produzida.

## Entrada
D0_GEOMETRIA_BRUTO.csv

## Saída
D0_GEOMETRIA_PROCESSADO.csv

## Controles
- preservação do arquivo bruto;
- exclusão de placeholders das estatísticas;
- cálculo da média somente para valores numéricos;
- desvio-padrão amostral;
- incerteza Tipo A quando houver pelo menos duas repetições;
- incerteza Tipo B permanece pendente até haver evidência metrológica;
- resultados devem ser revisados antes de qualquer aceitação.

## Estado
**PREPARADO — NÃO EXECUTADO SOBRE DADOS EXPERIMENTAIS.**
