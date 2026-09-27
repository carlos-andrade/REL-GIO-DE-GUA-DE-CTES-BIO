# D0 — CONTROLE DE PREENCHIMENTO S001 V1

## Regras de entrada
- Um registro por observação.
- Uma repetição possui ID próprio.
- Usar unidade explícita.
- Registrar instrumento_id.
- Registrar data/hora.
- Registrar condição relevante.
- Registrar anomalia sem apagar o valor observado.

## Valores especiais
- NÃO MEDIDO = observação não realizada.
- NÃO CALCULADO = resultado ainda não processado.
- PENDENTE = campo/etapa aguardando execução.

Nenhum destes estados pode ser convertido automaticamente em zero.

## Correção
Correções posteriores devem ser feitas por novo registro/versionamento e documentadas no log de correções.

## Estado
ATIVO — CONTROLE PARA S001.
