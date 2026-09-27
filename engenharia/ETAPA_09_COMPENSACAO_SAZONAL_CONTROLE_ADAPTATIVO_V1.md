# ETAPA 09 — COMPENSAÇÃO SAZONAL E CONTROLE ADAPTATIVO V1

## 1. Objetivo

Projetar e validar a adaptação sazonal da indicação temporal sem confundir a variação astronômica das horas com a estabilidade hidráulica do sistema.

A compensação deve preservar o princípio central do projeto: o controle hidráulico mantém condições de referência estáveis; a escala, o mecanismo ou o software traduz essa referência para a convenção temporal desejada.

## 2. Separação de funções

O sistema deve possuir três camadas independentes:

1. Estabilização hidráulica: mantém o nível de referência, reduz o efeito da queda de pressão e controla Q_in e Q_out.
2. Medição física: converte nível/deslocamento em variável mensurável e registra posição, tempo e eventos.
3. Compensação temporal: adapta escala ou algoritmo conforme a data e o ciclo definido; não corrige falhas hidráulicas.

Fluxo:

CONTROLE HIDRÁULICO → MEDIÇÃO → REFERÊNCIA TEMPORAL → COMPENSAÇÃO SAZONAL → INDICAÇÃO

## 3. Definição do modelo temporal

Antes da implementação, definir formalmente qual convenção será indicada:
- horas uniformes de 24 horas;
- horas sazonais/temporais;
- divisão específica de luz e escuridão;
- outra convenção experimental.

A convenção escolhida deve possuir definição matemática, intervalo de validade, origem temporal, unidade e regra de transição.

## 4. Variáveis

Registrar:
- data;
- hora de referência;
- latitude;
- longitude;
- fuso horário, quando aplicável;
- instante de início e fim do ciclo;
- duração do período de luz;
- duração do período de escuridão;
- duração da hora sazonal;
- posição física do indicador;
- indicação compensada;
- versão do modelo.

## 5. Modelo matemático básico

Para um período de luz com duração D_luz dividido em N partes:

duracao_hora_luz = D_luz / N

Para um período de escuridão:

duracao_hora_escura = D_escura / N

A indicação sazonal pode ser representada por função por partes:

H_sazonal(t) = f_luz(t) durante a luz

H_sazonal(t) = f_escura(t) durante a escuridão

Os limites de transição devem ser definidos explicitamente.

## 6. Fonte astronômica e referência

Quando o modelo depender de nascer/pôr do Sol ou outros eventos astronômicos, registrar a origem dos parâmetros.

O projeto deve distinguir:
- dado astronômico de entrada;
- regra de conversão temporal;
- indicação produzida pelo relógio.

Não considerar a indicação do protótipo como fonte dos próprios parâmetros de compensação.

## 7. Estratégias de implementação

### A — Escala física substituível

Utilizar escalas diferentes para períodos definidos.

Vantagens:
- simples;
- auditável;
- preserva forte analogia histórica.

Limitações:
- exige troca física;
- menor automação.

### B — Escala móvel

Utilizar mecanismo para deslocar ou girar uma escala conforme o calendário.

Vantagens:
- atualização automática;
- mantém leitura mecânica.

Riscos:
- folga;
- erro de posicionamento;
- desgaste;
- complexidade mecânica.

### C — Atuador com escala digital

Manter a medição física e usar atuador/display para aplicar a transformação.

Vantagens:
- flexibilidade;
- registro digital;
- fácil atualização.

Riscos:
- dependência eletrônica;
- erro de software;
- necessidade de versionamento.

### D — Modelo híbrido

Combinar escala mecânica, sensor de posição e compensação digital.

Deve ser tratado como arquitetura experimental quando a prioridade for auditabilidade e comparação entre indicação física e cálculo digital.

## 8. Regra de controle

A compensação não deve atuar continuamente sobre o regulador hidráulico para corrigir erro de indicação.

Regra:
- erro hidráulico → corrigir hidráulica;
- erro temporal/modelo → corrigir modelo;
- erro mecânico → corrigir mecânica;
- erro de sensor → corrigir instrumentação.

Isso evita que diferentes fontes de erro sejam mascaradas por uma única variável de controle.

## 9. Atualização sazonal

Rotina:

