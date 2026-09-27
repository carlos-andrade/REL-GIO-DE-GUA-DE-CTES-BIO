# ETAPA 15 — AUDITORIA FINAL DO PROJETO, CONTROLE DE VERSÃO E LIBERAÇÃO OFICIAL

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Caminho:** engenharia/ETAPA_15_AUDITORIA_FINAL_CONTROLE_VERSAO_LIBERACAO_OFICIAL_V1.md  
**Versão:** V1  
**Etapa:** 15  
**Status:** Especificação para auditoria e release oficial  
**Data de criação:** 27/09/2026

---

## 1. OBJETIVO

Executar a auditoria final do projeto antes da sua liberação oficial, verificando consistência documental, rastreabilidade, integridade dos dados, coerência entre requisitos e implementação, controle de versões, evidências de teste, segurança, calibração e capacidade de reprodução.

A auditoria deve responder a uma pergunta objetiva: **é possível identificar exatamente o que foi projetado, por que foi projetado, com base em qual evidência, como foi construído, como foi testado, quais resultados foram obtidos e qual configuração está oficialmente liberada?**

## 2. ESCOPO DA AUDITORIA

A auditoria cobre:

- governança;
- pesquisa histórica;
- síntese técnica;
- modelo matemático;
- protótipo experimental;
- arquitetura física;
- BOM;
- fabricação;
- montagem;
- comissionamento;
- calibração;
- compensação sazonal;
- ciclo automático;
- integração e dados;
- robustez e falhas;
- validação final;
- dossiê técnico;
- manual de operação;
- reprodução;
- GitHub e controle de versão.

## 3. PRINCÍPIO DE AUDITORIA

Nenhuma conclusão será considerada sustentada apenas pela existência de um documento. Deve existir evidência verificável e rastreável.

A cadeia mínima é:

**Requisito → Projeto → Implementação → Teste → Dado → Análise → Resultado → Aprovação**

Para afirmações históricas:

**Fonte → Evidência → Interpretação → Reconstrução → Decisão de projeto**

## 4. CLASSIFICAÇÃO DOS RESULTADOS

Cada item auditado deverá receber:

- **CONFORME:** requisito atendido e evidência suficiente.
- **CONFORME COM RESTRIÇÃO:** atendido com limitação documentada.
- **NÃO CONFORME:** requisito não atendido ou evidência insuficiente.
- **NÃO APLICÁVEL:** justificativa documentada.
- **PENDENTE:** informação ou evidência ainda necessária.

Itens críticos pendentes ou não conformes bloqueiam a liberação oficial.

## 5. AUDITORIA DE REQUISITOS

Criar uma matriz final:

| ID | Requisito | Documento | Evidência | Teste | Resultado | Status |
|---|---|---|---|---|---|---|
| R01 | nível hidráulico estável | Etapas 5–8 | dados | hidráulico | registrar | — |
| R02 | medição rastreável | Etapas 8–11 | calibração | metrológico | registrar | — |
| R03 | compensação sazonal | Etapa 9 | modelo + teste | sazonal | registrar | — |
| R04 | ciclo automático | Etapa 10 | eventos | automático | registrar | — |
| R05 | auditabilidade | Etapa 11 | registros | integração | registrar | — |
| R06 | robustez | Etapa 12 | campanha | durabilidade | registrar | — |
| R07 | validação final | Etapa 13 | dossiê | integrado | registrar | — |
| R08 | reprodução | Etapa 14 | pacote técnico | réplica | registrar | — |

Nenhum requisito crítico poderá permanecer sem evidência.

## 6. AUDITORIA HISTÓRICA

Verificar se cada afirmação histórica relevante possui:

- fonte identificada;
- classificação de evidência;
- trecho ou referência documental;
- interpretação explicitada quando necessária;
- distinção entre fato e reconstrução;
- registro de contradições;
- nível de confiança.

É proibido elevar uma hipótese de reconstrução à categoria de fato histórico sem nova evidência.

## 7. AUDITORIA DO MODELO MATEMÁTICO

Verificar:

- definição das variáveis;
- unidades;
- equações;
- hipóteses;
- condições de contorno;
- parâmetros;
- valores de referência;
- identificação de parâmetros experimentais;
- propagação de incerteza;
- comparação entre previsão e experimento;
- limitações do modelo.

