# ETAPA 5 — MODELO MATEMÁTICO E PROTÓTIPO EXPERIMENTAL

## Objetivo

Transformar a síntese histórica e técnica em um modelo quantitativo reproduzível para um protótipo moderno inspirado no princípio de Ctesíbio: estabilizar a condição hidráulica de medição antes de converter o deslocamento do fluido em informação temporal.

## Variáveis principais

- H — altura do nível de referência [m]
- A — área da seção do reservatório [m²]
- Q_in — vazão de entrada [m³/s]
- Q_out — vazão de saída [m³/s]
- V — volume [m³]
- p — pressão hidrostática [Pa]
- rho — densidade [kg/m³]
- g — aceleração gravitacional [m/s²]

Relações iniciais:

p = p_atm + rho g H

dV/dt = Q_in - Q_out

Para seção aproximadamente constante:

A dH/dt = Q_in - Q_out

A condição de nível constante é Q_in ≈ Q_out.

## Erro hidráulico

Para uma saída dependente da carga, usar como primeira aproximação:

Q_out ≈ C_d A_o sqrt(2 g H)

onde C_d é o coeficiente de descarga e A_o a área efetiva da abertura.

O regulador deverá reduzir a variação de H na alimentação do estágio de medição.

## Cadeia de medição

nível → flutuador → transmissão → indicador → registro

O sistema moderno poderá acrescentar sensor digital para auditoria sem substituir a referência mecânica experimental.

## Ciclo automático

Estados:

1. ENCHIMENTO
2. ESTABILIZAÇÃO
3. MEDIÇÃO
4. LIMITE_ATINGIDO
5. DESCARGA
6. REINICIALIZAÇÃO
7. VERIFICAÇÃO

Devem existir proteções contra descarga parcial, ausência de fluxo, transbordamento e flutuador travado.

## Descarga

Medir nível de disparo, volume descarregado, duração, volume residual, tempo de recuperação e repetibilidade.

A escolha moderna do componente não deve ser confundida com prova histórica de sua utilização exata.

## Modelo de erro

Separar erros sistemáticos, aleatórios e operacionais.

Sistemáticos: geometria, calibração, offset, escala, coeficiente hidráulico, temperatura e evaporação.

Aleatórios: flutuação da vazão, vibração, oscilação do flutuador e ruído de leitura.

Operacionais: obstrução, vazamento, bolhas, contaminação e desgaste.

## Incerteza

Para y = f(x1, ..., xn), usar inicialmente:

u_y² = Σ (∂f/∂x_i)² u_i²

para variáveis não correlacionadas. Correlações devem ser incorporadas quando identificadas.

## Calibração

1. verificar geometria;
2. verificar vazão;
3. estabilizar temperatura;
4. executar ciclos repetidos;
5. medir indicação;
6. comparar com referência;
7. calcular erro e repetibilidade;
8. ajustar parâmetros;
9. repetir ensaio.

Parâmetros de calibração devem possuir versão e data.

## Tolerâncias

Cada tolerância deverá derivar de requisito de medição, sensibilidade, capacidade de fabricação, erro observado e margem de segurança.

Distinguir tolerância de fabricação, limite operacional e incerteza de medição.

## Instrumentação

- referência de tempo independente;
- medição gravimétrica ou equivalente para vazão;
- termómetro;
- medição de nível;
- recipiente calibrado para volume;
- aquisição de dados;
- registo de eventos.

## Matriz experimental

| Ensaio | Condição | Variável |
|---|---|---|
| E01 | vazão nominal | estabilidade do nível |
| E02 | vazão baixa | estabilidade |
| E03 | vazão alta | estabilidade |
| E04 | ciclos repetidos | repetibilidade |
| E05 | variação térmica | deriva |
| E06 | perturbação do flutuador | recuperação |
| E07 | descarga repetida | consistência |
| E08 | obstrução controlada | segurança |
| E09 | perda de alimentação | falha |
| E10 | ciclo completo | auditabilidade |

## Critérios de aceitação

Definir antes dos ensaios:

- erro máximo admissível;
- desvio padrão máximo;
- tempo máximo de estabilização;
- variação máxima do nível;
- volume residual máximo;
- taxa máxima de falhas;
- número mínimo de ciclos válidos.

## Fases do protótipo

P0 — bancada hidráulica.

P1 — flutuador e indicação.

P2 — descarga e ciclo automático.

P3 — referência independente e aquisição de dados.

P4 — compensação sazonal.

P5 — validação completa.

## Auditabilidade

Cada ensaio deve possuir ID, versão do protótipo, configuração, parâmetros, instrumentos, calibração vigente, data/hora, dados brutos, processamento, resultado, decisão de aceitação e anomalias.

## Próxima etapa

A próxima etapa é a **Etapa 6 — Arquitetura Física e BOM**, contendo desenho dimensional preliminar, componentes, materiais, interfaces, fabricação, montagem, manutenção, segurança e custo estimado.