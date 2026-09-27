# D0 — MAPA DE EXECUÇÃO S001 V1

## Cadeia operacional

1. ABERTURA
2. IDENTIFICAÇÃO DO PROTÓTIPO
3. IDENTIFICAÇÃO DOS INSTRUMENTOS
4. SNAPSHOT DA CONFIGURAÇÃO
5. REGISTRO DAS CONDIÇÕES
6. P01 — GEOMETRIA
7. P02 — H↔V
8. PRESERVAÇÃO DO RAW
9. VALIDAÇÃO AUTOMÁTICA
10. PROCESSAMENTO
11. ORÇAMENTO DE INCERTEZA
12. REVISÃO
13. DECISÃO

## Portas de controle

| porta | condição mínima | se não cumprida |
|---|---|---|
| G1 | protótipo identificado | bloquear coleta |
| G2 | instrumentos identificados | bloquear coleta |
| G3 | configuração registrada | bloquear coleta |
| G4 | condições registradas | bloquear coleta |
| G5 | P01 executado | não avançar |
| G6 | P02 executado | não avançar |
| G7 | RAW íntegro | bloquear processamento |
| G8 | validação sem erro crítico | bloquear processamento |
| G9 | processamento rastreável | bloquear revisão |
| G10 | incertezas documentadas | bloquear decisão |

## Regra
A existência deste mapa não constitui evidência de execução de qualquer porta.
