# AUDITORIA_DADOS_B3_DISPONIVEIS_PARA_MODULO_MERCADO_V1

**Arquivo:** AUDITORIA_DADOS_B3_DISPONIVEIS_PARA_MODULO_MERCADO_V1.md  
**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Aplicação:** Módulos de Mercado / BRICKMASTER  
**Caminho:** MODULO DE MERCADO/AUDITORIA_DADOS_B3_DISPONIVEIS_PARA_MODULO_MERCADO_V1.md  
**Data:** 27/09/2026  
**Fonte auditada:** carlos-andrade/B3  
**Regra:** somente dados com evidência persistida e status compatível podem ser tratados como prontos.

## 1. Resultado executivo

A auditoria identificou quatro classes de informação no repositório B3:

1. **PRONTO PARA USO CONTROLADO:** COTAHIST corrente 2026.
2. **PRONTO COMO FONTE MACRO AUXILIAR:** BCB/SGS núcleo e Copom, armazenados no B3, mas não são dados de mercado B3.
3. **ESTRUTURA PRONTA, DADOS AINDA NÃO CERTIFICADOS:** índices/carteiras B3.
4. **INFRAESTRUTURA/CONTRATO PRONTOS, DATASET NÃO CERTIFICADO:** derivativos, futuros, opções e intraday/microestrutura.

## 2. COTAHIST — DISPONÍVEL E CERTIFICADO

Dataset corrente:
- arquivo: dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json
- status: VIGENTE
- status_frescor: VALIDADO
- última observação: 2026-09-25
- composição: snapshot anual + incrementos diários validados
- fail_closed: true

Incrementos validados:
- 23/09/2026: 15.747 linhas
- 24/09/2026: 15.903 linhas
- 25/09/2026: 16.593 linhas

O snapshot anual de 2026 permanece imutável até 22/09/2026; o dataset corrente V1.1 utiliza overlay diário auditável posterior.

Conclusão para o módulo:
**APTO PARA BACKTEST EDA/EOD**, desde que o backtest registre a versão do dataset, período, instrumentos e transformações.

Usos compatíveis:
- preço;
- retorno;
- amplitude;
- volatilidade;
- volume financeiro;
- VWAP/TWAP quando a granularidade disponível suportar;
- regime;
- normalização de atividade;
- testes do princípio de referência dinâmica.

Não usar COTAHIST/EOD como:
- fluxo de ordens;
- agressão;
- Cumulative Delta.

## 3. HISTÓRICO COTAHIST 1987–2025

Estado B3:
**CONDICIONAL**.

Existe cobertura histórica, mas a certificação é anual/por período. Não deve ser tratada como uma série integral já certificada sem verificar os anos específicos utilizados no backtest.

1986:
**EXCEÇÃO HISTÓRICA NÃO CERTIFICÁVEL**.

Regra: não fabricar, interpolar ou preencher observações ausentes.

## 4. ÍNDICES B3

O B3 criou a infraestrutura V1 para certificação da composição diária de carteiras de índices.

Inventário identificado:
- 33 códigos de índices de ações no escopo V1, incluindo IBOV, IBRX, IBRX50, SMLL, IDIV, IFIX e outros.
- fonte primária: canal público B3/API oficial.
- captura RAW, SHA-256, normalização, manifestos e índice oficial estão previstos no contrato.

Script atual:
scripts/ingestao/importar_indices_b3_v1.py

Estado de certificação em 27/09/2026:
**NÃO CERTIFICADO**.

A infraestrutura está instalada, mas a auditoria não encontrou evidência persistida suficiente para declarar o dataset de composição de carteiras pronto.

Conclusão para o módulo:
**NÃO CONSUMIR COMO DATASET CERTIFICADO AINDA.**

## 5. CARTEIRAS B3

Estado:
**NÃO CERTIFICADO**.

Há identificação da carteira definitiva do Ibovespa e da fonte oficial, mas a própria certificação B3 exige arquivo persistido, metadados, hash, data de referência e manifesto de qualidade.

Uso atual:
**referência metodológica apenas**.

## 6. INTRADAY / MICROESTRUTURA

O repositório possui estrutura para:
- market data histórico;
- microestrutura;
- Pesquisa por Pregão;
- dados BDI;
- contratos de ingestão;
- validadores;
- processamento de negócio a negócio.

Entretanto, o estado global B3 em 27/09/2026 mantém:
**B3_INTRADAY_WIN_WDO_DI = NÃO CERTIFICADO**.

O próprio catálogo de granularidade determina que a granularidade e a identificação do agressor precisam ser verificadas na fonte efetivamente capturada.

Conclusão:
**INFRAESTRUTURA DISPONÍVEL; DATASET CERTIFICADO PARA MICROESTRUTURA AINDA NÃO DISPONÍVEL.**

Isso é particularmente importante para qualquer futuro módulo que pretenda trabalhar com:
- agressão;
- fluxo;
- delta;
- intensidade de negócios;
- pressão intradiária.

## 7. BDI

Estrutura identificada:
dados/bdi/

O BDI foi organizado para estudos de:
- liquidez;
- volume;
- derivativos;
- empréstimos;
- negócio a negócio;
- microestrutura.

Entretanto, a pasta 2026 atualmente apresenta documentação/protocolo, sem evidência suficiente para classificar um dataset corrente BDI como certificado para backtest.

