# MÓDULO DE MERCADO — BRICKMASTER INSPIRADO EM CTESÍBIO — V1

## Arquivo
MODULO_MERCADO_BRICKMASTER_CTESIBIO_V1.md
## Projeto
RELÓGIO DE ÁGUA DE CTESÍBIO
## Aplicação derivada
Pesquisa para desenvolvimento de módulos de análise de mercado destinados ao ecossistema BRICKMASTER.
## Repositório
carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO
## Pasta
MODULO DE MERCADO/
## Data
27/09/2026

## 1. REVELAÇÃO DE CONTEXTO
Todo o levantamento realizado no projeto do relógio de água de Ctesíbio deve ser tratado também como pesquisa tecnológica para desenvolvimento de módulos de análise de mercado.
O objetivo não é reproduzir literalmente a clepsidra, mas transferir princípios de engenharia observados no sistema hidráulico para uma arquitetura quantitativa de análise de mercado.
A separação entre HISTÓRICO, RECONSTRUÇÃO, PRINCÍPIO DE ENGENHARIA, ANALOGIA COMPUTACIONAL, MÓDULO DE MERCADO e RESULTADO EXPERIMENTAL deve ser preservada para permitir auditoria posterior.

## 2. PRINCÍPIO CENTRAL A SER TRANSFERIDO
Reduzir o efeito de uma variável que muda continuamente utilizando uma referência estabilizada antes de realizar a medição.
Na clepsidra, a pressão hidráulica varia com a altura da coluna de água. O sistema de nível constante reduz essa variação.
Na análise de mercado, a hipótese é construir uma referência dinâmica que reduza a distorção provocada por volume absoluto diferente entre períodos, volatilidade variável, mudança de liquidez, velocidade de negociação e regime intradiário.
Isso é HIPÓTESE DE PROJETO, não fato validado.

## 3. MÓDULOS DE MERCADO A INVESTIGAR

### M01 — FLUXO NORMALIZADO
Transformar fluxo/volume observado em medida comparável ao longo do tempo.
Entradas possíveis: volume, agressão compradora, agressão vendedora, número de negócios, delta, volume por intervalo e tempo.
Saída conceitual: Fluxo_Normalizado.
Analogia: reservatório de nível constante.

### M02 — PRESSÃO DE MERCADO
Criar indicador equivalente à pressão hidráulica, relacionando fluxo observado com referência dinâmica.
Exemplo conceitual: Pressão_Mercado = Fluxo_Observado / Referência_de_Fluxo.
Estados possíveis: pressão compradora, pressão vendedora, equilíbrio, expansão e compressão.
Não definir limiares antes dos testes.

### M03 — NÍVEL CONSTANTE DE REFERÊNCIA
Criar linha-base dinâmica contra a qual o fluxo de mercado seja comparado.
Possíveis referências: média móvel adaptativa, média ponderada por volume, mediana móvel, baseline por horário, baseline por sessão ou referência híbrida volume × tempo.

### M04 — FLUTUADOR DE FLUXO
Representar a posição relativa do fluxo em relação à referência.
Possível variável: Posição_Fluxo = f(Fluxo - Referência).
A posição pode alimentar escala, classificação de estado, gatilho, painel ou filtro.
Não deve ser interpretada como previsão de preço.

### M05 — DESCARGA AUTOMÁTICA / RESET DE CICLO
Detectar quando o estado acumulado atingiu limite operacional e reiniciar a referência.
Analogia: sifão automático.
Possíveis eventos: ciclo completo, saturação, mudança de regime, encerramento de sessão ou reset por evento.
O histórico do ciclo anterior deve ser preservado.

### M06 — CICLO DE PRESSÃO
Arquitetura: ACUMULAÇÃO → ESTABILIZAÇÃO → MEDIÇÃO → LIMITE → DESCARGA → RESET → NOVO CICLO.
Cada ciclo deve possuir ID, início, fim, duração, intensidade máxima, intensidade média, direção, volume acumulado, número de eventos, condição de encerramento e resultado posterior.

### M07 — COMPENSAÇÃO INTRADIÁRIA
Adaptar a referência ao comportamento esperado de cada período do pregão.
Analogia: compensação sazonal.
Variáveis possíveis: horário, sessão, volume típico, volatilidade típica, liquidez, abertura, meio do pregão e fechamento.

### M08 — DETECTOR DE REGIME
Classificar o estado atual antes de interpretar o fluxo.
Estados experimentais: BAIXA_ATIVIDADE, EQUILÍBRIO, EXPANSÃO, PRESSÃO_COMPRADORA, PRESSÃO_VENDEDORA e TRANSIÇÃO.
Os estados devem ser definidos posteriormente por regras mensuráveis.

### M09 — INTEGRIDADE DO FLUXO
Detectar situações em que a medição do fluxo pode estar distorcida.
Anomalias possíveis: ausência de dados, salto de volume, mudança brusca de liquidez, dados inconsistentes, interrupção, duplicidade, mudança de configuração e comportamento incompatível com a referência.
Saídas: FLUXO_CONFIÁVEL, FLUXO_COM_RESTRIÇÃO e FLUXO_INVALIDO.