IDENTIFICAR DATA
→ CARREGAR PARÂMETROS
→ VALIDAR PARÂMETROS
→ CALCULAR ESCALA
→ VERIFICAR LIMITES
→ ATIVAR CONFIGURAÇÃO
→ REGISTRAR EVENTO

Cada atualização deve gerar log com timestamp, configuração anterior, configuração nova, parâmetros utilizados, versão do modelo e resultado da validação.

## 10. Controle adaptativo

O termo adaptativo fica restrito à atualização de parâmetros previamente definidos.

O sistema não deve alterar livremente sua própria lei de controle com base em dados insuficientes.

Parâmetros adaptáveis possíveis:
- posição da escala;
- relação de transmissão;
- offset;
- fator de conversão;
- tabela sazonal;
- parâmetros térmicos previamente validados.

Toda alteração automática deve possuir limites superior e inferior.

## 11. Validação da compensação

Executar, no mínimo:
- S01 — período curto;
- S02 — transição entre luz e escuridão;
- S03 — extremos sazonais;
- S04 — repetição;
- S05 — perturbação hidráulica controlada;
- S06 — perda ou corrupção de parâmetro.

Em cada ensaio verificar indicação, referência, erro, estabilidade, logs e condição de segurança.

## 12. Critérios de aceitação

Antes dos testes definir:
- erro temporal máximo;
- erro de posicionamento máximo;
- erro de transição máximo;
- atraso máximo de atualização;
- tolerância de parâmetros;
- faixa válida do modelo;
- comportamento em dados inválidos;
- comportamento em falha de energia;
- requisito de recuperação.

A compensação deve ser rejeitada se produzir melhoria aparente apenas por mascarar erro hidráulico, mecânico ou instrumental.

## 13. Auditoria do algoritmo

A implementação deve possuir:
- identificador do modelo;
- versão;
- data de criação;
- parâmetros;
- unidades;
- limites;
- origem dos dados;
- algoritmo;
- casos de teste;
- resultado esperado;
- resultado observado.

Para cada indicação deve ser possível reconstruir:

ENTRADA → PARÂMETROS → CÁLCULO → SAÍDA

## 14. Proteções

Se parâmetros sazonais estiverem ausentes, inválidos ou fora dos limites:

FALHA_DE_PARAMETRO → BLOQUEAR_ATUALIZAÇÃO → MANTER_ULTIMA_CONFIGURAÇÃO_VALIDADA → GERAR_ALARME

Se a última configuração não estiver disponível:

FALHA_DE_RECUPERAÇÃO → MODO_SEGURO

O modo seguro deve ser definido no projeto executivo antes da implementação.

## 15. Comparação com Ctesíbio

| Princípio histórico | Implementação moderna |
|---|---|
| Variação sazonal da escala | Modelo temporal versionado |
| Escala variável | Escala física, móvel ou digital |
| Mecanismo automático | Atuador/software controlado |
| Referência hidráulica | Reservatório de nível controlado |
| Indicação mecânica | Sensor + indicador mecânico/digital |
| Ajuste periódico | Atualização sazonal auditável |
| Mecanismo físico | Modelo híbrido físico-digital |

A tabela não afirma que todas as soluções modernas reproduzem literalmente o mecanismo histórico.

## 16. Dados de teste

Cada teste deve preservar:
- configuração hidráulica;
- configuração mecânica;
- versão do algoritmo;
- parâmetros sazonais;
- referência temporal;
- dados brutos;
- saída calculada;
- indicação física;
- erro;
- condições ambientais;
- logs.

## 17. Critério de liberação para Etapa 10

A etapa será considerada concluída somente quando:
- convenção temporal definida;
- modelo matemático documentado;
- parâmetros versionados;
- transições testadas;
- falhas de entrada testadas;
- erro de compensação quantificado;
- separação entre erros hidráulicos e temporais demonstrada;
- logs auditáveis;
- configuração aprovada e congelada.

## 18. Próxima etapa

### ETAPA 10 — CICLO AUTOMÁTICO, DESCARGA, RESET E ATUADORES

Objetivo: validar integralmente o ciclo automático do protótipo, incluindo detecção do nível-limite, acionamento da descarga, reinicialização hidráulica e atualização mecânica/digital da escala, com análise de falhas e recuperação.
