# D0 — DICIONÁRIO DE DADOS V1

## Dados brutos
| Campo | Tipo | Unidade | Regra |
|---|---|---|---|
| id | texto | — | único e permanente |
| componente | texto | — | código do componente |
| grandeza | texto | — | grandeza medida |
| unidade | texto | — | unidade SI quando aplicável |
| metodo | texto | — | método efetivamente usado |
| instrumento | texto | — | identificação legível |
| instrumento_id | texto | — | chave de rastreabilidade |
| resolucao | número | unidade da grandeza | conforme instrumento |
| temperatura_c | número | °C | registrar quando relevante |
| repeticao | inteiro | — | sequência da repetição |
| valor_bruto | número/texto | unidade | valor observado; não substituir ausência por zero |
| incerteza | número/texto | unidade | somente quando determinada |
| observacao | texto | — | contexto/anomalia |
| data_hora | data/hora | ISO 8601 | momento da aquisição |
| status | enum | — | ABERTO/VALIDADO/REJEITADO/NÃO MEDIDO |

## Dados processados
| Campo | Regra |
|---|---|
| media | calculada somente com dados válidos |
| desvio_padrao | desvio amostral |
| incerteza_tipo_A | s/sqrt(n) |
| incerteza_tipo_B | baseada em evidência metrológica |
| incerteza_combinada | somente após componentes determinados |
| status | PENDENTE/VALIDADO/REJEITADO |

## Regras de integridade
1. NÃO MEDIDO não é zero.
2. NÃO CALCULADO não é zero.
3. Valores derivados devem identificar sua origem.
4. Dados brutos não são sobrescritos por resultados processados.
5. Cada resultado deve apontar para os IDs brutos usados.
