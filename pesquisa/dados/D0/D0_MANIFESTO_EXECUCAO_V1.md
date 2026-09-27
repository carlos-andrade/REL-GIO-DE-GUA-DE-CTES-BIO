# MANIFESTO DE EXECUÇÃO — FASE D0

## Identificação
- Projeto: RELÓGIO DE ÁGUA DE CTESÍBIO
- Fase: D0 — Geometria e Volume de Referência
- Estado: PREPARADO PARA EXECUÇÃO FÍSICA
- Dados experimentais homologados: NÃO
- Data de criação: 27/09/2026

## Finalidade

Estabelecer uma identificação única para cada sessão física D0 e manter
rastreabilidade entre configuração, instrumentos, dados brutos,
processamento e revisão.

## Regra de integridade

Este manifesto não contém medições. Nenhum campo experimental pode ser
preenchido por estimativa, memória ou inferência.

Valores ausentes devem permanecer como:
- NÃO MEDIDO
- NÃO CALCULADO
- PENDENTE

## Identificação de sessão

Formato recomendado:

`D0-S###`

Exemplos:
- D0-S001
- D0-S002
- D0-S003

Uma sessão corresponde a uma execução física identificável, com data,
hora, configuração e instrumentos registrados.

## Sequência obrigatória

`D0-S### → REGISTRO DA SESSÃO → INSTRUMENTOS → P01/P02 → CSV BRUTO → VALIDAÇÃO AUTOMÁTICA → PROCESSAMENTO → REVISÃO → ACEITAÇÃO`

## Controles antes da coleta

1. Configuração do protótipo identificada.
2. Instrumentos identificados.
3. Instrumentos aptos ou justificadamente registrados.
4. Ambiente registrado.
5. Registro de sessão aberto.
6. CSV bruto preservado.
7. Procedimento P01/P02 disponível.
8. Nenhuma medição pré-preenchida.

## Controle após a coleta

1. Encerrar sessão.
2. Conferir IDs únicos.
3. Executar validador automatizado.
4. Registrar alertas e erros.
5. Processar somente dados válidos e rastreáveis.
6. Preservar o bruto sem sobrescrita.
7. Submeter resultados à revisão D0.
8. Somente então avaliar fechamento da fase.

## Critério de execução

A existência deste manifesto, do roteiro, dos formulários e do validador
não constitui evidência de execução física.

## Próximo estado

`D0-COLETA`

A transição para processamento depende de dados físicos reais registrados
no arquivo bruto correspondente à sessão.
