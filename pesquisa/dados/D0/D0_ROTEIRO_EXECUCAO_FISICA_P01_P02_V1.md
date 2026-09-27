# D0 — Roteiro de Execução Física P01/P02 V1

**Projeto:** Relógio de Água de Ctesíbio  
**Repositório:** carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO  
**Fase:** D0 — Geometria e volume de referência  
**Procedimentos:** D0-P01 — levantamento geométrico; D0-P02 — relação H↔V  
**Estado:** PREPARADO — execução física ainda não realizada

## 1. Objetivo

Fornecer uma sequência operacional única para a coleta dos dados físicos D0, preservando rastreabilidade e impedindo que estimativas sejam confundidas com medições.

## 2. Pré-condições

Antes de iniciar:

- identificar o protótipo e seus componentes;
- verificar estabilidade mecânica;
- limpar e inspecionar superfícies relevantes;
- identificar todos os instrumentos;
- registrar instrumento, resolução e condição metrológica;
- registrar temperatura ambiente e do fluido;
- nivelar ou documentar a condição da estrutura;
- fotografar a configuração inicial;
- abrir novo registro de sessão de medição.

Se qualquer pré-condição crítica não for atendida, registrar **BLOQUEADO** e não iniciar a coleta.

## 3. P01 — Levantamento geométrico

### P01.1 Altura

Medir a altura relevante de cada reservatório ou referência geométrica.

Executar pelo menos 3 repetições independentes quando o método permitir.

Registrar:

- ID da medição;
- ponto de referência;
- instrumento;
- repetição;
- valor bruto;
- unidade;
- temperatura;
- data/hora;
- observação.

### P01.2 Diâmetro ou dimensões lineares

Para seção circular:

- medir diâmetro em posições/orientações distintas;
- evitar assumir circularidade perfeita;
- registrar cada leitura.

Para seção não circular:

- medir as dimensões necessárias para caracterizar a seção;
- registrar explicitamente a geometria observada.

### P01.3 Níveis de referência

Definir fisicamente:

- nível inferior útil;
- nível de operação;
- nível superior;
- nível de descarga;
- nível de transbordamento, se existente.

Cada nível deve possuir referência física identificável.

## 4. P02 — Relação H↔V

### P02.1 Preparação

1. Colocar o reservatório em condição inicial definida.
2. Registrar o nível inicial.
3. Registrar temperatura.
4. Confirmar instrumento de volume ou método gravimétrico.
5. Definir incrementos de nível antes da coleta.

### P02.2 Coleta incremental

Para cada ponto:

1. adicionar volume conhecido;
2. aguardar estabilização;
3. determinar o nível H;
4. registrar o volume acumulado V;
5. registrar repetição e condições;
6. fotografar pontos críticos quando útil.

Não corrigir visualmente um valor durante a coleta sem preservar o valor original.

### P02.3 Faixa de pontos

A faixa deverá cobrir toda a região útil do reservatório.

Os incrementos devem ser suficientemente pequenos para revelar mudanças de geometria ou não linearidades relevantes.

O número final de pontos será definido conforme a geometria real e a resolução do método.

## 5. Repetições

Para grandezas críticas:

- mínimo recomendado: 3 repetições;
- aumentar repetições quando a dispersão indicar necessidade;
- registrar todas as leituras, inclusive anômalas;
- não descartar outlier sem investigação documentada.

## 6. Condições ambientais

Registrar, quando aplicável:

- temperatura;
- pressão ambiente;
- fluido utilizado;
- condição da bancada;
- inclinação;
- estado do reservatório;
- operador;
- data/hora.

## 7. Encerramento da sessão

Ao terminar:

1. verificar se todos os IDs estão presentes;
2. verificar unidades;
3. conferir registros contra anotações originais;
4. registrar ocorrências;
5. preservar o arquivo bruto;
6. registrar a identificação da sessão;
7. impedir processamento sobre o arquivo original.

## 8. Critérios de parada

Interromper a coleta se ocorrer:

- vazamento;
- deformação ou deslocamento do reservatório;
- falha de instrumento;
- leitura não reproduzível;
- alteração não controlada do nível;
- contaminação significativa;
- condição de segurança inadequada.

Registrar o motivo e o último ponto válido.

## 9. Resultado esperado

A execução deverá produzir:

- dados geométricos brutos;
- dados H↔V brutos;
- identificação dos instrumentos;
- condições ambientais;
- registros de repetição;
- ocorrências e anomalias;
- evidência fotográfica quando aplicável.

## 10. Estado de execução

**ATUAL:** roteiro preparado.  
**EXECUÇÃO:** NÃO REALIZADA.  
**DADOS EXPERIMENTAIS:** NÃO DISPONÍVEIS.  
**PRÓXIMO ESTADO:** D0-COLETA.

Nenhum resultado de medição deve ser declarado antes da execução física e do registro dos dados brutos.
