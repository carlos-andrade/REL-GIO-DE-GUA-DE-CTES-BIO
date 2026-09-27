# Relógio de Água de Ctesíbio — Fundamentação Histórica e Princípio de Engenharia

**Projeto:** RELÓGIO DE ÁGUA DE CTESÍBIO  
**Repositório:** carlos-andrade/REL-GIO-DE-GUA-DE-CTES-BIO  
**Data de criação:** 27/09/2026  
**Status:** Documento inicial de referência

## 1. O que foi o relógio de água de Ctesíbio

O relógio de água de Ctesíbio, ou clepsidra de Ctesíbio, foi um instrumento hidráulico desenvolvido em Alexandria, no Egito helenístico, por volta do século III a.C., associado ao inventor e engenheiro grego Ctesíbio.

Seu objetivo era medir a passagem do tempo utilizando o movimento controlado da água e mecanismos mecânicos de indicação.

## 2. O problema das clepsidras tradicionais

Em uma clepsidra simples, a água escoa por uma abertura. À medida que o nível da água diminui, a pressão hidrostática sobre a abertura também diminui.

A relação básica é:

P = rho × g × h

onde:

- P = pressão hidrostática;
- rho = densidade do fluido;
- g = aceleração da gravidade;
- h = altura da coluna de água.

Como h varia, a pressão e a vazão também variam. Isso introduz erro na relação entre volume escoado e tempo.

## 3. A inovação associada a Ctesíbio

A solução de engenharia atribuída ao sistema de Ctesíbio consistia em controlar a alimentação hidráulica de forma que o nível de água relevante para a medição permanecesse aproximadamente constante.

O princípio pode ser resumido:

nível controlado → pressão mais estável → vazão mais previsível → medição temporal mais regular.

Esse é o princípio central que deve ser preservado no projeto moderno.

## 4. Elementos funcionais

Uma arquitetura conceitual inclui:

1. reservatório de alimentação;
2. mecanismo de controle de nível/fluxo;
3. reservatório de medição;
4. flutuador;
5. elemento mecânico de transmissão;
6. indicador;
7. escala temporal;
8. mecanismo de descarga/reinicialização;
9. mecanismo de atualização da escala;
10. calibração e referência temporal.

## 5. Flutuador e indicação

O flutuador transforma a variação do nível da água em deslocamento mecânico.

Esse deslocamento pode ser transmitido por haste, corda, engrenagens ou outro mecanismo para produzir uma indicação contínua do tempo.

## 6. Ciclo automático

O conceito moderno de operação é:

1. alimentação controlada;
2. aumento progressivo do nível;
3. deslocamento do flutuador;
4. transmissão do deslocamento;
5. indicação temporal;
6. atingimento do limite operacional;
7. descarga automática;
8. reinicialização;
9. atualização da escala ou do estado;
10. repetição do ciclo.

## 7. Compensação sazonal

Os sistemas históricos de medição temporal podiam considerar a variação sazonal da duração dos períodos diurno e noturno.

No projeto moderno, essa função deve ser tratada como uma camada explícita de calibração, e não como uma característica implícita do mecanismo hidráulico.

## 8. Princípio de engenharia para o projeto moderno

A principal lição de Ctesíbio não é simplesmente utilizar água para medir tempo.

É controlar uma variável física que introduz erro antes de utilizá-la como referência de medição.

Arquitetura abstrata:

VARIÁVEL FÍSICA
↓
SENSOR / FLUTUADOR
↓
CONTROLE
↓
ESTADO ESTÁVEL
↓
MEDIÇÃO
↓
CALIBRAÇÃO
↓
CORREÇÃO
↓
REGISTRO AUDITÁVEL

## 9. Diretriz do projeto

O sistema moderno inspirado em Ctesíbio deverá priorizar:

- precisão;
- estabilidade hidráulica;
- repetibilidade;
- robustez;
- calibração rastreável;
- tolerâncias documentadas;
- segurança;
- manutenção previsível;
- registro dos ciclos;
- auditabilidade.

## 10. Observação histórica

Reconstruções modernas de mecanismos antigos podem divergir quanto a detalhes específicos da configuração original. Portanto, o projeto deve distinguir claramente entre:

- fatos historicamente documentados;
- reconstruções arqueológicas;
- interpretações de engenharia;
- soluções modernas inspiradas no princípio histórico.

Esta distinção será mantida em toda a documentação do projeto.
