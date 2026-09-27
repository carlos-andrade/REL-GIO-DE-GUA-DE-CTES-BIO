# ETAPA 08 — CALIBRAÇÃO E VALIDAÇÃO METROLÓGICA V1

## 1. Objetivo

Estabelecer, por ensaio controlado, a relação entre a indicação do protótipo e referências independentes, quantificando erro, repetibilidade, reprodutibilidade, deriva, influência térmica e incerteza.

A Etapa 8 transforma um protótipo funcional em um sistema de medição caracterizado.

## 2. Princípio de rastreabilidade

Toda conclusão metrológica deve ser vinculada a:

REFERÊNCIA INDEPENDENTE
→ MÉTODO DE ENSAIO
→ DADO BRUTO
→ CÁLCULO
→ INCERTEZA
→ RESULTADO
→ CRITÉRIO DE ACEITAÇÃO

Não utilizar a própria indicação do relógio como referência para validar a própria indicação.

## 3. Referências independentes

O plano deve prever, conforme a grandeza ensaiada:
- referência de tempo independente;
- referência de volume;
- referência de vazão, quando aplicável;
- termometria independente;
- instrumentos com resolução compatível com a tolerância desejada.

Cada instrumento deve possuir identificação, faixa, resolução, estado de calibração e incerteza conhecida ou estimada.

## 4. Variáveis

Registrar, no mínimo:
- tempo de referência: t_ref;
- indicação do sistema: t_ind;
- nível: H;
- vazão de entrada: Q_in;
- vazão de saída: Q_out;
- temperatura: T;
- ciclo: N;
- estado do sistema;
- evento de descarga;
- configuração do protótipo.

## 5. Ensaios de calibração

### C01 — Zero

Determinar a indicação de referência na condição inicial.

### C02 — Span

Determinar a resposta em pelo menos dois pontos extremos da faixa operacional.

### C03 — Pontos intermediários

Calibrar múltiplos pontos distribuídos pela faixa, evitando depender apenas de zero e fundo de escala.

### C04 — Repetibilidade

Repetir o mesmo ponto nas mesmas condições e calcular dispersão.

### C05 — Reprodutibilidade

Repetir ensaios em condições controladamente modificadas, incluindo operador, reinício e série temporal quando aplicável.

### C06 — Ciclo completo

Executar sucessivos ciclos de enchimento, medição, descarga e reinicialização.

### C07 — Influência térmica

Executar pontos em diferentes temperaturas dentro da faixa operacional segura.

### C08 — Deriva

Comparar a resposta ao longo do tempo para identificar alteração sistemática.

## 6. Erros

Para cada observação:

e = indicação - referência

Calcular, conforme aplicável:
- erro absoluto;
- erro relativo;
- erro percentual;
- média;
- desvio-padrão;
- amplitude;
- tendência;
- deriva;
- histerese.

Não substituir análise estatística por uma única medição.

## 7. Repetibilidade

Para um conjunto de n observações:

média = Σx_i / n

desvio-padrão = sqrt[Σ(x_i - média)^2 / (n-1)]

A quantidade de repetições deve ser definida antes da execução e mantida constante no ensaio comparável.

## 8. Incerteza

Usar um orçamento explícito de incerteza.

Modelo geral:

u_y² = Σ(∂f/∂x_i)² u_i²

Quando houver correlação entre entradas, incluir os termos de covariância correspondentes.

Componentes a considerar, conforme aplicabilidade:
- referência temporal;
- leitura do nível;
- geometria;
- vazão;
- temperatura;
- resolução;
- repetibilidade;
- deriva;
- histerese;
- sincronização;
- processamento digital;
- erro de posicionamento.

## 9. Compensação

A compensação somente deve ser aplicada após evidência experimental.

Modelo genérico:

y_corrigido = y_indicado - C(T, Q, H, ciclo, ...)

Toda compensação deve possuir:
- variável de entrada;
- modelo;
- parâmetros;
- faixa de validade;
- método de identificação;
- erro residual;
- versão;
- condição de reversão.

Uma correção não pode mascarar uma falha física do sistema.

## 10. Critérios de aceitação

Antes de cada campanha definir:
- faixa operacional;
- erro máximo permitido;
- repetibilidade máxima;
- deriva máxima;
- histerese máxima;
- tempo máximo de estabilização;
- tolerância do disparo;
- tolerância do reset;
- incerteza máxima aceitável.

Os valores devem ser derivados dos requisitos do projeto, e não ajustados depois de observar os resultados.

## 11. Matriz mínima

| Ensaio | Condição | Repetições | Grandezas | Resultado |
|---|---|---:|---|---|
| C01 | zero | definida no protocolo | indicação | aprovado/reprovado |
| C02 | extremos | definida | indicação/referência | aprovado/reprovado |
| C03 | intermediários | definida | indicação/referência | curva |
| C04 | nominal | definida | repetibilidade | estatística |
| C05 | condições alteradas | definida | reprodutibilidade | estatística |
| C06 | ciclos completos | definida | ciclo/erro | tendência |
| C07 | temperatura | definida | erro/T | modelo |
| C08 | longo prazo | definida | erro/tempo | deriva |

## 12. Registro por ensaio

Cada ensaio deve gerar:
- ID;
- data/hora;
- operador;
- configuração;
- instrumentos;
- condições ambientais;
- procedimento;
- dados brutos;
- cálculos;
- gráficos/tabelas;
- resultado;
- não conformidades;
- aprovação ou reprovação.

## 13. Validação da curva de calibração

A curva somente será aceita quando:
- os resíduos estiverem documentados;
- não houver padrão sistemático não explicado;
- os pontos independentes forem compatíveis com o modelo;
- a faixa de validade estiver definida;
- a incerteza residual estiver calculada.

Evitar extrapolação fora da faixa ensaiada.

## 14. Validação do ciclo automático

Verificar em cada ciclo:

ENCHIMENTO → ESTABILIZAÇÃO → MEDIÇÃO → LIMITE → DESCARGA → RESET

Registrar se a descarga altera a indicação seguinte de forma sistemática.

O reset deve restabelecer uma condição conhecida e reproduzível.

## 15. Deriva e manutenção

Definir:
- periodicidade de recalibração;
- condições que exigem recalibração imediata;
- limites de deriva;
- inspeções preventivas;
- registro de intervenções;
- versão da curva de calibração.

Qualquer alteração estrutural, hidráulica, mecânica ou de firmware deve ser avaliada quanto ao impacto metrológico.

## 16. Relatório metrológico

O relatório deve conter:
1. identificação do protótipo;
2. objetivo;
3. configuração;
4. referências utilizadas;
5. condições ambientais;
6. método;
7. dados brutos;
8. cálculos;
9. erros;
10. repetibilidade;
11. reprodutibilidade;
12. incerteza;
13. compensações;
14. limitações;
15. critérios de aceitação;
16. resultados;
17. conclusão técnica;
18. anexos e evidências.

## 17. Critério de liberação para Etapa 9

A Etapa 9 somente será iniciada quando:
- calibração concluída;
- dados brutos preservados;
- incerteza documentada;
- curva ou modelo de correção validado, se utilizado;
- repetibilidade caracterizada;
- ciclo automático validado;
- limites de operação definidos;
- configuração metrológica congelada.

## 18. Próxima etapa

### ETAPA 09 — COMPENSAÇÃO SAZONAL E CONTROLE ADAPTATIVO

Objetivo: implementar e validar a adaptação da escala ou do algoritmo aos ciclos sazonais, separando claramente a compensação astronômica/temporal da correção hidráulica e garantindo auditabilidade da regra aplicada.
