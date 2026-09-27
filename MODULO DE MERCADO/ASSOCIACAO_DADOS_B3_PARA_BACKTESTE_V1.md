# ASSOCIAÇÃO DE DADOS DE MERCADO B3 AO MÓDULO DE MERCADO

## Arquivo
ASSOCIACAO_DADOS_B3_PARA_BACKTESTE_V1.md

## Projeto
RELÓGIO DE ÁGUA DE CTESÍBIO

## Aplicação
Módulos de análise de mercado para BRICKMASTER

## Fonte de dados
carlos-andrade/B3

## Repositório consumidor
carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO

## Pasta
MODULO DE MERCADO/

## Data
27/09/2026

---

## 1. CONCLUSÃO

SIM. É tecnicamente possível associar o repositório `carlos-andrade/B3` como **fonte externa oficial de dados de mercado para pesquisa, testes e futuros backtests** dos módulos derivados dos princípios de Ctesíbio.

A estratégia recomendada é **não duplicar automaticamente o acervo do B3 neste repositório**.

O repositório B3 permanece como **fonte de dados** e este projeto mantém apenas:

- referência ao repositório;
- contrato de consumo;
- seleção de datasets;
- versões/commits utilizados;
- metadados;
- hashes quando disponíveis;
- critérios de frescor;
- regras de transformação;
- resultados de testes;
- evidências de reprodução.

Isso preserva a separação entre **dados-fonte** e **pesquisa/modelo**.

---

## 2. EVIDÊNCIA ATUAL DO REPOSITÓRIO B3

O repositório `carlos-andrade/B3` está ativo e possui infraestrutura de ingestão, normalização, auditoria e workflows relacionados a dados da B3.

Foi identificada, entre outras estruturas:

- `ativos/catalogo/`
- `ativos/catalogo/raw/`
- `ativos/catalogo/estatisticas/`
- `dados/cotahist/`
- `docs/ingestao/`
- `scripts/ingestao/`
- `.github/workflows/`

Há inclusive arquivo bruto COTAHIST de 2026 e datasets derivados.

---

## 3. DADO MAIS IMPORTANTE PARA O BACKTEST

O COTAHIST é uma fonte relevante para:

- preço;
- abertura;
- máxima;
- mínima;
- fechamento;
- quantidade;
- volume financeiro;
- outras variáveis compatíveis com o layout histórico.

O próprio projeto B3 estabelece que COTAHIST/EOD **não deve ser tratado como fluxo de ordens, agressão ou Cumulative Delta**.

Portanto:

### Pode ser usado para

- estudos de preço;
- volatilidade;
- volume;
- séries históricas;
- regimes;
- sazonalidade temporal;
- testes de referências adaptativas;
- testes de normalização;
- estudos de comportamento de ciclos.

### Não deve ser usado sozinho para

- reconstruir agressão compradora/vendedora;
- afirmar fluxo de ordens;
- reconstruir Cumulative Delta;
- inferir microestrutura que a fonte não registra.

---

## 4. DADOS DE MICROESTRUTURA

O repositório B3 também contém infraestrutura relacionada a dados de negócio a negócio e ingestões específicas.

Esses dados poderão ser candidatos para módulos que dependam de:

- negócios;
- sequência temporal;
- quantidade;
- preço;
- volume;
- microestrutura.

Entretanto, cada dataset deverá ser validado individualmente antes de ser utilizado.

Não assumir que a existência de um arquivo significa que ele possui todas as variáveis necessárias.

---

## 5. CONTRATO ENTRE OS DOIS REPOSITÓRIOS

Arquitetura:

`B3 → Fonte de dados`

`RELOGIO_DE_AGUA_DE_CTESIBIO → Pesquisa de modelos`

`BRICKMASTER → Implementação futura`

Fluxo:

`DADOS B3`
→ `VALIDAÇÃO`
→ `SELEÇÃO TEMPORAL`
→ `TRANSFORMAÇÃO CONTROLADA`
→ `MÓDULO CTESÍBIO`
→ `BACKTEST`
→ `RESULTADO`
→ `AUDITORIA`

---

## 6. IDENTIDADE DO DATASET

Todo backtest deverá registrar:

- repositório-fonte;
- caminho do dataset;
- commit do B3 utilizado;
- arquivo exato;
- período;
- primeira data;
- última data;
- número de registros;
- instrumento(s);
- versão do layout;
- transformação aplicada;
- hash quando disponível;
- data de captura;
- status de frescor.

Exemplo conceitual:

`SOURCE_REPO = carlos-andrade/B3`

`SOURCE_COMMIT = <SHA>`

`SOURCE_PATH = <arquivo>`

`DATASET_VERSION = <versão>`

`PERIOD = <início/fim>`

---

## 7. REGRA DE FRESCOR

Há uma limitação importante já registrada no próprio B3.

A Carta de Garantia de Atualização de Dados de 26/09/2026 está com status:

