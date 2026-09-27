# ETAPA 13 — VALIDAÇÃO FINAL, RECONSTRUÇÃO HISTÓRICA E COMPARAÇÃO

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Caminho:** engenharia/ETAPA_13_VALIDACAO_FINAL_RECONSTRUCAO_HISTORICA_COMPARACAO_V1.md  
**Versão:** V1  
**Etapa:** 13  
**Status:** Especificação para execução e fechamento técnico  
**Data de criação:** 27/09/2026

---

## 1. OBJETIVO

Consolidar a validação final do projeto, separando rigorosamente: (1) o que pode ser sustentado por evidência histórica; (2) o que corresponde a reconstrução ou interpretação técnica; e (3) o que é solução moderna de engenharia.

A validação final deverá demonstrar que o protótipo atende aos requisitos funcionais, metrológicos, de robustez, segurança, repetibilidade e auditabilidade definidos nas etapas anteriores, sem apresentar uma solução moderna como se fosse necessariamente a configuração histórica original.

## 2. PRINCÍPIO DE GOVERNANÇA DA EVIDÊNCIA

Toda afirmação sobre o relógio de Ctesíbio deve receber uma classificação explícita:

- **HISTÓRICO:** diretamente sustentado por fonte primária, edição crítica ou evidência arqueológica/documental adequada.
- **INTERPRETAÇÃO:** leitura técnica de uma fonte que admite mais de uma interpretação.
- **RECONSTRUÇÃO:** solução necessária para transformar evidência incompleta em mecanismo funcional.
- **PROPOSTA MODERNA:** decisão de engenharia contemporânea.
- **HIPÓTESE:** solução ainda não suficientemente demonstrada.
- **NÃO DETERMINADO:** informação que as fontes disponíveis não permitem estabelecer com segurança.

Regra central: ausência de evidência não deve ser convertida em certeza histórica.

## 3. CAMADAS DE VALIDAÇÃO

### 3.1 Camada histórica

Verificar princípio hidráulico, reservatório regulado, flutuador, indicação, transmissão, descarga/reset, escala sazonal e todos os elementos efetivamente documentados versus elementos inferidos.

### 3.2 Camada reconstrutiva

Verificar coerência física, hidráulica e cinemática; repetição do ciclo; compatibilidade entre componentes; hipóteses necessárias para completar lacunas históricas.

### 3.3 Camada projetual

Verificar precisão, robustez, repetibilidade, segurança, manutenção, instrumentação, registro de dados, calibração e auditabilidade.

## 4. MATRIZ FINAL DE EVIDÊNCIA

Cada componente deverá ser registrado com: elemento, evidência histórica, classe A–E, reconstrução, solução moderna e incerteza.

| Elemento | Evidência histórica | Classe | Reconstrução | Solução moderna | Incerteza |
|---|---|---|---|---|---|
| Reservatório | registrar fonte validada | A–E | geometria funcional | reservatório transparente/controlado | baixa/média/alta |
| Controle de nível | registrar fonte validada | A–E | regulador hidráulico | válvula/boia/regulador | baixa/média/alta |
| Flutuador | registrar fonte validada | A–E | corpo flutuante guiado | polímero técnico | baixa/média/alta |
| Indicador | registrar fonte validada | A–E | transmissão float-indicador | escala mecânica/digital | baixa/média/alta |
| Escala sazonal | registrar fonte validada | A–E | escala variável | escala física ou modelo digital | baixa/média/alta |
| Descarga | registrar fonte validada | A–E | sifão ou mecanismo equivalente | sifão/atuador | baixa/média/alta |
| Reset | registrar fonte validada | A–E | reposicionamento | atuador/mecanismo mecânico | baixa/média/alta |
| Engrenagens | registrar fonte validada | A–E | transmissão cinemática | engrenagens/POM/metal | baixa/média/alta |

A tabela final só poderá ser preenchida com evidência efetivamente validada.

## 5. MATRIZ DE COMPARAÇÃO HISTÓRICO × RECONSTRUÇÃO × MODERNO

Para cada solução deverá existir a cadeia: **Fonte → afirmação → interpretação → reconstrução → requisito → componente → teste → resultado**.

Exemplo: controle de nível — verificar documentação; determinar o princípio funcional; estabelecer geometria necessária; escolher regulador moderno; testar estabilidade de H; registrar erro, repetibilidade e incerteza.

## 6. VALIDAÇÃO HIDRÁULICA FINAL

### 6.1 Estabilidade do nível

Medir H médio, H máximo, H mínimo, desvio-padrão, deriva e tempo de estabilização. O limite quantitativo deverá ser definido antes do ensaio e vinculado à incerteza metrológica.

### 6.2 Controle de vazão

Avaliar Q_in, Q_out, estabilidade temporal, resposta a perturbações e resposta a variações de temperatura e alimentação.

### 6.3 Modelo hidráulico

