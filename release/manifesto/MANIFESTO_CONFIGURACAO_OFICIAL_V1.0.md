# MANIFESTO DA CONFIGURAÇÃO OFICIAL V1.0

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Arquivo:** `release/manifesto/MANIFESTO_CONFIGURACAO_OFICIAL_V1.0.md`  
**Versão documental:** V1.0  
**Data de criação:** 27/09/2026  
**Estado:** PRÉ-MANIFESTO / CONFIGURAÇÃO CANDIDATA  

---

## 1. FINALIDADE

Este documento estabelece o modelo do Manifesto da Configuração Oficial V1.0 e prepara o fechamento formal da primeira configuração do projeto.

**Importante:** este manifesto não inventa resultados de calibração, validação, auditoria, reprodução ou desempenho. Campos que dependem de ensaios ou artefatos ainda não registrados permanecem explicitamente como `PENDENTE`.

## 2. IDENTIDADE DO PROJETO

| Campo | Estado |
|---|---|
| PROJECT-ID | `CTESIBIO` |
| Projeto | Relógio de Água de Ctesíbio |
| Repositório | `carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO` |
| Configuração | `CONFIG-1.0-CANDIDATA` |
| Release | `CTESIBIO-REL-1.0.0-CANDIDATA` |
| Estado | `PRÉ-RELEASE` |
| Data do manifesto | `27/09/2026` |
| Commit de referência do manifesto | preenchido no histórico Git após criação |

## 3. ESCOPO DA CONFIGURAÇÃO

A configuração candidata consolida a arquitetura documental desenvolvida nas Etapas 1–18, incluindo:

- pesquisa histórica;
- síntese histórica/reconstrutiva/projetual;
- modelo matemático;
- arquitetura física;
- BOM;
- fabricação e montagem;
- comissionamento;
- calibração;
- compensação sazonal;
- ciclo automático;
- registro de dados;
- robustez e falhas;
- validação final;
- dossiê técnico;
- auditoria;
- reprodução independente;
- publicação e preservação.

## 4. MATRIZ DE CONFIGURAÇÃO

| Elemento | Versão/ID | Estado |
|---|---|---|
| Governança | V1 | REGISTRADA |
| Pesquisa | V1 | REGISTRADA |
| Síntese | V1 | REGISTRADA |
| Modelo matemático | Etapa 05 V1 | DOCUMENTADO |
| Arquitetura/BOM | Etapa 06 V1 | DOCUMENTADA |
| Fabricação/comissionamento | Etapa 07 V1 | DOCUMENTADA |
| Calibração | Etapa 08 V1 | PROCEDIMENTO DOCUMENTADO; RESULTADO REAL PENDENTE |
| Compensação sazonal | Etapa 09 V1 | MODELO DOCUMENTADO |
| Ciclo automático | Etapa 10 V1 | ARQUITETURA DOCUMENTADA |
| Integração/auditabilidade | Etapa 11 V1 | DOCUMENTADA |
| Robustez/falhas | Etapa 12 V1 | PLANO DOCUMENTADO |
| Validação final | Etapa 13 V1 | PROCEDIMENTO DOCUMENTADO; EXECUÇÃO PENDENTE |
| Dossiê técnico | Etapa 14 V1 | DOCUMENTADO |
| Auditoria final | Etapa 15 V1 | PROCEDIMENTO DOCUMENTADO; AUDITORIA FORMAL PENDENTE |
| Reprodução/demonstração | Etapa 16 V1 | PACOTE ESPECIFICADO |
| Publicação/arquivo | Etapa 17 V1 | ESTRUTURA ESPECIFICADA |
| Encerramento/evolução | Etapa 18 V1 | DOCUMENTADO |

## 5. CONFIGURAÇÃO TÉCNICA

### 5.1 Hidráulica

Princípio de referência:

`ALIMENTAÇÃO → PRÉ-REGULAÇÃO → RESERVATÓRIO DE NÍVEL CONSTANTE → SAÍDA CONTROLADA`

Objetivo: reduzir a influência da variação de carga hidráulica sobre a vazão de medição.

### 5.2 Medição

`NÍVEL → FLUTUADOR → TRANSMISSÃO → INDICADOR → REGISTRO`

### 5.3 Compensação temporal

`REFERÊNCIA TEMPORAL → MODELO SAZONAL → ESCALA/ATUADOR → INDICAÇÃO`

### 5.4 Ciclo automático

`LIMITE → DESCARGA → RESET → RECUPERAÇÃO → VERIFICAÇÃO → NOVO CICLO`

## 6. CAMADAS DE IDENTIDADE

A configuração oficial deverá identificar separadamente:

- hardware;
- hidráulica;
- mecânica;
- instrumentação;
- firmware;
- software;
- modelo matemático;
- modelo sazonal;
- calibração;
- validação;
- auditoria;
- dados.

