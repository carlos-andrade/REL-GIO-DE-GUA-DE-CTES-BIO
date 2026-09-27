# ETAPA 5 — MODELO MATEMÁTICO E PROTÓTIPO EXPERIMENTAL

## Objetivo

Transformar a síntese histórica e técnica em um modelo quantitativo reproduzível para um protótipo moderno inspirado no princípio de Ctesíbio: estabilizar a condição hidráulica de medição antes de converter o deslocamento do fluido em informação temporal.

## 1. Variáveis principais

### Hidráulicas

- H — altura do nível de referência [m]
- A — área da seção do reservatório [m²]
- Q_in — vazão de entrada [m³/s]
- Q_out — vazão de saída [m³/s]
- V — volume [m³]
- p — pressão hidrostática [Pa]
- rho — densidade do fluido [kg/m³]
- g — aceleração gravitacional [m/s²]

Relação básica:

p = p_atm + rho g H

Balanço de volume:

dV/dt = Q_in - Q_out

Para um reservatório de seção aproximadamente constante:

A dH/dt = Q_in - Q_out

A condição de nível constante é:

Q_in ≈ Q_out

e, idealmente:

dH/dt ≈ 0

## 2. Erro de pressão

O projeto deve quantificar o erro causado pela variação da coluna hidráulica.

Para uma saída dependente de carga, uma aproximação inicial pode ser:

Q_out ≈ C_d A_o sqrt(2 g H)

onde C_d é o coeficiente de descarga e A_o é a área efetiva da abertura.

A função do regulador moderno será reduzir a variação de H que aparece na alimentação do estágio de medição.

## 3. Reservatório de nível constante

O protótipo deverá possuir:

- reservatório primário;
- estágio regulador;
- reservatório de referência;
- entrada controlada;
- saída de excesso;
- proteção contra transbordamento;
- acesso para limpeza;
- pontos de medição.

A geometria deverá ser parametrizada para permitir alterações sem reconstrução completa.

## 4. Flutuador

O flutuador deverá converter variação de nível residual em deslocamento mensurável.

Variáveis:

- massa;
- volume deslocado;
- densidade;
- área projetada;
- curso;
- atrito;
- guia mecânica;
- histerese;
- sensibilidade.

A ligação deve minimizar atrito lateral e inclinação.

## 5. Cadeia de medição

Arquitetura recomendada:

nível → flutuador → transmissão → indicador → registro

O sistema moderno poderá acrescentar um sensor digital para auditoria, sem substituir a referência mecânica experimental.

## 6. Ciclo automático

Estados mínimos:

1. ENCHIMENTO
2. ESTABILIZAÇÃO
3. MEDIÇÃO
4. LIMITE_ATINGIDO
5. DESCARGA
6. REINICIALIZAÇÃO
7. VERIFICAÇÃO

Condições de segurança:

- impedir descarga parcial;
- detectar ausência de fluxo;
- detectar transbordamento;
- detectar flutuador travado;
- impedir reinício enquanto o estado hidráulico não estiver estável.

## 7. Descarga

O mecanismo poderá ser um sifão, válvula ou atuador equivalente.

O protótipo deverá medir:

- nível de disparo;
- volume descarregado;
- duração da descarga;
- volume residual;
- tempo de recuperação;
- repetibilidade do ciclo.

A escolha moderna do componente não deverá ser confundida com prova histórica de sua utilização exata.

## 8. Modelo de erro

A análise deverá separar:

### Erros sistemáticos

- geometria;
- calibração;
- offset;
- erro de escala;
- coeficiente hidráulico;
- temperatura;
- evaporação.

### Erros aleatórios

- flutuação da vazão;
- vibração;
- oscilação do flutuador;
- ruído de leitura.

### Erros operacionais

- obstrução;
- vazamento;
- bolhas;
- contaminação;
- desgaste.

## 9. Incerteza

A incerteza deverá ser propagada a partir das grandezas medidas.

Para uma função genérica:

y = f(x1, x2, ..., xn)

a primeira aproximação da incerteza combinada é:

u_y² = Σ (∂f/∂x_i)² u_i²

quando as variáveis forem consideradas não correlacionadas.

Correlações deverão ser incorporadas quando identificadas experimentalmente.

## 10. Calibração

A calibração deverá utilizar uma referência independente de tempo e volume.

Procedimento mínimo:

1. verificar geometria;
2. verificar vazão;
3. estabilizar temperatura;
4. executar ciclos repetidos;
5. medir indicação;
6. comparar com referência;
7. calcular erro;
8. calcular repetibilidade;
9. ajustar parâmetros;
10. repetir ensaio.

Todos os parâmetros de calibração devem possuir versão e data.

## 11. Tolerâncias

As tolerâncias não devem ser arbitrárias.

Cada tolerância deverá ser derivada de:

- requisito de medição;
- sensibilidade do modelo;
- capacidade de fabricação;
- erro observado;
- margem de segurança.

A documentação deverá distinguir tolerância de fabricação, limite operacional e incerteza de medição.

## 12. Instrumentação

Instrumentação mínima recomendada:

- referência de tempo independente;
- balança ou método gravimétrico para vazão;
- termómetro;
- medição de nível;
- recipiente calibrado para volume;
- aquisição de dados;
- registo dos eventos de ciclo.

## 13. Matriz experimental

Testar pelo menos:

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
| E09 | perda de alimentação | comportamento de falha |
| E10 | ciclo completo | auditabilidade |

## 14. Critérios de aceitação

Antes dos ensaios, definir quantitativamente:

- erro máximo admissível;
- desvio padrão máximo;
- tempo máximo de estabilização;
- variação máxima do nível;
- volume residual máximo;
- taxa máxima de falhas;
- número mínimo de ciclos válidos.

Nenhum resultado deverá ser declarado aprovado sem comparar com esses limites previamente definidos.

## 15. Protótipo em fases

### P0 — bancada hidráulica

Validar somente entrada, regulador e nível constante.

### P1 — flutuador

Adicionar indicação mecânica.

### P2 — descarga

Adicionar sifão/atuador e ciclo automático.

### P3 — medição

Adicionar referência independente e aquisição de dados.

### P4 — compensação

Adicionar parametrização sazonal e verificar o efeito experimental.

### P5 — validação

Executar matriz completa de testes e congelar a configuração validada.

## 16. Auditabilidade

Cada ensaio deve possuir:

- ID;
- versão do protótipo;
- configuração;
- parâmetros;
- instrumentos;
- calibração vigente;
- data/hora;
- operador;
- dados brutos;
- processamento;
- resultado;
- decisão de aceitação;
- anomalias.

## Próxima etapa

Depois desta especificação, preparar a **Etapa 6 — Arquitetura Física e BOM**, contendo desenho dimensional preliminar, componentes, materiais, interfaces, fabricação, montagem, manutenção, segurança e custo estimado do protótipo.
