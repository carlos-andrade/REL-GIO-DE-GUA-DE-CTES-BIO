# ETAPA 11 — INTEGRAÇÃO DO SISTEMA, REGISTRO DE DADOS E AUDITABILIDADE V1

## 1. Objetivo

Consolidar hidráulica, mecânica, instrumentação, controle, compensação sazonal e ciclo automático em uma arquitetura integrada, capaz de registrar e reconstruir qualquer ciclo experimental.

A integração deve preservar separação de responsabilidades, rastreabilidade e capacidade de auditoria.

## 2. Arquitetura integrada

Fluxo funcional:

ALIMENTAÇÃO
→ PRÉ-REGULAÇÃO
→ RESERVATÓRIO DE REFERÊNCIA
→ FLUTUADOR
→ TRANSMISSÃO
→ INDICAÇÃO

Em paralelo:

SENSORES
→ AQUISIÇÃO
→ CONTROLE
→ REGISTRO

E:

CALENDÁRIO/REFERÊNCIA TEMPORAL
→ COMPENSAÇÃO SAZONAL
→ ESCALA/ATUADOR
→ INDICAÇÃO

E o ciclo automático:

NÍVEL-LIMITE
→ DESCARGA
→ RESET
→ VERIFICAÇÃO
→ NOVO CICLO

## 3. Camadas do sistema

### L0 — Física

- água;
- reservatórios;
- tubos;
- flutuador;
- sifão;
- estrutura.

### L1 — Mecânica

- guias;
- polias;
- engrenagens;
- transmissão;
- escala;
- atuadores.

### L2 — Instrumentação

- nível;
- temperatura;
- posição;
- fluxo, quando utilizado;
- referência temporal.

### L3 — Controle

- máquina de estados;
- limites;
- intertravamentos;
- timeouts;
- controle de descarga.

### L4 — Compensação

- modelo sazonal;
- parâmetros temporais;
- correções validadas;
- versão do algoritmo.

### L5 — Dados

- aquisição;
- timestamps;
- armazenamento;
- eventos;
- configuração;
- auditoria.

## 4. Identidade do sistema

Cada protótipo deve possuir:

- prototype_id;
- versão mecânica;
- versão hidráulica;
- versão elétrica;
- versão de firmware;
- versão de software;
- versão do modelo sazonal;
- versão da calibração;
- data de configuração.

Nenhum conjunto de dados deve existir sem identificação da configuração que o produziu.

## 5. Estrutura mínima do registro

Cada amostra deve conter:

- timestamp;
- prototype_id;
- cycle_id;
- estado;
- nível;
- posição;
- temperatura;
- vazão, quando disponível;
- indicação;
- referência;
- parâmetros ativos;
- qualidade do dado.

Exemplo lógico:

timestamp | cycle_id | state | H | position | T | indication | reference | quality

## 6. Registro de eventos

Além das amostras contínuas, registrar eventos discretos:

- START;
- STOP;
- ESTABILIZAÇÃO;
- LIMITE_ATINGIDO;
- DESCARGA_INÍCIO;
- DESCARGA_FIM;
- RESET_INÍCIO;
- RESET_FIM;
- COMPENSAÇÃO_ATUALIZADA;
- ALARME;
- FALHA;
- RECUPERAÇÃO;
- CONFIGURAÇÃO_ALTERADA.

Cada evento deve conter timestamp e origem.

## 7. Sincronização temporal

Todas as fontes devem utilizar uma referência temporal comum.

Registrar:
- origem do relógio;
- precisão estimada;
- método de sincronização;
- offset conhecido;
- estado de sincronização.

Se houver perda da referência temporal, o sistema deve marcar os dados afetados como potencialmente inválidos.

## 8. Qualidade do dado

Cada registro deve possuir estado:

- VALID — válido;
- SUSPECT — suspeito;
- INVALID — inválido;
- MISSING — ausente;
- ESTIMATED — estimado.

Dados estimados não devem ser confundidos com dados medidos.

## 9. Integridade

O sistema deve permitir detectar:
- dados truncados;
- timestamps duplicados;
- lacunas;
- alteração de configuração;
- perda de comunicação;
- reinicialização;
- corrupção de arquivo;
- alteração posterior dos dados.

Quando tecnicamente viável, utilizar checksum ou hash por arquivo/lote.

## 10. Configuração versionada

Toda configuração deve ser armazenada como artefato versionado contendo:

- parâmetros hidráulicos;
- limites;
- calibração;
- parâmetros sazonais;
- relações mecânicas;
- sensores;
- firmware;
- software;
- data de ativação.

Mudanças devem gerar nova versão.

## 11. Máquina de estados integrada

Estados:

BOOT
→ SELF_TEST
→ READY
→ FILL
→ STABILIZE
→ MEASURE
→ LIMIT
→ DISCHARGE
→ RESET
→ VERIFY
→ READY

Falha:

QUALQUER_ESTADO
→ FAULT
→ SAFE
→ RECOVERY
→ SELF_TEST

A transição deve ser registrada.

## 12. Hierarquia de autoridade

Para evitar comandos conflitantes:

1. segurança;
2. proteção hidráulica;
3. integridade do ciclo;
4. controle;
5. compensação;
6. indicação;
7. registro auxiliar.

