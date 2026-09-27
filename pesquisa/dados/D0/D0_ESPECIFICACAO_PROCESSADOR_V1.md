# D0 — Especificação do Processador de Dados V1

**Projeto:** Relógio de Água de Ctesíbio  
**Repositório:** carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO  
**Fase:** D0 — Geometria e volume de referência  
**Estado:** PREPARADO — aguardando dados físicos

## Objetivo

Definir o comportamento de um processamento reprodutível para transformar o CSV bruto D0 em resultados estatísticos e geométricos, sem preencher dados ausentes.

## Entrada

Arquivo:

`pesquisa/dados/D0/D0_GEOMETRIA_BRUTO.csv`

Campos mínimos:

`id, componente, grandeza, unidade, método, instrumento, instrumento_id, resolução, temperatura_c, repeticao, valor_bruto, incerteza, observacao, data_hora, status`

## Regras obrigatórias

1. Ler somente registros válidos para processamento.
2. Não converter `NÃO MEDIDO` em zero.
3. Não converter `NÃO CALCULADO` em estimativa.
4. Não eliminar repetição sem justificativa registrada.
5. Preservar IDs de origem.
6. Produzir resultados em arquivo separado.
7. Informar número de repetições usado.
8. Calcular média e desvio-padrão somente quando houver dados numéricos suficientes.
9. Registrar falhas e pendências.
10. Nunca declarar D0 fechada automaticamente.

## Cálculos

Para cada grupo homogêneo de grandeza/componente/unidade:

`media = soma(x_i) / n`

`s = sqrt(soma((x_i-media)^2)/(n-1))`

`uA = s/sqrt(n)`

Quando aplicável:

`A = pi*D^2/4`

A área calculada deverá ser marcada como **DERIVADA**.

## H↔V

Para pares de nível e volume:

`H_i → V_i`

O processador deverá:

- ordenar os pontos por H;
- verificar monotonicidade;
- identificar duplicações;
- preservar pontos anômalos;
- não removê-los automaticamente;
- registrar eventual modelo ajustado separadamente dos dados observados.

## Saída esperada

Arquivo:

`pesquisa/dados/D0/D0_GEOMETRIA_PROCESSADO.csv`

Com, no mínimo:

`id, componente, grandeza, unidade, n_repeticoes, media, desvio_padrao, incerteza_tipo_A, incerteza_tipo_B, incerteza_combinada, status, observacao`

## Relatório de execução

Cada processamento deverá registrar:

- data/hora;
- versão do processador;
- arquivo de entrada;
- arquivo de saída;
- número de registros lidos;
- número processado;
- número rejeitado;
- pendências;
- erros;
- observações.

## Critério de reprodutibilidade

Dado o mesmo arquivo bruto, a mesma versão do processador e os mesmos parâmetros, o resultado deverá ser reproduzível.

**Estado atual:** especificação preparada; nenhum processamento experimental executado.
