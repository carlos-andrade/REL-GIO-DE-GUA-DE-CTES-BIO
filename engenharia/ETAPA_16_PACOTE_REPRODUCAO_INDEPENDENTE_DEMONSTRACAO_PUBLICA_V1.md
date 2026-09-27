# ETAPA 16 — PACOTE DE REPRODUÇÃO INDEPENDENTE E DEMONSTRAÇÃO PÚBLICA

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Caminho:** engenharia/ETAPA_16_PACOTE_REPRODUCAO_INDEPENDENTE_DEMONSTRACAO_PUBLICA_V1.md  
**Versão:** V1  
**Etapa:** 16  
**Status:** Especificação para reprodução independente e demonstração  
**Data de criação:** 27/09/2026

---

## 1. OBJETIVO

Transformar a configuração auditada e liberada em um pacote independente capaz de permitir que um terceiro autorizado compreenda, fabrique, monte, calibre, opere e teste uma réplica sem depender de conhecimento informal da equipe original.

A demonstração pública deverá comunicar claramente três camadas distintas:

1. o que é historicamente documentado;
2. o que é reconstrução técnica;
3. o que é engenharia moderna desenvolvida para o projeto.

## 2. CONDIÇÃO DE ENTRADA

A Etapa 16 somente poderá ser executada sobre uma versão que tenha passado pelos critérios de release da Etapa 15.

A versão de entrada deverá possuir:

- CONFIG-ID;
- commit SHA;
- BOM controlada;
- desenhos controlados;
- calibração válida;
- resultados de validação;
- documentação de segurança;
- dados preservados;
- limitações conhecidas.

## 3. PRINCÍPIO DE INDEPENDÊNCIA

O pacote de reprodução deverá permitir que um terceiro responda, utilizando exclusivamente a documentação oficial:

- o que fabricar;
- o que comprar;
- como fabricar;
- como montar;
- como conectar;
- como configurar;
- como calibrar;
- como operar;
- como testar;
- como interpretar os resultados;
- quais diferenças devem ser registradas.

Qualquer dependência de instrução oral deverá ser registrada como lacuna documental.

## 4. ESTRUTURA DO PACOTE DE REPRODUÇÃO

Estrutura mínima:

- 01_LEIA_PRIMEIRO/
- 02_REQUISITOS/
- 03_HISTORIA_EVIDENCIAS/
- 04_RECONSTRUCAO/
- 05_ARQUITETURA/
- 06_BOM/
- 07_DESENHOS/
- 08_FABRICACAO/
- 09_MONTAGEM/
- 10_COMISSIONAMENTO/
- 11_INSTRUMENTACAO/
- 12_CALIBRACAO/
- 13_OPERACAO/
- 14_MANUTENCAO/
- 15_TESTES/
- 16_DADOS_E_FORMATOS/
- 17_SOFTWARE_FIRMWARE/
- 18_SEGURANCA/
- 19_VALIDACAO/
- 20_MANIFESTO/

## 5. ARQUIVO LEIA PRIMEIRO

O documento inicial deverá apresentar:

- identificação do projeto;
- finalidade;
- versão;
- CONFIG-ID;
- commit de referência;
- requisitos de segurança;
- sequência recomendada de leitura;
- materiais necessários;
- competências técnicas recomendadas;
- limitações;
- advertência sobre a diferença entre história e reconstrução.

## 6. CHECKLIST DE MATERIAIS

Criar uma lista operacional dividida em:

### Componentes comerciais

- reservatórios;
- tubos;
- válvulas;
- sensores;
- conectores;
- fonte de alimentação;
- sistema de aquisição;
- referência temporal.

### Componentes fabricados

- flutuador;
- guias;
- suportes;
- polias;
- engrenagens;
- escala;
- mecanismos de acionamento;
- estrutura.

### Ferramentas

- instrumentos dimensionais;
- ferramentas de montagem;
- instrumentos elétricos;
- equipamentos de teste;
- equipamentos de segurança.

Cada item deverá possuir quantidade e especificação suficiente para reprodução.

