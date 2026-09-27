# SÍNTESE TÉCNICA E RECONSTRUÇÃO — CTESÍBIO

## Etapa 4

Esta etapa transforma evidência documental validada em uma especificação técnica separada em três camadas:

1. HISTÓRICA — o que as fontes permitem afirmar sobre o mecanismo antigo.
2. RECONSTRUTIVA — interpretações modernas necessárias para montar um modelo funcional.
3. PROJETUAL — soluções contemporâneas propostas para o protótipo de medição contínua e autoajustável.

## Entradas

- pesquisa/relatorios/RELATORIO_VALIDACAO_V1.md
- fontes classificadas e revisadas;
- registros de contradições;
- reconstruções arqueológicas e acadêmicas;
- dados hidráulicos e metrológicos.

## Entregáveis

### 1. Matriz histórica
Para cada componente: reservatório, regulador de nível, flutuador, indicador, escala, sifão/descarga, engrenagens, atuadores e compensação temporal/sazonal.

Registrar evidência, fonte, grau de certeza e controvérsias.

### 2. Modelo funcional

Descrever a cadeia:

fonte de água → regulação → reservatório de nível constante → flutuador → transmissão → indicação → descarga → reinicialização

Quando uma ligação for apenas hipótese reconstrutiva, marcá-la explicitamente.

### 3. Modelo hidráulico

Definir, no mínimo: nível do reservatório, pressão hidrostática, vazão de entrada, vazão de saída, área efetiva, volume, altura de referência, tempo de ciclo e estabilidade do nível.

A análise deve considerar a relação entre pressão e vazão e identificar as fontes de erro.

### 4. Cadeia metrológica

Definir:

grandeza física → sensor/boia → transmissão → escala → leitura

Especificar resolução, repetibilidade, histerese, deriva, erro sistemático e incerteza.

### 5. Compensação sazonal

Separar evidência histórica, interpretação e solução moderna.

Uma implementação moderna poderá usar tabelas parametrizadas, calendário astronômico ou software, mas isso não deve ser apresentado como prova de que Ctesíbio utilizava tecnologia equivalente.

### 6. Descarga e reinicialização

Especificar nível de disparo, condição de acionamento, mecanismo de descarga, duração, condição de retorno, prevenção de ciclos incompletos e detecção de falha.

### 7. Controle e auditabilidade

Toda medição deverá permitir reconstruir:

entrada → estado do sistema → evento → indicação → descarga → reinício

Registrar timestamp, estado, parâmetros de calibração e eventos anômalos no protótipo moderno.

## Critérios de engenharia

O protótipo deverá ser avaliado por precisão, exatidão, estabilidade, repetibilidade, robustez, tolerância a variações de vazão, tolerância a temperatura, resistência a obstrução, segurança contra transbordamento, facilidade de manutenção e auditabilidade.

## Regra fundamental

Não converter uma reconstrução moderna em fato histórico. Cada afirmação deverá possuir uma etiqueta:

- HISTÓRICO
- INTERPRETAÇÃO
- RECONSTRUÇÃO
- PROPOSTA MODERNA
- HIPÓTESE
- NÃO DETERMINADO

## Próxima etapa

Depois da síntese, preparar o modelo matemático e o protótipo experimental, incluindo dimensionamento, equações, tolerâncias, materiais, instrumentação, plano de calibração e matriz de testes.