Nenhuma camada inferior pode anular uma proteção superior.

## 13. Interface entre subsistemas

### Hidráulica → Instrumentação
Nível, vazão e temperatura.

### Instrumentação → Controle
Valores filtrados, estados de qualidade e eventos.

### Controle → Atuadores
Comandos autorizados.

### Atuadores → Controle
Confirmação de posição ou estado.

### Referência temporal → Compensação
Parâmetros temporais.

### Compensação → Indicação
Transformação validada.

### Todos → Dados
Registro auditável.

## 14. Taxa de aquisição

A frequência de aquisição deve ser definida por variável.

Critério:

frequência de aquisição >> frequência característica do fenômeno observado

Eventos rápidos, como descarga e acionamento, podem exigir taxa superior à utilizada durante a estabilização.

A frequência adotada deve ser registrada na configuração.

## 15. Filtragem

Filtragem somente deve ser aplicada quando:
- objetivo definido;
- resposta temporal conhecida;
- atraso quantificado;
- impacto metrológico avaliado.

O dado bruto deve ser preservado sempre que possível.

Estrutura recomendada:

DADO_BRUTO
→ PROCESSAMENTO
→ DADO_VALIDADO
→ INDICAÇÃO

## 16. Banco/arquivo de dados

Estrutura mínima recomendada:

dados/
├── bruto/
├── processado/
├── eventos/
├── configuracoes/
├── calibracoes/
├── relatorios/
└── auditoria/

Cada campanha deve possuir identificador próprio.

## 17. Pacote de auditoria

Para reconstruir um ciclo, devem estar disponíveis:

1. dados brutos;
2. eventos;
3. configuração;
4. calibração;
5. modelo sazonal;
6. versões de firmware/software;
7. referências utilizadas;
8. condições ambientais;
9. logs de falhas;
10. relatório do ensaio.

A ausência de qualquer elemento crítico deve ser explicitamente registrada.

## 18. Reconstrução de um ciclo

A auditoria deve permitir:

CYCLE_ID
→ CONFIGURAÇÃO
→ DADOS BRUTOS
→ EVENTOS
→ PROCESSAMENTO
→ COMPENSAÇÃO
→ INDICAÇÃO
→ REFERÊNCIA
→ ERRO

O resultado reconstruído deve ser reproduzível utilizando as mesmas versões.

## 19. Controle de alterações

Alterações em:
- hardware;
- hidráulica;
- mecânica;
- sensores;
- firmware;
- software;
- parâmetros;
- calibração;
- modelo sazonal

devem produzir registro de mudança contendo:
- versão anterior;
- versão nova;
- motivo;
- responsável;
- data;
- testes necessários;
- resultado;
- aprovação.

## 20. Backup e preservação

Manter pelo menos:
- cópia de trabalho;
- cópia de preservação;
- registro no repositório para documentos e metadados.

Dados brutos não devem ser sobrescritos.

Correções devem gerar nova versão.

## 21. Testes de integração

### I11-01 — aquisição contínua
Verificar todos os canais.

### I11-02 — sincronização
Comparar timestamps.

### I11-03 — ciclo completo
Verificar registro de todos os estados.

### I11-04 — falha de sensor
Verificar qualidade e alarme.

### I11-05 — reinicialização
Verificar recuperação e preservação do histórico.

### I11-06 — alteração de configuração
Verificar versionamento.

### I11-07 — perda de comunicação
Verificar marcação dos dados afetados.

### I11-08 — reconstrução
Reproduzir um ciclo apenas com o pacote de auditoria.

## 22. Critérios de aceitação

Definir antes dos testes:
- perda máxima aceitável de amostras;
- erro máximo de timestamp;
- latência máxima;
- integridade mínima dos arquivos;
- tempo máximo de recuperação;
- completude mínima do pacote de auditoria;
- taxa máxima de eventos não registrados.

## 23. Segurança dos dados

Dados históricos não devem ser alterados silenciosamente.

Quando houver correção:
- preservar original;
- registrar motivo;
- criar nova versão;
- manter relação entre original e corrigido.

## 24. Comparação com Ctesíbio

| Elemento histórico | Sistema moderno |
|---|---|
| Movimento físico contínuo | Sensores + aquisição |
| Indicador mecânico | Indicador mecânico/digital |
| Ciclo hidráulico | Máquina de estados |
| Engrenagens | Atuadores/transmissão |
| Escala sazonal | Modelo versionado |
| Observação do mecanismo | Telemetria auditável |

A instrumentação moderna amplia a observabilidade; não deve ser apresentada como parte do mecanismo histórico original.

## 25. Critério de liberação para Etapa 12

Liberar somente quando:
- subsistemas integrados;
- sincronização validada;
- aquisição validada;
- eventos registrados;
- configuração versionada;
- falhas registradas;
- dados brutos preservados;
- reconstrução de ciclo demonstrada;
- pacote de auditoria completo.

## 26. Próxima etapa

### ETAPA 12 — ENSAIOS DE DURABILIDADE, ROBUSTEZ E FALHAS

Objetivo: avaliar comportamento do sistema após operação prolongada, repetição de ciclos, perturbações controladas, envelhecimento, contaminação, variação ambiental e falhas previsíveis, estabelecendo limites de operação e manutenção.
