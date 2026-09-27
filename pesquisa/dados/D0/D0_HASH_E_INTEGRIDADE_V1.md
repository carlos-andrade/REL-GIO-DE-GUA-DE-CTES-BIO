# PROCEDIMENTO DE INTEGRIDADE E HASH — D0

## Finalidade

Estabelecer um procedimento para demonstrar que o arquivo bruto usado na
validação e no processamento corresponde ao arquivo preservado após a
coleta.

## Princípio

O arquivo bruto é evidência primária da coleta.

Nenhum processamento pode substituir, sobrescrever ou apagar o arquivo
bruto original.

## Arquivos controlados

- `D0_GEOMETRIA_BRUTO.csv`
- `D0_GEOMETRIA_PROCESSADO.csv`
- relatório de validação automática
- relatório de sessão
- registro de correções, quando existente

## Hash

Para cada arquivo utilizado em uma etapa formal, registrar:

| Campo | Valor |
|---|---|
| Arquivo | PREENCHER |
| Caminho | PREENCHER |
| Algoritmo | SHA-256 |
| Hash | PREENCHER |
| Data/hora | PREENCHER |
| Operador | PREENCHER |
| Etapa | PREENCHER |

## Regra de alteração

Se um arquivo bruto precisar ser corrigido:

1. não sobrescrever silenciosamente a versão anterior;
2. registrar a correção no `D0_LOG_CORRECOES_V1.md`;
3. preservar a versão anterior;
4. criar nova versão identificável;
5. gerar novo hash;
6. registrar a relação entre as versões;
7. repetir a validação afetada.

## Critério de integridade

Um resultado D0 não será considerado plenamente auditável se não for
possível identificar:

`resultado → arquivo → hash → dados brutos → sessão → instrumento → método`

## Estado

**PROCEDIMENTO DEFINIDO — EXECUÇÃO DE HASH PENDENTE.**

A ausência de hash neste momento não representa falha experimental; significa
apenas que a coleta física ainda não ocorreu.
