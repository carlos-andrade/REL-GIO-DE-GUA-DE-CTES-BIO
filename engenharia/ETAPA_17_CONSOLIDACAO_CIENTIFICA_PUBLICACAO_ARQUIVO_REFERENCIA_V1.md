# ETAPA 17 — CONSOLIDAÇÃO CIENTÍFICA, PUBLICAÇÃO TÉCNICA E ARQUIVO DE REFERÊNCIA

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Caminho:** engenharia/ETAPA_17_CONSOLIDACAO_CIENTIFICA_PUBLICACAO_ARQUIVO_REFERENCIA_V1.md  
**Versão:** V1  
**Etapa:** 17  
**Data de criação:** 27/09/2026

---

## 1. OBJETIVO

Consolidar os resultados históricos, científicos, experimentais e de engenharia em uma estrutura final de publicação e preservação de longo prazo.

A Etapa 17 não altera a configuração técnica liberada. Seu objetivo é transformar o conjunto documental em um **arquivo de referência controlado, citável, reproduzível e preservável**.

## 2. PRINCÍPIO DE CONSOLIDAÇÃO

A documentação final deverá preservar a cadeia:

**FONTE → EVIDÊNCIA → AFIRMAÇÃO → INTERPRETAÇÃO → RECONSTRUÇÃO → REQUISITO → PROJETO → IMPLEMENTAÇÃO → TESTE → RESULTADO**

Nenhuma afirmação histórica deverá perder sua origem durante a consolidação editorial.

## 3. ESTRUTURA DA PUBLICAÇÃO TÉCNICA

A publicação principal deverá possuir, no mínimo:

1. resumo;
2. contexto histórico;
3. problema hidráulico;
4. princípio de funcionamento;
5. evidências documentais;
6. análise das fontes;
7. reconstrução proposta;
8. arquitetura moderna;
9. modelo matemático;
10. protótipo;
11. calibração;
12. compensação sazonal;
13. ciclo automático;
14. aquisição e auditabilidade;
15. testes de robustez;
16. validação final;
17. limitações;
18. reprodução independente;
19. conclusão técnica;
20. referências.

## 4. RESUMO EXECUTIVO

O resumo deverá responder objetivamente:

- qual problema histórico foi estudado;
- qual princípio hidráulico foi preservado;
- quais elementos são sustentados por evidência;
- quais elementos são reconstruções;
- quais soluções são modernas;
- como o sistema foi validado;
- quais limitações permanecem.

O resumo não deverá apresentar uma reconstrução moderna como se fosse uma descrição integral do mecanismo antigo.

## 5. CLASSIFICAÇÃO DAS AFIRMAÇÕES

Cada afirmação relevante deverá receber uma das classificações:

- **HISTÓRICO** — sustentado diretamente por fonte histórica adequada;
- **INTERPRETAÇÃO** — leitura técnica de uma evidência;
- **RECONSTRUÇÃO** — solução plausível necessária para representar o mecanismo;
- **PROPOSTA MODERNA** — solução desenvolvida para o protótipo contemporâneo;
- **HIPÓTESE** — proposição ainda não suficientemente demonstrada;
- **NÃO DETERMINADO** — informação que as evidências disponíveis não permitem estabelecer.

## 6. MATRIZ DE EVIDÊNCIAS

Criar uma matriz final:

| ID | Afirmação | Classificação | Fonte | Evidência | Confiança | Documento relacionado |
|---|---|---|---|---|---|---|
| E01 | registrar | registrar | registrar | registrar | registrar | registrar |

Nenhuma afirmação histórica crítica deverá permanecer sem referência identificável.

## 7. CONTROLE DAS FONTES

Para cada fonte relevante registrar:

- identificador persistente;
- título;
- autor;
- instituição;
- data;
- idioma;
- tipo documental;
- URL ou identificador bibliográfico;
- data de acesso;
- classe de evidência;
- relação com a afirmação;
- versão ou edição consultada;
- observações sobre tradução.

Quando houver traduções divergentes, conservar a referência ao texto ou edição utilizada.

## 8. CONTRADIÇÕES E INCERTEZAS

Contradições não deverão ser eliminadas por edição.

