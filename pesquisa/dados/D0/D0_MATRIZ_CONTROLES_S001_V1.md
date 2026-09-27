# MATRIZ DE CONTROLES — D0-S001

## Finalidade

Controlar a primeira sessão física D0 por requisito, evidência, estado e
critério de passagem.

| ID | Controle | Evidência esperada | Estado inicial | Critério de passagem |
|---|---|---|---|---|
| S001-01 | Identificação da sessão | Registro D0-S001 | PENDENTE | ID único |
| S001-02 | Configuração | identificação do protótipo | PENDENTE | configuração registrada |
| S001-03 | Instrumentos | cadastro de instrumentos | PENDENTE | IDs e características |
| S001-04 | P01 geometria | dados dimensionais | PENDENTE | medições reais |
| S001-05 | P02 H↔V | pares altura-volume | PENDENTE | dados reais rastreáveis |
| S001-06 | Repetibilidade | repetições | PENDENTE | mínimo definido no protocolo |
| S001-07 | Ambiente | temperatura/condições | PENDENTE | registro disponível |
| S001-08 | Integridade | hash | PENDENTE | hash registrado |
| S001-09 | Validação | relatório automático | PENDENTE | execução registrada |
| S001-10 | Processamento | CSV processado | PENDENTE | derivação rastreável |
| S001-11 | Incerteza | cálculo/documentação | PENDENTE | componentes identificados |
| S001-12 | Revisão | formulário de aceitação | PENDENTE | revisão concluída |
| S001-13 | Fechamento D0 | decisão formal | PENDENTE | critérios atendidos |

## Estados

- PENDENTE
- EM EXECUÇÃO
- COLETADO
- EM PROCESSAMENTO
- EM REVISÃO
- ACEITO
- ACEITO COM RESSALVAS
- REJEITADO

## Regra

Nenhum estado posterior poderá ser marcado sem a evidência correspondente.

## Estado atual

**PENDENTE — S001 AINDA NÃO EXECUTADA.**
