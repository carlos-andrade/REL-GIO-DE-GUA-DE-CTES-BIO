# CARTA REGENTE DO PROJETO — V1

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO
**Repositório oficial:** carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO
**Branch de referência:** main
**Data de vigência:** 27/09/2026
**Status:** CARTA REGENTE / NORMA SUPERIOR DE GOVERNANÇA DO PROJETO

## 1. Finalidade

Esta Carta Regente estabelece as regras superiores para preservar a integridade documental, técnica, histórica, experimental, computacional e de engenharia do projeto RELÓGIO DE ÁGUA DE CTESÍBIO.

Ela rege as demais cartas, regras, procedimentos, etapas de engenharia, pesquisas, dados, protótipos, testes, relatórios e releases do projeto.

## 2. Fonte oficial de verdade

O repositório GitHub oficial é a fonte de verdade documental e versionada do projeto.

O chat é ambiente de trabalho, decisão, execução e confirmação operacional. Conteúdo relevante para a continuidade do projeto não pode permanecer exclusivamente no chat.

Em caso de conflito entre memória informal, conversa e documento versionado, prevalece o documento versionado mais recente e aplicável, salvo decisão formal registrada no repositório.

## 3. Identidade oficial

O nome oficial do repositório é:

`carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO`

Referências futuras devem utilizar exclusivamente essa identificação. O nome histórico anterior não deve ser utilizado como referência operacional.

## 4. Hierarquia documental

A governança segue esta ordem:

1. Carta Regente do Projeto;
2. cartas e regras permanentes de GOVERNANCA/;
3. requisitos, especificações e decisões versionadas;
4. etapas de engenharia;
5. procedimentos de pesquisa, coleta, teste, calibração e validação;
6. dados brutos e evidências;
7. relatórios e sínteses;
8. manifestos e releases.

Nenhum documento subordinado pode contradizer esta Carta sem que a Carta ou a regra superior seja formalmente revisada.

## 5. Regra GitHub-first

Todo artefato reutilizável produzido para o projeto deve ser salvo no repositório antes de ser considerado concluído.

Fluxo obrigatório:

`PRODUZIR → REVISAR → CLASSIFICAR → SALVAR → COMMITAR → VERIFICAR → CONFIRMAR`

## 6. Caminho e commit obrigatórios

Toda alteração relevante deve permitir identificar:

- repositório;
- caminho completo;
- nome do arquivo;
- versão;
- data;
- status;
- commit SHA.

A confirmação no chat deve informar pelo menos o caminho e o commit.

## 7. Integridade e preservação

Não apagar ou substituir histórico técnico relevante sem justificativa documental.

Quando uma alteração modificar uma decisão, requisito, método ou resultado relevante, registrar a evolução por nova versão ou histórico de alteração.

Nenhum dado experimental deve ser alterado para melhorar resultados, aparência ou conformidade.

## 8. Separação de evidências

O projeto deve manter separadas, de forma explícita:

- evidência histórica;
- interpretação histórica;
- reconstrução moderna;
- proposta de engenharia;
- hipótese;
- dado experimental;
- resultado validado;
- informação ainda não determinada.

Uma reconstrução moderna nunca deve ser apresentada como fato histórico sem evidência suficiente.

## 9. Dados experimentais

Dados brutos devem ser preservados antes de qualquer tratamento.

Sempre que aplicável, registrar:

- identificação do protótipo;
- configuração;
- instrumento;
- unidade;
- timestamp;
- operador ou processo de aquisição;
- condições ambientais;
- parâmetros do teste;
- versão do software/firmware;
- qualidade do dado;
- método de processamento.

Resultados calculados devem permanecer rastreáveis aos dados brutos.

## 10. Metrologia e validação

Nenhuma precisão, tolerância, calibração, repetibilidade ou desempenho pode ser declarado como resultado medido antes da execução do teste correspondente.

Critérios de aceitação devem ser definidos antes do teste sempre que possível.

Planejamento, especificação e resultado medido devem ser claramente diferenciados.

## 11. Pesquisa histórica

Fontes devem ser classificadas e rastreadas.

A cadeia mínima é:

`FONTE → EVIDÊNCIA → AFIRMAÇÃO → INTERPRETAÇÃO → RECONSTRUÇÃO → REQUISITO`

Contradições entre fontes devem ser registradas, não ocultadas.

## 12. Engenharia

A engenharia deve preservar a sequência das etapas 01–18 e seus vínculos de dependência.

A cadeia geral é:

`FUNDAMENTAÇÃO → PESQUISA → EVIDÊNCIA → SÍNTESE → MODELO → ARQUITETURA → FABRICAÇÃO → CALIBRAÇÃO → COMPENSAÇÃO → CICLO → INTEGRAÇÃO → ROBUSTEZ → VALIDAÇÃO → DOSSIÊ → AUDITORIA → REPRODUÇÃO → PUBLICAÇÃO → ENCERRAMENTO`

## 13. Controle de configuração

Toda configuração física, hidráulica, mecânica, elétrica, eletrônica, computacional ou de modelo que produza dados deve possuir identificação versionada.

Alterações que possam afetar resultados exigem nova avaliação de impacto e, quando aplicável, nova calibração ou validação.

## 14. Auditabilidade

O projeto deve permitir reconstruir:

`REQUISITO → PROJETO → IMPLEMENTAÇÃO → TESTE → DADO → ANÁLISE → RESULTADO → DECISÃO`

Para afirmações históricas:

`FONTE → EVIDÊNCIA → INTERPRETAÇÃO → RECONSTRUÇÃO → DECISÃO DE PROJETO`

## 15. Automação e workflows

Workflows automatizados são auxiliares de execução e nunca substituem a validação humana ou documental quando esta for exigida.

Uma coleta automática é evidência de descoberta até que a fonte seja documentalmente validada.

Falhas de automação devem ser registradas e não mascaradas.

## 16. Segurança

Segurança física, hidráulica, elétrica e operacional tem prioridade sobre continuidade de teste, produção de dados ou demonstração.

Em conflito entre objetivos, a ordem de autoridade é:

`SEGURANÇA → INTEGRIDADE DO SISTEMA → INTEGRIDADE DO DADO → VALIDAÇÃO → DESEMPENHO → DEMONSTRAÇÃO`

## 17. Proibição de fabricação de evidência

É proibido inventar, completar, alterar ou inferir como medido qualquer valor que não tenha sido efetivamente observado, registrado ou suportado por fonte identificável.

Estimativas devem ser identificadas como estimativas.

## 18. Controle de mudanças

Toda mudança relevante deve responder, quando aplicável:

- o que mudou;
- por que mudou;
- qual requisito é afetado;
- quais documentos são afetados;
- quais testes precisam ser repetidos;
- qual configuração passa a ser válida;
- qual commit registra a mudança.

## 19. Estado oficial do projeto

Os estados permitidos são:

`EM DESENVOLVIMENTO → EM VALIDAÇÃO → AUDITADO → LIBERADO → PUBLICADO → ARQUIVADO`

Nenhum estado posterior deve ser declarado sem cumprir seus critérios documentais.

## 20. Regra de continuidade entre chats

Ao iniciar ou retomar trabalho em novo chat:

1. consultar o repositório;
2. identificar o estado vigente;
3. localizar a etapa ou documento aplicável;
4. continuar a partir da versão registrada;
5. salvar novas entregas no repositório;
6. confirmar caminho e commit.

## 21. Integridade após renomeação

A alteração do nome do repositório não deve alterar a identidade, o histórico ou o conteúdo técnico do projeto.

Qualquer futura alteração de nome, organização ou migração exige auditoria específica de referências, workflows, links, documentação e automações.

## 22. Regra de precedência

Esta Carta prevalece sobre regras operacionais incompatíveis ou desatualizadas. Regras subordinadas devem ser mantidas compatíveis com ela.

## 23. Revisão da Carta Regente

Esta Carta somente deve ser alterada mediante nova versão formal, com justificativa e commit registrado.

Versões anteriores devem permanecer no histórico Git.

## 24. Princípio permanente

> **O projeto trabalha no chat, preserva no GitHub, mede no experimento, comprova nos dados e libera somente aquilo que pode ser auditado.**
