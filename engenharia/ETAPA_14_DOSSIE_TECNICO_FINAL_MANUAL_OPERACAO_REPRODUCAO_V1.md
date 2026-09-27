# ETAPA 14 — DOSSIÊ TÉCNICO FINAL, MANUAL DE OPERAÇÃO E PLANO DE REPRODUÇÃO

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Caminho:** engenharia/ETAPA_14_DOSSIE_TECNICO_FINAL_MANUAL_OPERACAO_REPRODUCAO_V1.md  
**Versão:** V1  
**Etapa:** 14  
**Status:** Especificação para consolidação e reprodução  
**Data de criação:** 27/09/2026

---

## 1. OBJETIVO

Consolidar todas as etapas anteriores em um pacote técnico único, reproduzível, auditável e operacionalmente utilizável por terceiros autorizados.

A Etapa 14 não substitui a validação metrológica. Ela transforma os resultados validados em documentação controlada para fabricação, montagem, operação, calibração, manutenção, reprodução e publicação.

## 2. PACOTE TÉCNICO OFICIAL

O pacote final deverá conter:

- especificação funcional;
- arquitetura física;
- diagramas;
- BOM final;
- desenhos e tolerâncias;
- instruções de fabricação;
- instruções de montagem;
- manual de operação;
- procedimento de calibração;
- plano de manutenção;
- plano de segurança;
- protocolo de testes;
- formato de dados;
- manifesto de configuração;
- histórico de versões;
- matriz de rastreabilidade;
- plano de reprodução;
- documentação histórica e reconstrutiva.

## 3. HIERARQUIA DOCUMENTAL

A documentação deverá seguir:

**Governança → Requisitos → Arquitetura → Projeto detalhado → Fabricação → Montagem → Calibração → Validação → Operação → Manutenção → Reprodução → Publicação**

Nenhum documento derivado poderá contradizer um documento superior sem registro formal de alteração.

## 4. BOM FINAL

A BOM final deverá registrar, no mínimo:

- ID do componente;
- descrição;
- quantidade;
- material;
- especificação;
- fornecedor ou origem;
- componente comercial/customizado;
- desenho associado;
- revisão;
- tolerância crítica;
- função;
- criticidade;
- substitutos permitidos;
- condição de inspeção.

Componentes críticos deverão possuir identificação inequívoca.

## 5. DESENHOS E FABRICAÇÃO

Cada componente customizado deverá possuir desenho controlado contendo:

- vistas necessárias;
- dimensões;
- tolerâncias;
- material;
- acabamento;
- furos e roscas;
- referência de montagem;
- revisão;
- identificação do desenho.

Nenhuma dimensão crítica deverá permanecer apenas em descrição textual quando for necessária à reprodução.

## 6. MANUAL DE OPERAÇÃO

O manual deverá conter:

### 6.1 Antes da operação

- inspeção visual;
- verificação de vazamentos;
- verificação do reservatório;
- verificação do flutuador;
- verificação da descarga;
- verificação dos sensores;
- verificação da alimentação;
- confirmação da configuração;
- confirmação da calibração vigente.

### 6.2 Inicialização

1. instalar o protótipo em superfície nivelada;
2. confirmar contenção e drenagem;
3. iniciar aquisição;
4. registrar prototype_id e configuração;
5. iniciar alimentação hidráulica;
6. aguardar estabilização;
7. confirmar estado PRONTO.

### 6.3 Operação

Registrar continuamente as variáveis definidas na Etapa 11. Não alterar componentes, parâmetros ou conexões durante uma campanha sem registrar a mudança.

### 6.4 Encerramento

- interromper alimentação;
- concluir ciclo seguro quando aplicável;
- registrar estado final;
- drenar quando necessário;
- executar inspeção;
- preservar dados;
- registrar anomalias.

## 7. MANUAL DE CALIBRAÇÃO

O procedimento deverá especificar:

- referência utilizada;
- condições ambientais;
- configuração;
- pontos de calibração;
- sequência;
- número de repetições;
- cálculo;
- critérios de aceitação;
- incerteza;
- identificação do certificado/registro;
- data de validade;
- responsável.

A calibração não poderá alterar parâmetros sem gerar nova versão da configuração.

## 8. PLANO DE MANUTENÇÃO

### Antes de cada campanha

Inspecionar reservatório, tubos, conexões, flutuador, guia, transmissão, descarga, sensores e contenção.

### Após cada campanha

Limpar componentes aplicáveis, verificar depósitos, secar áreas críticas, registrar desgaste e preservar os dados.

### Manutenção periódica

Verificar folgas, alinhamento, vedação, tubos, mecanismo de descarga, sensores, cabos, conectores, estrutura e referência de calibração.

### Manutenção extraordinária