Estado:
**NÃO CERTIFICADO PARA CONSUMO AUTOMÁTICO.**

## 8. MARKET DATA

Estrutura identificada:
dados/market_data/

Fontes documentadas:
- BVBG.086.01 — PriceReport;
- BVBG.186.01 — Simplified Price Report Equities;
- BVBG.187.01 — Simplified Price Report Derivatives.

A documentação explicitamente impede tratar BVBG.186.01 e BVBG.187.01 como feed tick a tick.

Estado:
**FONTE/ARQUITETURA DOCUMENTADA; DATASET DE MICROESTRUTURA CERTIFICADO NÃO CONFIRMADO.**

## 9. BCB/SGS E COPOM

O repositório B3 também contém dados macroeconômicos certificados:

- BCB/SGS núcleo macro: CERTIFICADO;
- Copom 281: CERTIFICADO.

Esses dados podem ser úteis como variáveis externas de contexto/regime, mas não devem ser classificados como dados de mercado B3.

Uso potencial no módulo:
- regime macro;
- eventos;
- análise de sensibilidade;
- estudos de contexto.

Não devem ser misturados ao dataset de preço sem uma camada temporal explícita.

## 10. MATRIZ DE DISPONIBILIDADE PARA O PROJETO CTESÍBIO

| Dataset | Estado B3 | Uso no módulo | Situação |
|---|---|---|---|
| COTAHIST corrente 2026 | CERTIFICADO | preço/volume/regime | APTO |
| COTAHIST 1987–2025 | CONDICIONAL | backtest histórico | VALIDAR ANO A ANO |
| COTAHIST 1986 | EXCEÇÃO | histórico | BLOQUEADO |
| Índices B3 | NÃO CERTIFICADO | referência dinâmica/universo | BLOQUEADO |
| Carteiras B3 | NÃO CERTIFICADO | composição/universo | BLOQUEADO |
| Intraday WIN/WDO/DI | NÃO CERTIFICADO | microestrutura | BLOQUEADO |
| Derivativos/futuros/opções | NÃO CERTIFICADO | regime/microestrutura | BLOQUEADO |
| BDI | NÃO CERTIFICADO | volume/liquidez/microestrutura | BLOQUEADO |
| BCB/SGS núcleo | CERTIFICADO | contexto macro | APTO COMO AUXILIAR |
| Copom 281 | CERTIFICADO | evento macro | APTO COMO AUXILIAR |

## 11. Dados atualmente prioritários para M01

Para o primeiro módulo — **M01 Fluxo Normalizado** — o dataset imediatamente utilizável é o **COTAHIST corrente 2026**, porque já possui evidência de frescor e validação.

A hipótese inicial deve permanecer:

> Uma referência dinâmica pode tornar uma medida de fluxo/atividade mais comparável entre períodos com diferentes níveis absolutos de negociação.

O teste inicial deve comparar:
- referência fixa;
- referência adaptativa;
- estabilidade;
- frequência de eventos;
- sensibilidade a volume;
- sensibilidade a regime;
- degradação fora da amostra.

Nenhuma fórmula, limiar ou sinal deve ser considerado validado antes do backtest.

## 12. Controle de look-ahead

O dataset deve ser congelado por data de referência antes da execução de cada experimento.

É proibido usar:
- composição futura de índices;
- carteira futura;
- informação publicada posteriormente;
- dado corrigido posteriormente sem preservar o estado disponível na data do teste.

A informação utilizada deve ser temporalmente disponível no instante simulado.

## 13. Fontes de auditoria no B3

Principais evidências consultadas:

- governanca/garantia_atualizacao_dados/CERTIFICACAO_DOMINIOS_B3_2026-09-27.md
- governanca/garantia_atualizacao_dados/CERTIFICACAO_DOMINIOS_B3_2026-09-27.json
- governanca/garantia_atualizacao_dados/MATRIZ_GLOBAL_FRESCOR_DADOS_B3_2026-09-27.md
- governanca/garantia_atualizacao_dados/DIAGNOSTICO_FRESCOR_COTAHIST_2026-09-27.md
- dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json
- dados/market_data/README.md
- dados/market_data/PROVEDORES_E_GRANULARIDADE.md
- dados/bdi/README.md
- governanca/indices_b3/INVENTARIO_INDICES_B3_V1.md
- scripts/ingestao/importar_indices_b3_v1.py
- docs/ingestao/REGRAS_PERMANENTES_INGESTAO_HISTORICA_B3_V1.0.md

## 14. Estado da auditoria

**AUDITORIA REALIZADA.**

O resultado não promove datasets bloqueados para uso. A separação entre:
- dado certificado;
- dado condicional;
- infraestrutura;
- fonte documentada;
- dado não certificado

deve ser preservada.

## 15. Próxima etapa autorizada

A próxima etapa é construir o **CONTRATO DE DATASET DO M01**, utilizando o COTAHIST corrente certificado como primeira fonte.

O contrato deverá congelar:
- dataset;
- versão;
- período;
- instrumentos;
- campos;
- transformação;
- granularidade;
- regra temporal;
- controle de look-ahead;
- hash;
- critérios de entrada no backtest;
- critérios de exclusão.

**Estado:** AUDITADO PARA SELEÇÃO — BACKTEST AINDA NÃO EXECUTADO.
