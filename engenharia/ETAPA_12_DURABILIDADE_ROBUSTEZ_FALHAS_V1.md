# ETAPA 12 — ENSAIOS DE DURABILIDADE, ROBUSTEZ E FALHAS V1

## 1. Objetivo

Determinar se o sistema mantém comportamento funcional e metrológico aceitável após operação repetida, variações ambientais e falhas controladas.

Esta etapa não substitui a calibração. Ela verifica estabilidade operacional e capacidade de permanecer dentro das condições especificadas.

## 2. Dimensões da robustez

Avaliar:
- ciclos repetidos;
- desgaste mecânico;
- estabilidade hidráulica;
- variação de temperatura;
- pequenas perturbações de alimentação;
- obstruções controladas;
- contaminação controlada;
- perda de energia;
- falhas de sensores;
- falhas de comunicação;
- recuperação após intervenção.

## 3. Plano de durabilidade

Definir antes do ensaio:
- número total de ciclos;
- duração de cada campanha;
- intervalo entre ciclos;
- condições ambientais;
- limites de parada;
- pontos de inspeção;
- critérios de reprovação.

A quantidade de ciclos deve ser justificada pelo objetivo do protótipo.

## 4. Inspeções intermediárias

Em intervalos definidos registrar:
- desgaste do flutuador;
- desgaste das guias;
- folgas;
- vazamentos;
- deformações;
- alteração de vazão;
- alteração do tempo de descarga;
- alteração do reset;
- alteração da indicação;
- estado dos tubos;
- estado das conexões.

## 5. Ensaio de ciclos repetidos

Executar série prolongada de ciclos automáticos.

Para cada ciclo registrar:
- duração;
- nível de disparo;
- volume descarregado;
- nível de reset;
- erro;
- falhas;
- temperatura;
- configuração.

Avaliar tendência ao longo do número de ciclos.

## 6. Ensaio de variação ambiental

Dentro dos limites seguros do protótipo, avaliar:
- temperatura baixa;
- temperatura nominal;
- temperatura alta;
- variações graduais;
- retorno à condição nominal.

Não executar condições ambientais capazes de criar risco estrutural ou elétrico.

## 7. Ensaio de perturbação hidráulica

Aplicar variações controladas de:
- vazão de entrada;
- pressão de alimentação;
- nível inicial;
- resistência hidráulica.

Verificar se o regulador mantém a condição de referência.

## 8. Ensaio de obstrução

Introduzir restrição controlada em pontos definidos.

Registrar:
- alteração de fluxo;
- tempo de detecção;
- efeito no nível;
- resposta do sistema;
- alarme;
- recuperação.

A obstrução deve ser reversível e executada em condição segura.

## 9. Ensaio de contaminação

Utilizar somente contaminantes controlados e seguros para o protótipo.

Avaliar:
- alteração da transparência;
- aderência;
- atrito;
- obstrução;
- alteração de vazão;
- necessidade de limpeza.

Não utilizar substâncias perigosas.

## 10. Falhas elétricas e digitais

Testar, quando aplicável:
- perda de alimentação;
- reinicialização;
- sensor desconectado;
- sensor saturado;
- comunicação interrompida;
- memória indisponível;
- timestamp inválido;
- configuração ausente.

O sistema deve entrar em estado seguro e preservar o máximo possível de informação diagnóstica.

## 11. Falhas mecânicas

Testar de forma controlada:
- aumento de atrito;
- pequena folga;
- curso incompleto;
- atuador sem confirmação;
- desalinhamento dentro de limite seguro.

Verificar capacidade de detectar a condição antes que ela comprometa a segurança.

## 12. Matriz de falhas

| ID | Falha | Detecção | Resposta esperada | Recuperação |
|---|---|---|---|---|
| F12-01 | sensor desconectado | diagnóstico | bloquear/alarme | reconectar e validar |
| F12-02 | descarga incompleta | nível/timeout | estado seguro | inspeção |
| F12-03 | obstrução | vazão/nível | alarme | limpeza |
| F12-04 | perda de energia | alimentação | estado seguro | reinicialização |
| F12-05 | atuador travado | posição/timeout | bloquear ciclo | intervenção |
| F12-06 | overflow | nível | proteção | inspeção |
| F12-07 | dados ausentes | integridade | marcar inválidos | recuperar |
| F12-08 | deriva | calibração | manutenção | recalibrar |

## 13. Critérios de parada

Interromper o ensaio imediatamente em caso de:
- risco de transbordamento não controlado;
- risco elétrico;
- instabilidade estrutural;
- vazamento relevante;
- temperatura fora do limite;
- movimento mecânico perigoso;
- perda de contenção;
- condição não prevista com risco.

## 14. Manutenção preventiva

Com base nos ensaios, definir:
- frequência de limpeza;
- inspeção de tubos;
- inspeção do flutuador;
- inspeção de guias;
- inspeção de transmissão;
- verificação de conexões;
- verificação de sensores;
- recalibração;
- substituição de peças de desgaste.

## 15. Indicadores de degradação

Monitorar:
- erro por ciclo;
- dispersão;
- tempo de descarga;
- tempo de reset;
- vazão;
- nível;
- atrito;
- deriva;
- taxa de falhas;
- intervenções de manutenção.

## 16. Critérios de aceitação

Antes da campanha definir:
- número mínimo de ciclos;
- erro máximo após campanha;
- aumento máximo de dispersão;
- deriva máxima;
- taxa máxima de falhas;
- tempo máximo de recuperação;
- limite de desgaste;
- disponibilidade mínima.

Não definir os limites depois de observar o resultado.

## 17. Comparação com Ctesíbio

| Princípio | Avaliação moderna |
|---|---|
| Operação hidráulica contínua | Durabilidade do circuito |
| Flutuador | Desgaste e atrito |
| Sifão | Repetibilidade de descarga |
| Engrenagens | Desgaste e folga |
| Escala | Deriva e estabilidade |
| Ajuste sazonal | Persistência dos parâmetros |

## 18. Relatório de robustez

O relatório deve incluir:
1. objetivo;
2. configuração;
3. número de ciclos;
4. condições ambientais;
5. falhas introduzidas;
6. respostas observadas;
7. manutenção executada;
8. dados brutos;
9. indicadores de degradação;
10. não conformidades;
11. critérios de aceitação;
12. conclusão;
13. recomendações.

## 19. Critério de liberação para Etapa 13

Liberar somente quando:
- campanha de durabilidade concluída;
- falhas críticas caracterizadas;
- manutenção definida;
- degradação quantificada;
- limites operacionais documentados;
- dados preservados;
- configuração pós-ensaio identificada.

## 20. Próxima etapa

### ETAPA 13 — VALIDAÇÃO FINAL, RECONSTRUÇÃO HISTÓRICA E COMPARAÇÃO

Objetivo: comparar o protótipo moderno com os princípios históricos documentados, separar claramente fatos históricos de reconstruções e soluções modernas, consolidar resultados experimentais e preparar a documentação final do projeto.