Qualquer substituição de componente crítico deverá gerar inspeção, recalibração quando aplicável e registro de nova configuração.

## 9. PLANO DE REPRODUÇÃO

Um terceiro autorizado deverá conseguir reproduzir o sistema usando apenas o pacote oficial e os materiais especificados.

A reprodução deverá seguir:

**BOM → desenhos → fabricação → inspeção → montagem → comissionamento → calibração → validação → liberação**

Diferenças entre protótipo original e réplica deverão ser registradas como desvios de reprodução.

## 10. CRITÉRIOS DE EQUIVALÊNCIA DA RÉPLICA

A réplica deverá ser comparada ao protótipo de referência quanto a:

- geometria crítica;
- materiais críticos;
- volumes;
- vazões;
- níveis;
- transmissão;
- descarga;
- tempos de ciclo;
- indicação;
- erro de medição;
- repetibilidade;
- comportamento de segurança.

Uma réplica não será considerada equivalente apenas por aparência física.

## 11. CONTROLE DE CONFIGURAÇÃO

Toda unidade deverá possuir:

- prototype_id;
- serial ou identificador único;
- revisão mecânica;
- revisão hidráulica;
- revisão elétrica;
- firmware;
- software;
- modelo sazonal;
- calibração;
- documentação.

Qualquer mudança deverá gerar registro de alteração e avaliação de impacto.

## 12. MANIFESTO DE RELEASE

Cada versão oficial deverá registrar:

- versão;
- data;
- commit;
- arquivos incluídos;
- alterações;
- testes executados;
- calibração;
- limitações conhecidas;
- responsáveis;
- status de liberação.

## 13. PLANO DE PRESERVAÇÃO

Manter pelo menos:

- dados brutos;
- dados processados;
- relatórios;
- configurações;
- firmware/software;
- desenhos;
- BOM;
- certificados;
- registros de manutenção;
- registros de falhas;
- evidências históricas;
- hashes dos arquivos críticos.

Não substituir dados brutos por dados processados.

## 14. PUBLICAÇÃO TÉCNICA

O pacote de publicação deverá separar explicitamente:

1. história documentada;
2. interpretação;
3. reconstrução;
4. projeto moderno;
5. resultados experimentais;
6. limitações.

O material publicado não deverá apresentar hipóteses de reconstrução como fatos históricos.

## 15. CRITÉRIOS DE REPRODUTIBILIDADE

Um terceiro deverá conseguir:

- identificar a versão exata;
- obter os materiais;
- fabricar os componentes;
- montar o sistema;
- configurar a instrumentação;
- calibrar;
- executar os testes;
- obter dados comparáveis;
- reconstruir os cálculos;
- identificar diferenças.

## 16. PROCEDIMENTO DE LIBERAÇÃO FINAL

A liberação deverá seguir:

1. auditoria documental;
2. conferência da BOM;
3. conferência dos desenhos;
4. conferência dos procedimentos;
5. conferência da calibração;
6. conferência dos testes;
7. conferência dos dados;
8. conferência das limitações;
9. congelamento da versão;
10. criação do manifesto;
11. publicação do pacote.

## 17. CRITÉRIOS DE BLOQUEIO

Não liberar a documentação quando houver:

- desenho crítico ausente;
- componente crítico sem especificação;
- procedimento não reproduzível;
- calibração vencida ou ausente;
- configuração inconsistente;
- dados essenciais ausentes;
- teste crítico sem evidência;
- divergência não registrada;
- falha de segurança conhecida sem controle;
- alteração sem versionamento.

## 18. ESTRUTURA FINAL SUGERIDA

- 01_governanca/
- 02_requisitos/
- 03_historia/
- 04_reconstrucao/
- 05_arquitetura/
- 06_desenhos/
- 07_bom/
- 08_fabricacao/
- 09_montagem/
- 10_comissionamento/
- 11_calibracao/
- 12_validacao/
- 13_operacao/
- 14_manutencao/
- 15_robustez/
- 16_dados/
- 17_auditabilidade/
- 18_reproducao/
- 19_publicacao/
- 20_releases/

## 19. RESULTADO ESPERADO

Ao final da Etapa 14 deverá existir uma versão oficial do projeto que possa ser:

- fabricada;
- montada;
- calibrada;
- operada;
- mantida;
- auditada;
- reproduzida;
- comparada com o protótipo de referência;
- publicada sem confundir história com reconstrução ou engenharia moderna.

## 20. PRÓXIMA ETAPA

Após a consolidação desta etapa, executar **Etapa 15 — Auditoria Final do Projeto, Controle de Versão e Liberação Oficial**, destinada a verificar integralmente a documentação, rastreabilidade, consistência entre etapas, integridade do repositório e critérios formais de release.
