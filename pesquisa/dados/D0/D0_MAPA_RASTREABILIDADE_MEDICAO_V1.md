# D0 — MAPA DE RASTREABILIDADE DA MEDIÇÃO V1

## Objetivo
Ligar cada resultado processado à evidência física que o originou.

## Cadeia oficial

RESULTADO
→ ID DO GRUPO PROCESSADO
→ IDS DOS DADOS BRUTOS
→ INSTRUMENTO_ID
→ MÉTODO
→ SESSÃO
→ DATA/HORA
→ CONDIÇÕES
→ PROTÓTIPO/CONFIGURAÇÃO

## Matriz

| Elemento | Fonte | Obrigatório |
|---|---|---|
| Resultado estatístico | D0_GEOMETRIA_PROCESSADO.csv | Sim |
| Observações | D0_GEOMETRIA_BRUTO.csv | Sim |
| Instrumento | D0_CADASTRO_INSTRUMENTOS_V1.md | Sim |
| Método | D0_FICHA_COLETA_FISICA_V1.md | Sim |
| Sessão | D0_REGISTRO_SESSAO_MEDICAO_V1.md | Sim |
| Configuração | Registro de sessão | Sim |
| Condições ambientais | Registro de sessão / dados brutos | Quando relevante |

## Regra
Um resultado sem cadeia completa de rastreabilidade não pode ser classificado como resultado D0 validado.

## Estado
PREPARADO — AGUARDANDO DADOS FÍSICOS.