Registrar:

- afirmação A;
- afirmação B;
- fontes correspondentes;
- natureza da divergência;
- evidência disponível;
- interpretação adotada;
- impacto sobre a reconstrução;
- decisão de projeto;
- grau de incerteza.

Quando a evidência não permitir decisão, utilizar **NÃO DETERMINADO**.

## 9. DOCUMENTO DE RECONSTRUÇÃO

A reconstrução deverá ser publicada separadamente da narrativa histórica.

Deverá conter:

- requisitos derivados das fontes;
- elementos inferidos;
- elementos desconhecidos;
- hipóteses geométricas;
- hipóteses hidráulicas;
- hipóteses mecânicas;
- alternativas consideradas;
- critérios para seleção;
- limitações da reconstrução.

## 10. DOCUMENTO DE ENGENHARIA MODERNA

A solução contemporânea deverá ser apresentada como sistema de engenharia independente, ainda que inspirado no princípio histórico.

Registrar:

- requisitos;
- arquitetura;
- componentes;
- materiais;
- instrumentação;
- controle;
- software/firmware;
- calibração;
- segurança;
- manutenção;
- desempenho;
- tolerâncias;
- resultados experimentais.

## 11. PACOTE DE PUBLICAÇÃO

Estrutura recomendada:

- `publicacao/README.md`
- `publicacao/resumo/`
- `publicacao/artigo/`
- `publicacao/figuras/`
- `publicacao/tabelas/`
- `publicacao/metodologia/`
- `publicacao/resultados/`
- `publicacao/referencias/`
- `publicacao/suplementos/`
- `publicacao/dados/`
- `publicacao/reproducao/`
- `publicacao/versoes/`

## 12. DADOS SUPLEMENTARES

Sempre que possível, preservar:

- dados brutos;
- dados processados;
- scripts de análise;
- parâmetros;
- configurações;
- resultados intermediários;
- gráficos;
- tabelas;
- logs;
- relatórios de validação.

O dado processado deverá permanecer ligado ao dado bruto por identificador ou hash.

## 13. ARQUIVO DE REFERÊNCIA

Criar um manifesto que identifique a configuração oficial:

- `PROJECT-ID`;
- `CONFIG-ID`;
- versão;
- commit SHA;
- data de liberação;
- BOM;
- desenhos;
- firmware/software;
- modelo sazonal;
- calibração;
- relatório de validação;
- relatório de auditoria;
- pacote de reprodução.

## 14. INTEGRIDADE DIGITAL

Para arquivos críticos registrar hashes criptográficos, preferencialmente SHA-256.

A verificação deverá permitir detectar:

- alteração de conteúdo;
- substituição de arquivo;
- corrupção;
- divergência entre pacote publicado e pacote arquivado.

## 15. VERSIONAMENTO

Usar versionamento explícito para:

- documentação;
- hardware;
- desenhos;
- firmware;
- software;
- modelo matemático;
- modelo sazonal;
- calibração;
- conjunto de dados;
- publicação.

Uma alteração técnica que possa modificar resultados deverá gerar nova configuração identificável.

## 16. POLÍTICA DE PUBLICAÇÃO

Antes da publicação, verificar:

- precisão das citações;
- consistência das unidades;
- coerência entre texto e dados;
- coerência entre gráficos e dados;
- identificação das incertezas;
- distinção entre fato e interpretação;
- reprodução das análises;
- controle de versões;
- integridade dos arquivos.

## 17. PUBLICAÇÃO HISTÓRICA

A parte histórica deverá evitar afirmações que excedam as evidências disponíveis.

Quando uma característica do mecanismo antigo não puder ser determinada, declarar explicitamente essa limitação em vez de preencher a lacuna com uma solução moderna.

## 18. PUBLICAÇÃO EXPERIMENTAL

Os resultados experimentais deverão indicar:

- equipamento utilizado;
- configuração;
- condições ambientais;
- procedimento;
- referência;
- número de repetições;
- resultados;
- incerteza;
- critérios de aceitação;
- anomalias;
- exclusões justificadas.

Dados removidos ou excluídos deverão permanecer rastreáveis.

