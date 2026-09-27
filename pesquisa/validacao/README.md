# PRÓXIMA ETAPA — VALIDAÇÃO DE FONTES

Esta etapa está preparada para execução após a primeira rodada do coletor.

## Procedimento

1. Ler pesquisa/dados/rodada-*/results.jsonl.
2. Deduplicar preservando a origem.
3. Confirmar metadados e URL.
4. Classificar a natureza da fonte.
5. Extrair afirmações sobre nível, flutuador, pressão, válvulas, sifão, engrenagens, indicador e compensação sazonal.
6. Registrar a evidência que sustenta cada afirmação.
7. Procurar evidência contraditória.
8. Atribuir confiança com justificativa.
9. Produzir pesquisa/relatorios/RELATORIO_VALIDACAO_V1.md.

## Regra

Resultado encontrado pelo coletor = candidato. Não é fato validado.

Trilha obrigatória: consulta → provedor → URL → documento → afirmação → evidência → classificação.

## Próxima etapa já preparada

Após a validação, executar a síntese técnica e reconstrução comparativa em pesquisa/sintese/.