## 7. GUIA DE FABRICAÇÃO

A documentação deverá indicar:

1. sequência de fabricação;
2. matéria-prima;
3. dimensões;
4. tolerâncias;
5. acabamento;
6. inspeções intermediárias;
7. identificação da peça;
8. critérios de rejeição;
9. armazenamento.

Peças críticas deverão possuir inspeção dimensional documentada.

## 8. GUIA DE MONTAGEM

A montagem deverá seguir uma sequência controlada:

**ESTRUTURA → RESERVATÓRIOS → HIDRÁULICA → GUIAS → FLUTUADOR → TRANSMISSÃO → DESCARGA → INSTRUMENTAÇÃO → AQUISIÇÃO → PROTEÇÕES**

Cada etapa deverá possuir checklist de montagem e ponto de inspeção.

## 9. COMISSIONAMENTO DA RÉPLICA

A réplica deverá passar por:

1. inspeção visual;
2. inspeção dimensional;
3. teste de estanqueidade;
4. teste de alimentação;
5. teste de nível;
6. teste do flutuador;
7. teste de transmissão;
8. teste de descarga;
9. teste de reset;
10. teste de sensores;
11. sincronização temporal;
12. aquisição de dados;
13. calibração;
14. ciclo completo.

Nenhuma etapa posterior deve mascarar falha de uma etapa anterior.

## 10. CALIBRAÇÃO DA RÉPLICA

A réplica deverá ser calibrada independentemente do protótipo de referência.

Registrar:

- identificador da réplica;
- configuração;
- instrumentos;
- referência temporal;
- pontos;
- repetições;
- resultados;
- incerteza;
- data;
- responsável.

A calibração não deve copiar automaticamente coeficientes do protótipo original sem demonstração de equivalência.

## 11. TESTE DE EQUIVALÊNCIA

Comparar protótipo e réplica em condições equivalentes:

| Parâmetro | Referência | Réplica | Diferença | Critério | Status |
|---|---:|---:|---:|---:|---|
| nível | registrar | registrar | calcular | definido | — |
| vazão | registrar | registrar | calcular | definido | — |
| tempo de ciclo | registrar | registrar | calcular | definido | — |
| descarga | registrar | registrar | calcular | definido | — |
| reset | registrar | registrar | calcular | definido | — |
| indicação | registrar | registrar | calcular | definido | — |
| erro | registrar | registrar | calcular | definido | — |
| repetibilidade | registrar | registrar | calcular | definido | — |

A equivalência deverá ser baseada em critérios quantitativos previamente definidos.

## 12. CLASSIFICAÇÃO DE DESVIOS DA RÉPLICA

Cada diferença deverá ser classificada como:

- D1 — dimensional;
- D2 — material;
- D3 — hidráulica;
- D4 — mecânica;
- D5 — instrumental;
- D6 — software/firmware;
- D7 — calibração;
- D8 — operacional.

Para cada desvio registrar causa, impacto, correção e novo teste necessário.

## 13. PACOTE DE DADOS DE DEMONSTRAÇÃO

A demonstração deverá utilizar dados reais do sistema ou dados sintéticos explicitamente identificados como sintéticos.

O pacote deverá conter:

- dados brutos;
- dados processados;
- configuração;
- unidades;
- descrição dos sinais;
- eventos;
- referência temporal;
- resultado;
- procedimento de reprodução da análise.

## 14. DEMONSTRAÇÃO PÚBLICA

A demonstração deverá mostrar visualmente, de forma controlada:

1. reservatório de alimentação;
2. controle de nível;
3. flutuador;
4. indicação;
5. escala;
6. descarga;
7. reset;
8. aquisição de dados;
9. referência temporal;
10. ciclo completo.

A apresentação deverá explicar o princípio físico antes de apresentar resultados.

## 15. ROTEIRO DA DEMONSTRAÇÃO

### Abertura

Identificar Ctesíbio, o contexto histórico e o objetivo do projeto moderno.

### Princípio hidráulico