## 19. REPRODUCIBILIDADE DA ANÁLISE

Um terceiro deverá conseguir reconstruir os resultados a partir de:

**DADOS BRUTOS + CONFIGURAÇÃO + MÉTODO + PARÂMETROS + SOFTWARE/SCRIPT + VERSÃO**

Se isso não for possível, o resultado deverá ser marcado como não plenamente reproduzível.

## 20. ARQUIVAMENTO DE LONGO PRAZO

Manter pelo menos três classes de preservação:

### A — Fonte de trabalho

Repositório Git e histórico de commits.

### B — Pacote de release

Conjunto fechado correspondente à configuração liberada.

### C — Cópia de preservação

Cópia independente do pacote final, com manifesto e hashes.

A cópia de preservação deverá ser periodicamente verificada.

## 21. IDENTIDADE DA CONFIGURAÇÃO OFICIAL

A configuração oficial será identificada por:

**PROJECT-ID + CONFIG-ID + RELEASE-VERSION + COMMIT-SHA**

Nenhuma cópia derivada deverá ser chamada de configuração oficial sem correspondência documental.

## 22. PUBLICAÇÃO E REPOSITÓRIO

O repositório deverá permanecer como fonte primária do histórico de desenvolvimento.

Uma publicação externa deverá apontar para a versão específica do repositório, e não apenas para a página principal, sempre que tecnicamente possível.

## 23. PACOTE DE CITAÇÃO

Preparar metadados para futura citação científica ou técnica:

- título;
- autor;
- projeto;
- versão;
- data;
- descrição;
- palavras-chave;
- identificador persistente, quando disponível;
- licença, quando definida;
- referência ao commit.

## 24. CHECKLIST FINAL DE PUBLICAÇÃO

- [ ] evidências históricas rastreadas;
- [ ] reconstruções identificadas;
- [ ] soluções modernas identificadas;
- [ ] fontes normalizadas;
- [ ] contradições documentadas;
- [ ] dados brutos preservados;
- [ ] análise reproduzível;
- [ ] resultados validados;
- [ ] configuração congelada;
- [ ] hashes gerados;
- [ ] manifesto criado;
- [ ] pacote de reprodução fechado;
- [ ] limitações publicadas;
- [ ] revisão técnica concluída;
- [ ] revisão editorial concluída;
- [ ] arquivo de preservação criado.

## 25. CRITÉRIOS DE BLOQUEIO

A publicação final deverá ser bloqueada se houver:

- fonte crítica sem identificação;
- resultado sem rastreabilidade;
- dado essencial ausente;
- inconsistência entre configuração e publicação;
- versão ambígua;
- erro material conhecido não corrigido;
- reconstrução apresentada como fato histórico;
- análise não reproduzível quando declarada reproduzível;
- pacote de release sem integridade verificável.

## 26. ENCERRAMENTO DOCUMENTAL

O projeto somente deverá ser considerado documentalmente consolidado quando existir uma cadeia verificável:

**HISTÓRIA → PESQUISA → SÍNTESE → MODELO → PROTÓTIPO → CALIBRAÇÃO → VALIDAÇÃO → AUDITORIA → REPRODUÇÃO → PUBLICAÇÃO → PRESERVAÇÃO**

## 27. ESTADO FINAL DOCUMENTAL

Estados previstos:

`EM DESENVOLVIMENTO → EM VALIDAÇÃO → AUDITADO → LIBERADO → PUBLICADO → ARQUIVADO`

Uma nova alteração técnica deverá retirar a configuração afetada do estado `ARQUIVADO` e gerar nova versão controlada.

## 28. RESULTADO ESPERADO

Ao final desta etapa deverá existir uma base documental capaz de sustentar:

- consulta histórica;
- análise científica;
- reprodução experimental;
- auditoria técnica;
- publicação;
- preservação de longo prazo;
- evolução futura sem perda do histórico.

## 29. PRÓXIMA ETAPA

**Etapa 18 — Encerramento Formal, Manifesto da Configuração Oficial e Plano de Evolução**, destinada a consolidar o estado final do projeto, registrar a configuração oficial e estabelecer o mecanismo controlado para futuras versões.
