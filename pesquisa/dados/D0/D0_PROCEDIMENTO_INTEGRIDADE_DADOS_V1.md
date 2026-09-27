# D0 — Procedimento de Integridade dos Dados V1

**Projeto:** Relógio de Água de Ctesíbio  
**Repositório:** carlos-andrade/RELOGIO_DE_AGUA_DE_CTESIBIO  
**Fase:** D0 — Geometria e volume de referência  
**Estado:** PREPARADO — aguardando dados físicos

## Objetivo

Garantir que os dados brutos coletados possam ser identificados, preservados e auditados sem substituição silenciosa, arredondamento indevido ou perda de rastreabilidade.

## 1. Regra de ouro

O arquivo bruto é evidência primária da medição D0.

Não alterar uma linha já coletada para corrigir um erro. Quando houver erro de registro:

1. preservar o valor original;
2. registrar a ocorrência;
3. criar correção identificável;
4. manter vínculo entre original e correção.

## 2. Identificação

Cada registro deverá possuir:

- ID único;
- data e hora;
- componente;
- grandeza;
- unidade;
- método;
- instrumento;
- repetição;
- valor bruto;
- observação;
- status.

## 3. Integridade

Antes do processamento:

- verificar existência do arquivo;
- verificar cabeçalho;
- verificar IDs únicos;
- verificar unidades;
- verificar campos obrigatórios;
- verificar valores ausentes;
- verificar duplicações;
- registrar a versão do arquivo.

Quando possível, calcular um hash do arquivo bruto e registrar o algoritmo utilizado.

## 4. Correções

Correções devem ser aditivas e rastreáveis. Não utilizar edição silenciosa do valor original.

Formato recomendado de ocorrência:

| Campo | Conteúdo |
|---|---|
| ocorrência_id | D0-ERR-XXXX |
| registro_original | ID do dado |
| problema | descrição |
| ação | correção adotada |
| novo_registro | ID, se houver |
| responsável | operador |
| data_hora | registro |
| justificativa | motivo |

## 5. Processamento

O processamento deverá consumir o arquivo bruto e gerar arquivo separado.

Fluxo:

`DADOS BRUTOS → VERIFICAÇÃO → PROCESSAMENTO → RESULTADOS → REVISÃO`

Os dados brutos não deverão ser sobrescritos pelo processamento.

## 6. Estados de integridade

- RECEBIDO
- VERIFICADO
- COM PENDÊNCIA
- CORRIGIDO COM RASTREABILIDADE
- LIBERADO PARA PROCESSAMENTO
- PROCESSADO
- REVISADO

## 7. Critério de auditoria

Um terceiro deverá conseguir responder:

> Qual medição originou este resultado?

e percorrer:

`RESULTADO → ID BRUTO → INSTRUMENTO → MÉTODO → DATA/HORA → CONDIÇÃO`

**Observação:** este procedimento define controle de dados; não constitui evidência experimental.