Mostrar por que a queda de pressão altera a vazão e como o controle de nível reduz essa fonte de erro.

### Medição

Demonstrar a relação entre nível, flutuador, transmissão e indicação.

### Ciclo automático

Demonstrar limite, descarga, reset e reinicialização.

### Compensação sazonal

Explicar que a adaptação temporal é uma camada separada do controle hidráulico.

### Auditoria

Mostrar como um ciclo pode ser reconstruído a partir dos dados registrados.

### Limitações

Apresentar explicitamente o que é documentado historicamente e o que é reconstrução ou engenharia moderna.

## 16. MATERIAL VISUAL

O pacote público poderá conter:

- fotografias;
- diagramas;
- desenhos simplificados;
- vídeos;
- gráficos;
- animações;
- sequência de estados;
- comparação histórica/moderna.

Todo material deverá possuir identificação de versão e origem.

## 17. DIAGRAMA PÚBLICO DE FUNCIONAMENTO

Representação mínima:

**ALIMENTAÇÃO → REGULAÇÃO → NÍVEL CONSTANTE → FLUTUADOR → INDICAÇÃO → REGISTRO**

Em paralelo:

**REFERÊNCIA TEMPORAL → COMPENSAÇÃO SAZONAL → ESCALA/ATUADOR**

No ciclo:

**LIMITE → DESCARGA → RESET → VERIFICAÇÃO → NOVO CICLO**

## 18. SEGURANÇA DA DEMONSTRAÇÃO

A demonstração pública deverá utilizar:

- contenção secundária;
- proteção de partes móveis;
- proteção elétrica;
- drenagem controlada;
- sinalização de risco;
- procedimento de parada;
- supervisão durante operação;
- plano de resposta a vazamento ou falha.

Não realizar demonstração pública com configuração experimental não caracterizada sem identificação explícita de seu status.

## 19. CONTROLE DE COMUNICAÇÃO TÉCNICA

Todo material público deverá distinguir claramente:

**FATO HISTÓRICO**

**RECONSTRUÇÃO**

**SOLUÇÃO MODERNA**

**RESULTADO EXPERIMENTAL**

**HIPÓTESE**

Essa distinção é obrigatória em textos, legendas, vídeos e apresentações.

## 20. MANIFESTO DO PACOTE

O pacote deverá conter:

- nome do projeto;
- versão;
- CONFIG-ID;
- commit SHA;
- data;
- lista de arquivos;
- hashes;
- limitações;
- status de reprodução;
- status de demonstração;
- responsável pela publicação.

## 21. CRITÉRIOS DE ACEITAÇÃO

O pacote será considerado pronto quando:

- um terceiro conseguir identificar os componentes;
- a montagem puder ser executada sem instrução oral essencial;
- a calibração puder ser reproduzida;
- os testes puderem ser executados;
- os dados puderem ser interpretados;
- os resultados puderem ser auditados;
- diferenças da réplica puderem ser quantificadas;
- o material público distinguir história e engenharia moderna;
- a demonstração puder ser executada com segurança.

## 22. CRITÉRIOS DE BLOQUEIO

Bloquear a publicação/reprodução quando houver:

- instrução crítica ausente;
- componente crítico sem especificação;
- desenho inconsistente;
- configuração desconhecida;
- calibração inválida;
- teste crítico ausente;
- risco público não controlado;
- dado apresentado como real quando é sintético;
- reconstrução apresentada como fato histórico;
- versão do pacote não identificada.

## 23. RESULTADO ESPERADO

Ao final da Etapa 16 deverá existir um pacote que permita:

**REPRODUZIR → CALIBRAR → TESTAR → COMPARAR → AUDITAR → DEMONSTRAR**

sem dependência de conhecimento informal e sem confusão entre evidência histórica, reconstrução e solução moderna.

## 24. PRÓXIMA ETAPA

**Etapa 17 — Consolidação Científica, Publicação Técnica e Arquivo de Referência**, destinada a organizar a documentação final para publicação, preservação de longo prazo, indexação e futura evolução do projeto.