**NÃO CERTIFICADA — PENDÊNCIA DE FRESCOR**

Para o COTAHIST, o documento registra:

- geração do dataset: 26/09/2026;
- última data de mercado registrada: 22/09/2026;
- período declarado: 1986–2026.

Portanto, nenhum backtest deverá interpretar automaticamente o repositório B3 como cobertura integral até a data civil corrente.

O backtest deve registrar explicitamente a última sessão efetivamente disponível.

---

## 8. SEPARAÇÃO RAW / NORMALIZED / BACKTEST

A cadeia deverá ser:

`RAW B3`
→ `NORMALIZED B3`
→ `DATASET DE PESQUISA`
→ `FEATURES`
→ `MÓDULO`
→ `BACKTEST`

Nunca alterar o RAW.

Qualquer ajuste, agregação, normalização, filtro ou transformação deve gerar uma camada derivada identificável.

---

## 9. CONTROLE DE LOOK-AHEAD

Esta associação deverá obedecer a uma regra crítica:

**nenhuma informação futura poderá entrar no cálculo de uma decisão histórica.**

Exemplos de risco:

- usar o fechamento do dia para calcular um indicador que supostamente existia antes do fechamento;
- usar estatísticas de todo o período para normalizar uma observação histórica;
- ajustar parâmetros com dados que pertencem ao período de teste;
- usar catálogo futuro para definir universo histórico.

Cada backtest deverá declarar sua janela de treinamento, validação e teste.

---

## 10. PRIMEIROS DATASETS A CONSIDERAR

### B01 — COTAHIST

Uso inicial:
- preço;
- volume;
- quantidade;
- séries históricas;
- regime;
- sazonalidade.

Status:
**CANDIDATO PARA BACKTEST**

### B02 — Dados de negócio a negócio

Uso potencial:
- microestrutura;
- fluxo;
- ciclos;
- intensidade;
- eventos intradiários.

Status:
**CANDIDATO — NECESSITA VALIDAÇÃO DE ESCOPO E COBERTURA**

### B03 — Catálogo de instrumentos

Uso:
- identidade dos ativos;
- validade temporal;
- universo negociável;
- identificação de instrumentos.

Status:
**CANDIDATO PARA CONTROLE DO UNIVERSO**

---

## 11. PRINCÍPIO CTESÍBIO A TESTAR

A primeira hipótese experimental deverá ser:

**Uma referência dinâmica pode tornar uma medida de fluxo/atividade mais comparável entre períodos com diferentes níveis absolutos de negociação.**

O teste deverá comparar, no mínimo:

### Modelo A
Referência fixa ou convencional.

### Modelo B
Referência adaptativa inspirada no princípio de nível constante.

A comparação deve ser estatística e temporalmente controlada.

---

## 12. NÃO COPIAR AUTOMATICAMENTE OS DADOS

A decisão inicial é:

**NÃO DUPLICAR O ACERVO B3.**

Motivos:

1. evita divergência entre repositórios;
2. preserva uma única fonte de dados;
3. reduz armazenamento redundante;
4. facilita auditoria;
5. permite rastrear exatamente a versão utilizada;
6. mantém os dados e os modelos separados.

Se no futuro houver necessidade de um dataset congelado para reprodução, ele poderá ser materializado neste projeto como **snapshot de pesquisa**, com hash e identificação completa da origem.

---

## 13. STATUS

Dados B3 identificados:
**SIM**

Fonte externa associável:
**SIM**

COTAHIST disponível no B3:
**SIM**

Dados de microestrutura identificados:
**SIM, com necessidade de validação individual**

Backtest já executado neste projeto:
**NÃO**

Dataset congelado para este projeto:
**NÃO**

Contrato formal de consumo:
**CRIADO NESTE DOCUMENTO**

Validação de frescor integral:
**NÃO CERTIFICADA**

---

## 14. REGRA DE AUDITORIA

Nenhum resultado futuro deverá ser apresentado simplesmente como:

`BACKTEST BRICKMASTER`

Deverá ser possível reconstruir:

`RESULTADO`
→ `MODELO`
→ `PARÂMETROS`
→ `DATASET`
→ `ARQUIVO`
→ `COMMIT B3`
→ `PERÍODO`
→ `TRANSFORMAÇÕES`
→ `CÓDIGO`
→ `EXECUÇÃO`

Esse será o vínculo formal entre o projeto Ctesíbio, o repositório B3 e o futuro BRICKMASTER.

---

## ESTADO

**ASSOCIAÇÃO ARQUITETURAL: APROVADA PARA PESQUISA**

**EXECUÇÃO DE BACKTEST: NÃO INICIADA**

**VALIDAÇÃO DOS DATASETS PARA CADA MÓDULO: PENDENTE**

**FRESCOR GLOBAL DO B3: NÃO CERTIFICADO**

**PRÓXIMO PASSO:** selecionar e auditar o primeiro dataset B3 para o M01 — Fluxo Normalizado, sem ainda executar backtest.