Comparar os dados com A dH/dt = Q_in - Q_out e, quando aplicável, Q_out ≈ C_d A_o sqrt(2 g H). Diferenças deverão ser registradas como erro do modelo, parâmetro não identificado ou fenômeno físico adicional.

## 7. VALIDAÇÃO DA CADEIA DE MEDIÇÃO

Cadeia final: **Nível → Flutuador → Transmissão → Indicador → Registro → Referência temporal**.

Avaliar linearidade, repetibilidade, resolução, histerese, atrito, folga, desalinhamento, erro de transmissão, erro de indicação e erro de registro. A indicação não será considerada validada apenas porque o mecanismo se movimenta; deve haver comparação com referência independente.

## 8. VALIDAÇÃO DO CICLO AUTOMÁTICO

Sequência: **ENCHIMENTO → ESTABILIZAÇÃO → MEDIÇÃO → LIMITE → DESCARGA → RESET → VERIFICAÇÃO → NOVO CICLO**.

Registrar cycle_id, tempos de transição, configuração, resultados, alarmes, falhas e recuperação. O ciclo somente será válido quando todas as transições obrigatórias forem confirmadas.

## 9. VALIDAÇÃO DA DESCARGA E DO RESET

Avaliar nível de disparo, tempo até descarga, duração, volume descarregado, nível residual, recuperação, posição final e repetibilidade. Verificar descarga parcial, sifonagem indevida, retorno incompleto, bloqueio, vazamento, disparo prematuro, ausência de disparo e reset incompleto.

A atualização da escala ou indicação somente ocorrerá depois da confirmação do reset hidráulico/mecânico.

## 10. VALIDAÇÃO DA COMPENSAÇÃO SAZONAL

Fluxo: **Referência temporal → Modelo sazonal → Parâmetros → Escala/Atuador → Indicação**.

Verificar convenção temporal, data, localização, duração de luz/escuridão, resolução, versão do modelo, arredondamento, atualização e comportamento em mudança de data ou parâmetros. Correção temporal deve ser identificada como correção de modelo, não como correção hidráulica.

## 11. VALIDAÇÃO DE ROBUSTEZ

Reutilizar os resultados da Etapa 12 para verificar ciclos repetidos, desgaste, variação térmica, perturbação de alimentação, obstrução controlada, contaminação controlada, perda de alimentação elétrica, falha de sensor, falha de comunicação e recuperação.

Classificar cada resultado como aprovado, aprovado com restrição, reprovado ou inconclusivo. Resultado inconclusivo não poderá ser usado como aprovação.

## 12. MÉTRICAS FINAIS

| Métrica | Resultado | Incerteza | Critério | Status |
|---|---:|---:|---:|---|
| estabilidade de nível | registrar | registrar | pré-declarado | P/A/R/I |
| erro de medição | registrar | registrar | pré-declarado | P/A/R/I |
| repetibilidade | registrar | registrar | pré-declarado | P/A/R/I |
| reproducibilidade | registrar | registrar | pré-declarado | P/A/R/I |
| tempo de descarga | registrar | registrar | pré-declarado | P/A/R/I |
| repetibilidade do reset | registrar | registrar | pré-declarado | P/A/R/I |
| erro sazonal | registrar | registrar | pré-declarado | P/A/R/I |
| deriva | registrar | registrar | pré-declarado | P/A/R/I |
| robustez | registrar | registrar | pré-declarado | P/A/R/I |
| integridade dos dados | registrar | registrar | pré-declarado | P/A/R/I |

Legenda: P = aprovado; A = aprovado com restrição; R = reprovado; I = inconclusivo.

## 13. CONTROLE DE INCERTEZA

O orçamento deverá incluir, quando aplicável, referência temporal, leitura de nível, resolução, estabilidade da vazão, temperatura, geometria, repetibilidade, reproducibilidade, deriva, atraso e incerteza do modelo sazonal.

Usar como estrutura geral: u_y² = Σ (∂f/∂x_i)² u_i². Quando houver correlação relevante, incluir covariância.

## 14. CONTRADIÇÕES HISTÓRICAS

Registrar afirmações conflitantes, traduções divergentes, reconstruções incompatíveis, componentes não comprovados, interpretações que extrapolem a evidência e lacunas documentais.

Para cada conflito registrar: fonte A, fonte B, ponto de divergência, natureza, evidência disponível, consequência para a reconstrução e decisão de projeto, quando necessária. Não selecionar uma versão apenas por conveniência técnica.

## 15. TESTE FINAL INTEGRADO

Executar em configuração congelada: identificação do protótipo; verificação da configuração; instrumentos; inicialização; alimentação hidráulica; estabilização; medição; registro; compensação temporal; limite; descarga; reset; verificação; repetição; análise; comparação com referência; emissão do resultado.

O ensaio deverá ser repetido em quantidade previamente definida no plano de validação.

## 16. CRITÉRIO DE ACEITAÇÃO FINAL