Todas as unidades deverão utilizar um sistema coerente, preferencialmente SI, salvo quando houver justificativa documentada.

## 8. AUDITORIA FÍSICA

Conferir se a unidade física corresponde à documentação:

- reservatórios;
- regulador;
- tubos;
- válvulas;
- flutuador;
- guia;
- transmissão;
- indicador;
- descarga;
- atuadores;
- sensores;
- estrutura;
- contenção;
- alimentação elétrica.

Qualquer diferença deverá ser classificada como alteração controlada ou não conformidade.

## 9. AUDITORIA DE BOM E DESENHOS

Verificar:

- todos os componentes presentes;
- quantidades corretas;
- materiais definidos;
- peças críticas identificadas;
- desenhos associados;
- revisões coerentes;
- tolerâncias críticas;
- componentes comerciais identificados;
- substituições autorizadas.

A BOM liberada deve corresponder à configuração física validada.

## 10. AUDITORIA DE CALIBRAÇÃO

Verificar:

- referência independente;
- rastreabilidade;
- data da calibração;
- validade definida;
- pontos utilizados;
- repetições;
- resultados;
- incerteza;
- certificado ou registro;
- configuração durante a calibração.

Alterações posteriores à calibração devem disparar avaliação de necessidade de recalibração.

## 11. AUDITORIA DOS TESTES

Para cada teste crítico verificar:

1. objetivo;
2. pré-condições;
3. configuração;
4. instrumentos;
5. procedimento;
6. critério de aceitação;
7. dados brutos;
8. processamento;
9. resultado;
10. responsável/data;
11. anomalias;
12. conclusão.

Teste sem dado bruto ou evidência equivalente deverá ser classificado como incompleto.

## 12. AUDITORIA DOS DADOS

Verificar:

- timestamps;
- cycle_id;
- prototype_id;
- versão da configuração;
- unidade de medida;
- frequência de aquisição;
- qualidade do dado;
- sincronização temporal;
- integridade;
- backups;
- hashes quando aplicáveis.

Dados brutos não devem ser sobrescritos.

## 13. AUDITORIA DO CICLO AUTOMÁTICO

Reconstruir pelo menos uma execução completa a partir dos registros:

**START → ENCHIMENTO → ESTABILIZAÇÃO → MEDIÇÃO → LIMITE → DESCARGA → RESET → VERIFICAÇÃO → PRONTO**

Confirmar que cada transição possui evidência temporal e que nenhuma etapa foi inferida apenas por ausência de erro.

## 14. AUDITORIA DE SEGURANÇA

Verificar:

- contenção secundária;
- overflow independente;
- drenagem;
- estabilidade estrutural;
- proteção de partes móveis;
- proteção elétrica;
- procedimento de parada;
- comportamento em falha;
- identificação de riscos residuais.

Falha de segurança crítica bloqueia o release.

## 15. AUDITORIA DE ROBUSTEZ

Verificar se os resultados da campanha de durabilidade foram preservados e se as conclusões correspondem aos dados.

Conferir:

- número de ciclos;
- interrupções;
- falhas;
- manutenção realizada;
- alterações durante a campanha;
- degradação;
- critérios de parada;
- comportamento após recuperação.

## 16. AUDITORIA DE SOFTWARE, FIRMWARE E MODELO

Registrar exatamente:

- versão do software;
- versão do firmware;
- versão do modelo sazonal;
- parâmetros;
- bibliotecas relevantes, quando aplicável;
- ambiente de execução;
- configuração de aquisição;
- hashes dos arquivos críticos.

Nenhuma versão utilizada para produzir resultados oficiais poderá permanecer ambígua.

## 17. AUDITORIA DE CONFIGURAÇÃO

Criar o identificador de configuração oficial:

**CONFIG-ID = protótipo + mecânica + hidráulica + elétrica + firmware + software + modelo + calibração + documentação**

O CONFIG-ID deverá ser associado aos resultados oficiais.

## 18. AUDITORIA DE REPRODUTIBILIDADE

Executar revisão documental simulando um terceiro sem acesso ao conhecimento informal da equipe.

Perguntas mínimas:

