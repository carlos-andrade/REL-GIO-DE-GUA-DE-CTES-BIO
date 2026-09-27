# D0 — Plano de Processamento e Auditoria V1

**Projeto:** Relógio de Água de Ctesíbio  
**Repositório:** carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO  
**Fase:** D0 — Geometria e volume de referência  
**Estado:** PREPARADO — aguardando dados físicos

## Objetivo

Definir, antes da coleta, como os dados brutos serão transformados em resultados dimensionais auditáveis.

## 1. Regras

1. Dados brutos nunca são sobrescritos.
2. Valores calculados ficam em arquivo separado.
3. Cada resultado deve apontar para seus IDs brutos.
4. Nenhuma média substitui as repetições originais.
5. Ausência de dado deve ser registrada como **NÃO MEDIDO**.
6. Resultado não calculado deve permanecer **NÃO CALCULADO**.
7. Nenhuma tolerância será considerada atendida sem medição correspondente.

## 2. Estatística mínima

Para cada grandeza com n repetições:

- média: x_media = soma(x_i) / n
- desvio-padrão amostral: s = sqrt[soma((x_i-x_media)^2)/(n-1)]
- erro padrão: uA = s/sqrt(n)

A incerteza Tipo B deverá considerar, quando aplicável:
- resolução do instrumento;
- especificação do fabricante;
- calibração/verificação;
- método de leitura;
- efeitos ambientais identificados.

A combinação das componentes deverá ser feita somente quando suas contribuições estiverem documentadas.

## 3. Relação H <-> V

Para cada ponto medido:

H_i -> V_i

Registrar:
- ID do ponto;
- altura;
- volume;
- método;
- repetição;
- instrumento;
- condição ambiental.

Para reservatório de seção constante, poderá ser verificada a aproximação:

V(H) = A*H + V0

Essa relação não será presumida. Ela deverá ser confrontada com os dados.

## 4. Área da seção

Quando a geometria permitir, calcular A a partir das dimensões medidas.

Exemplo para seção circular ideal:

A = pi*D^2/4

O valor calculado deverá permanecer identificado como **DERIVADO**, separado da medição direta.

## 5. Verificações

### D0-A01 — rastreabilidade
Cada resultado possui origem identificável?

### D0-A02 — repetibilidade
As repetições apresentam dispersão compatível com o método?

### D0-A03 — consistência geométrica
As dimensões são compatíveis entre si?

### D0-A04 — monotonicidade H <-> V
O volume aumenta com o nível na faixa útil?

### D0-A05 — fechamento volumétrico
Volume útil ≈ volume medido até o nível superior, dentro da incerteza estabelecida?

### D0-A06 — integridade
Nenhum valor foi alterado ou inventado durante o processamento?

## 6. Critério de liberação D0

D0 somente poderá ser encerrada quando:
- dados brutos completos para as grandezas críticas;
- rastreabilidade dos instrumentos;
- repetições suficientes;
- processamento reproduzível;
- incertezas documentadas quando aplicáveis;
- relação H <-> V estabelecida;
- anomalias resolvidas ou formalmente registradas;
- revisão final concluída.

## 7. Estado

**ATUAL:** preparação concluída.  
**PENDÊNCIA:** coleta física.  
**PRÓXIMA TRANSIÇÃO:** D0-COLETA -> D0-PROCESSAMENTO -> D0-VALIDAÇÃO -> D0-FECHADA.

Este documento não constitui resultado experimental.