O sistema somente poderá ser declarado tecnicamente validado quando a cadeia de medição estiver documentada; referências independentes estiverem identificadas; testes críticos forem executados; critérios forem definidos previamente; resultados e incertezas forem registrados; ciclos forem repetíveis; descarga/reset forem verificáveis; compensação sazonal estiver validada; falhas críticas tiverem comportamento seguro; rastreabilidade estiver preservada; divergências históricas estiverem documentadas; hipóteses relevantes não forem apresentadas como fatos; e configuração, software, firmware, calibração e modelo estiverem congelados.

## 17. CRITÉRIO DE NÃO CONFORMIDADE

A validação será bloqueada por ausência de referência independente, perda de dados críticos, alteração não registrada, falha de segurança, falha de descarga/reset, erro acima do limite, comportamento não repetível sem explicação, incompatibilidade entre documentação e configuração física, impossibilidade de reconstruir um ciclo ou evidência histórica essencial sem rastreabilidade.

## 18. DOSSIÊ FINAL DE EVIDÊNCIAS

Estrutura mínima:

- 01_resumo_executivo/
- 02_base_historica/
- 03_matriz_evidencias/
- 04_reconstrucao/
- 05_arquitetura_final/
- 06_bom_final/
- 07_desenhos/
- 08_calibracao/
- 09_testes/
- 10_dados_brutos/
- 11_dados_processados/
- 12_incerteza/
- 13_compensacao_sazonal/
- 14_robustez/
- 15_falhas/
- 16_auditabilidade/
- 17_contradicoes_historicas/
- 18_comparacao_historico_moderno/
- 19_resultado_final/
- 20_manifesto_de_versao/

## 19. MANIFESTO DA CONFIGURAÇÃO VALIDADA

Registrar prototype_id, versão mecânica, hidráulica, elétrica, firmware, software, modelo sazonal, calibração, documentação, data de congelamento, operador, instrumentos, referências, hashes dos arquivos críticos e resultado da validação.

## 20. REGRA DE AUDITABILIDADE FINAL

Qualquer terceiro autorizado deverá conseguir seguir: **Fonte histórica → evidência → interpretação → reconstrução → requisito → componente → configuração → teste → dado bruto → processamento → resultado → conclusão técnica**.

Sem essa cadeia, a validação final será considerada incompleta.

## 21. REGRA DE NÃO SOBRESTIMAÇÃO HISTÓRICA

Evitar afirmar que Ctesíbio utilizou exatamente determinado componente, geometria ou configuração quando isso não estiver demonstrado. Preferir: “a fonte descreve...”, “a evidência é compatível com...”, “a reconstrução adotou...”, “para o protótipo moderno foi utilizado...”, “não foi possível determinar...” e “esta solução é uma hipótese de reconstrução...”.

## 22. COMPARAÇÃO FINAL

| Dimensão | Princípio histórico | Reconstrução | Implementação moderna |
|---|---|---|---|
| Controle hidráulico | nível/fluxo controlado | mecanismo funcional reconstruído | regulador de precisão |
| Medição | flutuador/indicador | cadeia mecânica reconstruída | sensor + indicador |
| Tempo | escala temporal | escala reconstruída | referência temporal auditável |
| Sazonalidade | adaptação da escala | modelo interpretativo | algoritmo/escala configurável |
| Descarga | ciclo hidráulico | sifão/mecanismo equivalente | descarga controlada |
| Reset | novo ciclo | mecanismo reconstruído | atuador/intertravamento |
| Precisão | dependente do sistema hidráulico | estimada experimentalmente | calibrada e quantificada |
| Auditabilidade | limitada pela evidência disponível | documentação de reconstrução | registro digital versionado |

A tabela não deve ser interpretada como afirmação de que todos os elementos modernos existiam no mecanismo antigo.

## 23. RESULTADO ESPERADO

A conclusão técnica deverá separar três níveis:

### Nível A — Histórico
O que pode ser afirmado com segurança sobre o relógio de Ctesíbio.

### Nível B — Reconstrutivo
O que foi necessário inferir para obter um mecanismo funcional.

### Nível C — Moderno
O que foi projetado especificamente para obter precisão, robustez, repetibilidade e auditabilidade contemporâneas.

Esses níveis não devem ser misturados.

## 24. LIBERAÇÃO DA ETAPA 13

A etapa será considerada encerrada somente após matriz histórica preenchida, matriz de reconstrução preenchida, matriz moderna preenchida, testes finais concluídos, resultados comparados com critérios, incerteza consolidada, contradições registradas, configuração congelada, dossiê final indexado, manifesto de versão criado e rastreabilidade auditada.

## 25. PRÓXIMA ETAPA

**Etapa 14 — Dossiê Técnico Final, Manual de Operação e Plano de Reprodução**

Escopo previsto: consolidar a configuração final; transformar a arquitetura em documentação de fabricação; produzir manual de operação; produzir procedimento de calibração; produzir plano de manutenção; produzir plano de reprodução; definir pacote de publicação; organizar documentação final para terceiros; estabelecer versão oficial de referência do projeto.