### M10 — PAINEL CTESÍBIO DE MERCADO
Painel integrado de fluxo bruto, fluxo normalizado, referência, pressão, posição, ciclo, regime, integridade, reset e histórico.

## 4. ARQUITETURA PROPOSTA
DADOS DE MERCADO → PRÉ-PROCESSAMENTO → REFERÊNCIA DINÂMICA → NORMALIZAÇÃO → PRESSÃO → ESTADO / FLUTUADOR VIRTUAL → DETECÇÃO DE LIMITE → RESET / NOVO CICLO → REGIME → PAINEL / SINAL → REGISTRO AUDITÁVEL

## 5. VARIÁVEIS
Entrada: preço, volume, negócios, agressão, delta, máxima/mínima, spread quando disponível, tempo e sessão.
Estado: referência, desvio, pressão, velocidade, aceleração, acumulação, posição virtual, ciclo e regime.
Controle: limiar, janela, fator de normalização, condição de reset e condição de invalidação.
Nenhum parâmetro deve ser considerado ótimo antes de validação.

## 6. PRINCÍPIO DE AUDITORIA
Cada módulo deverá responder: qual foi a entrada; qual referência estava ativa; qual transformação foi aplicada; qual era o estado anterior; qual evento provocou a mudança; qual estado foi produzido; houve reset; por que houve reset; qual configuração estava ativa; o cálculo pode ser reproduzido?

## 7. LIMITAÇÃO DA ANALOGIA
Não transformar a analogia hidráulica em afirmação de que o mercado funciona como um fluido.
Não assumir que pressão hidráulica = pressão de mercado; nível = preço; flutuador = indicador preditivo; sifão = reversão; descarga = venda; enchimento = compra.
Essas são analogias de arquitetura. A validade de cada módulo deverá ser demonstrada por dados.

## 8. PLANO DE EXPERIMENTAÇÃO
Fase M0 — Definição: formalizar variáveis e fórmulas.
Fase M1 — Dados históricos: testar sem execução financeira.
Fase M2 — Replay: preservar causalidade temporal.
Fase M3 — Comparação: referência fixa versus adaptativa.
Fase M4 — Robustez: testar sessões, ativos, regimes e liquidez.
Fase M5 — Integração: avaliar integração com módulos existentes do BRICKMASTER.
Fase M6 — Validação: separar desenvolvimento, validação e teste fora da amostra.

## 9. MÉTRICAS
Estabilidade, repetibilidade, latência, frequência de sinais, distribuição por regime, sensibilidade a parâmetros, comportamento diante de mudanças de liquidez e volatilidade, falsos eventos, consistência entre sessões e degradação fora da amostra.
Se houver posterior uso para decisão operacional, métricas financeiras devem ser especificadas separadamente.

## 10. HIPÓTESES PRIORITÁRIAS
H01 — Uma referência dinâmica de fluxo pode produzir medidas mais comparáveis que o volume bruto.
H02 — Normalização por regime intradiário pode reduzir distorções causadas pela variação natural de atividade.
H03 — Um ciclo acumulativo com reset controlado pode representar mudanças de regime de fluxo de maneira auditável.
H04 — Separar intensidade de fluxo de direção de preço pode produzir uma leitura de estado mais informativa.
Todas permanecem NÃO VALIDADAS.

## 11. RELAÇÃO CTESÍBIO → MERCADO
Coluna de água → acumulação de fluxo.
Pressão hidráulica → intensidade relativa.
Nível constante → referência dinâmica.
Flutuador → estado virtual.
Indicador → série/escala.
Escala sazonal → ajuste intradiário.
Sifão → reset.
Engrenagens → máquina de estados.
Ciclo hidráulico → ciclo de mercado.
Registro de posição → registro auditável.
Esta é uma correspondência conceitual, não uma equivalência física.

## 12. CONTROLE DE VERSÃO E AUDITORIA
Todos os módulos derivados desta pesquisa devem permanecer em MODULO DE MERCADO/.
Cada módulo deverá possuir versão, data, objetivo, entradas, saídas, fórmula, parâmetros, hipóteses, limitações, dados utilizados, testes, resultados, conclusão e status de validação.
Estados permitidos: IDEIA → ESPECIFICAÇÃO → PROTÓTIPO → TESTE → VALIDAÇÃO → VALIDADO ou REJEITADO → ARQUIVADO.

## 13. ESTADO INICIAL
Módulos identificados: 10.
Fórmulas definitivas: NÃO DEFINIDAS.
Dados de mercado testados: NÃO.
Backtest: NÃO REALIZADO.
Replay: NÃO REALIZADO.
Validação: NÃO REALIZADA.
Integração BRICKMASTER: NÃO REALIZADA.
Conclusão: arquitetura de pesquisa criada; nenhuma hipótese de mercado considerada comprovada.