## 7. EVIDÊNCIA HISTÓRICA

A configuração moderna não deve ser interpretada como prova de que todos os detalhes do mecanismo antigo foram determinados.

As afirmações deverão continuar classificadas como:

- HISTÓRICO;
- INTERPRETAÇÃO;
- RECONSTRUÇÃO;
- PROPOSTA MODERNA;
- HIPÓTESE;
- NÃO DETERMINADO.

## 8. STATUS METROLÓGICO

**Estado atual:** `PENDENTE DE EXECUÇÃO EXPERIMENTAL`.

O manifesto não atribui valor de erro, incerteza, repetibilidade, exatidão ou deriva sem dados experimentais correspondentes.

Campos a preencher após ensaios:

- erro máximo;
- erro médio;
- incerteza expandida;
- repetibilidade;
- reprodutibilidade;
- deriva;
- influência térmica;
- estabilidade hidráulica;
- tempo de ciclo;
- tempo de descarga;
- tempo de reset.

## 9. STATUS DE VALIDAÇÃO

**Estado:** `PENDENTE DE EXECUÇÃO`.

A validação deverá demonstrar, por dados, os critérios definidos nas Etapas 8, 10, 11, 12 e 13.

## 10. STATUS DE AUDITORIA

**Estado:** `PENDENTE DE AUDITORIA FORMAL`.

A Etapa 15 define o procedimento e os critérios. A existência do procedimento não equivale à conclusão da auditoria.

## 11. STATUS DE REPRODUÇÃO

**Estado:** `PACOTE ESPECIFICADO / REPRODUÇÃO NÃO DEMONSTRADA`.

A reprodução independente deverá ser registrada somente após fabricação, calibração, testes e comparação com critérios quantitativos.

## 12. STATUS DE PUBLICAÇÃO

**Estado:** `PRÉ-PUBLICAÇÃO`.

A publicação final dependerá da conclusão das validações e da auditoria e deverá conservar as limitações encontradas.

## 13. CRITÉRIOS PARA CONVERTER EM RELEASE OFICIAL

O estado `CONFIG-1.0-CANDIDATA` somente poderá ser promovido para `CTESIBIO-REL-1.0.0` quando houver:

1. configuração física identificada;
2. BOM final;
3. desenhos finais;
4. calibração executada;
5. validação executada;
6. dados brutos preservados;
7. auditoria concluída;
8. segurança aprovada;
9. pacote de reprodução fechado;
10. manifesto final preenchido;
11. hashes calculados;
12. changelog registrado.

## 14. BLOQUEADORES ATUAIS

No momento da criação deste documento, os seguintes itens permanecem dependentes de evidência operacional real:

- ensaios físicos;
- resultados de calibração;
- resultados de validação;
- ensaios de robustez;
- reprodução independente;
- auditoria formal da configuração física;
- hashes do pacote final de release;
- identificação definitiva do commit de release.

Esses itens são bloqueadores de `RELEASE OFICIAL`, não de desenvolvimento documental.

## 15. REGRA DE INTEGRIDADE

É proibido preencher os campos acima com valores estimados apresentados como resultados medidos.

Valores de planejamento deverão ser marcados como:

`META`, `LIMITE DE PROJETO`, `ESTIMATIVA` ou `CRITÉRIO PROPOSTO`.

Resultados medidos deverão ser marcados como:

`RESULTADO EXPERIMENTAL`.

## 16. PROMOÇÃO DE ESTADO

```text
CONFIG-1.0-CANDIDATA
        ↓
EXECUÇÃO EXPERIMENTAL
        ↓
CALIBRAÇÃO
        ↓
VALIDAÇÃO
        ↓
AUDITORIA
        ↓
REPRODUÇÃO
        ↓
MANIFESTO COMPLETO
        ↓
CTESIBIO-REL-1.0.0
        ↓
PUBLICADO
        ↓
ARQUIVADO
```

## 17. CONTROLE DE MUDANÇA

Qualquer alteração que modifique a configuração física, hidráulica, mecânica, metrológica, de controle ou de processamento deverá criar nova configuração ou nova versão conforme a matriz definida na Etapa 18.

## 18. ASSINATURA DOCUMENTAL

### Preparado

Projeto: RELÓGIO DE ÁGUA DE CTESÍBIO  
Estado: configuração candidata  
Data: 27/09/2026

### Aprovação técnica

`PENDENTE`

### Aprovação metrológica

`PENDENTE`

### Auditoria final

`PENDENTE`

### Release oficial

`PENDENTE`

## 19. RESULTADO DESTE MANIFESTO

Este arquivo cria a identidade documental da configuração candidata e impede que a configuração seja chamada de release oficial antes da existência das evidências correspondentes.

A próxima ação técnica deverá ser preencher os campos pendentes somente com resultados verificáveis e, depois, gerar o manifesto definitivo da release.