- consegue identificar cada peça?
- consegue saber como fabricar?
- consegue saber como montar?
- consegue saber como calibrar?
- consegue saber como operar?
- consegue saber quais critérios usar?
- consegue saber quais dados registrar?
- consegue reproduzir a análise?

Qualquer resposta negativa em item crítico gera pendência.

## 19. AUDITORIA DO REPOSITÓRIO

Verificar:

- estrutura de pastas;
- nomes de arquivos;
- versionamento;
- commits;
- ausência de duplicatas conflitantes;
- documentação de mudanças;
- workflows relevantes;
- scripts executáveis;
- relatórios;
- arquivos essenciais;
- consistência entre README e estrutura real.

## 20. INTEGRIDADE DE VERSÃO

A versão oficial deverá possuir:

- número de versão;
- data;
- commit SHA;
- lista de arquivos;
- configuração física correspondente;
- resultados associados;
- limitações conhecidas;
- status de release.

Uma versão não deve depender de arquivos não versionados para reproduzir o resultado oficial.

## 21. MATRIZ DE RASTREABILIDADE FINAL

A matriz final deverá ligar:

**REQ → DOC → COMP → CONFIG → TESTE → DADO → ANÁLISE → RESULTADO → RELEASE**

E, para história:

**FONTE → EVIDÊNCIA → INTERPRETAÇÃO → RECONSTRUÇÃO → COMPONENTE**

## 22. AUDITORIA DE ALTERAÇÕES

Toda alteração após a validação deverá registrar:

- motivo;
- autor;
- data;
- arquivo afetado;
- versão anterior;
- versão nova;
- impacto técnico;
- impacto metrológico;
- impacto de segurança;
- necessidade de novo teste;
- necessidade de recalibração;
- aprovação.

## 23. CRITÉRIOS DE RELEASE OFICIAL

Liberar somente quando:

- requisitos críticos conformes;
- evidência histórica rastreável;
- configuração física identificada;
- BOM e desenhos consistentes;
- calibração válida;
- testes críticos concluídos;
- dados preservados;
- incertezas documentadas;
- segurança verificada;
- robustez avaliada;
- software/firmware/modelo versionados;
- documentação reproduzível;
- auditoria sem pendências críticas.

## 24. BLOQUEADORES DE RELEASE

São bloqueadores automáticos:

- falha de segurança crítica;
- ausência de calibração quando exigida;
- resultado crítico sem dado verificável;
- configuração desconhecida;
- divergência entre protótipo e documentação;
- requisito crítico sem teste;
- perda de dados brutos;
- alteração não versionada;
- erro acima do limite de aceitação;
- impossibilidade de reproduzir um resultado oficial.

## 25. RELATÓRIO FINAL DE AUDITORIA

O relatório deverá conter:

1. identificação do projeto;
2. versão auditada;
3. CONFIG-ID;
4. escopo;
5. documentos examinados;
6. testes examinados;
7. evidências históricas examinadas;
8. não conformidades;
9. pendências;
10. limitações;
11. conclusão de auditoria;
12. decisão de release;
13. assinatura/identificação dos responsáveis;
14. commit SHA da versão liberada.

## 26. ESTADOS OFICIAIS DO PROJETO

Usar os estados:

**EM DESENVOLVIMENTO → EM VALIDAÇÃO → AUDITADO → LIBERADO → SUPERADO**

Uma versão superada permanece preservada para rastreabilidade histórica.

## 27. RELEASE E PRESERVAÇÃO

O release oficial deverá preservar:

- código/documentação;
- dados brutos;
- relatórios;
- configurações;
- desenhos;
- BOM;
- registros de calibração;
- evidências históricas;
- resultados de testes;
- manifesto;
- hash dos artefatos críticos.

Nenhum release deverá apagar a versão anterior.

## 28. RESULTADO ESPERADO

Ao término desta etapa deverá ser possível identificar uma única configuração oficial do projeto e reconstruir documentalmente sua evolução desde a pesquisa histórica até a solução moderna validada.

## 29. PRÓXIMA ETAPA

Após a auditoria, executar **Etapa 16 — Pacote de Reprodução Independente e Demonstração Pública**, caso os critérios de release sejam atendidos. Essa etapa deverá transformar a versão liberada em um pacote independente para reprodução por terceiro e apresentação técnica controlada.
