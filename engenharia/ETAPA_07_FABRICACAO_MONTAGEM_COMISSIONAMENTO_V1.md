# ETAPA 07 — FABRICAÇÃO, MONTAGEM E COMISSIONAMENTO V1

## 1. Objetivo

Transformar a arquitetura física da Etapa 6 em um protótipo montado, inspecionado, estanque, funcional e documentado, sem confundir aceitação da montagem com validação metrológica.

**Regra:** a conclusão desta etapa libera o sistema para calibração; não declara que o relógio já atingiu a precisão final de projeto.

## 2. Sequência controlada

1. Conferência da BOM e versões dos desenhos.
2. Inspeção de recebimento dos componentes.
3. Verificação dimensional.
4. Limpeza e preparação.
5. Fabricação das peças customizadas.
6. Montagem hidráulica.
7. Montagem mecânica.
8. Instalação dos sensores e aquisição.
9. Integração elétrica e de dados.
10. Teste de estanqueidade.
11. Teste de enchimento estático.
12. Teste de fluxo controlado.
13. Teste de liberdade do flutuador.
14. Teste de descarga e reinicialização.
15. Teste de overflow e drenagem de segurança.
16. Comissionamento instrumentado.
17. Registro de não conformidades.
18. Congelamento da configuração de referência.
19. Liberação para a Etapa 8.

## 3. Inspeção de recebimento

Para cada componente registrar:
- código;
- descrição;
- fabricante;
- modelo;
- lote ou número de série, quando existir;
- material;
- dimensão nominal;
- quantidade;
- estado físico;
- documentação técnica;
- certificado de calibração, quando aplicável;
- versão/desenho associado.

Componentes críticos sem identificação ou com documentação incompatível devem ficar **BLOQUEADOS** até análise.

## 4. Controle dimensional

Inspecionar, no mínimo:
- geometria do reservatório;
- posição e altura das conexões;
- curso do flutuador;
- verticalidade das guias;
- alinhamento do eixo de transmissão;
- posição da escala;
- altura de disparo da descarga;
- posição do overflow;
- pontos de referência dos sensores.

Registrar dimensão nominal, dimensão medida, instrumento utilizado, resolução, tolerância e resultado.

## 5. Fabricação

Peças customizadas devem possuir:
- desenho ou especificação;
- material;
- processo de fabricação;
- tolerâncias;
- identificação da revisão;
- inspeção pós-fabricação.

Peças impressas em 3D não devem ser usadas em função crítica de estanqueidade ou segurança sem ensaio específico de adequação.

## 6. Montagem hidráulica

### 6.1 Princípios

- minimizar volume morto;
- evitar bolsões de ar;
- manter conexões acessíveis;
- impedir esforço mecânico sobre tubos frágeis;
- manter direção de fluxo identificada;
- permitir desmontagem para limpeza;
- manter descarga e overflow independentes quando possível.

### 6.2 Sequência

1. instalar reservatório;
2. instalar regulador;
3. instalar linhas de alimentação;
4. instalar reservatório de referência;
5. instalar overflow;
6. instalar descarga/sifão;
7. instalar dreno;
8. verificar conexões;
9. preencher lentamente;
10. eliminar ar aprisionado;
11. executar ensaio de estanqueidade.

## 7. Montagem mecânica

O flutuador deve:
- mover-se sem contato indevido;
- permanecer estável;
- não sofrer atrito significativo com a guia;
- retornar à posição prevista;
- transmitir movimento sem folga excessiva.

A transmissão deve ser alinhada antes de qualquer ensaio de medição.

Registrar:
- curso útil;
- folga;
- atrito observado;
- posição de zero;
- posição de referência;
- sentido de movimento;
- relação mecânica.

## 8. Instrumentação e aquisição

Instalar, no mínimo:
- referência independente de tempo;
- sensor de temperatura;
- medição de nível, direta ou indireta;
- registro do evento de descarga;
- aquisição sincronizada.

Cada canal deve possuir:
- identificador;
- unidade;
- resolução;
- frequência de aquisição;
- timestamp;
- versão de firmware/software;
- estado de validade.

## 9. Teste de estanqueidade

Procedimento:
1. preencher até nível de teste;
2. interromper a alimentação;
3. observar vazamentos;
4. registrar queda de nível;
5. inspecionar conexões;
6. corrigir não conformidades;
7. repetir o ensaio.

**Critério de aceitação:** nenhum vazamento visível em conexões ou reservatórios e perda residual compatível com a tolerância definida no protocolo de ensaio.

## 10. Teste de enchimento estático

Objetivo: verificar geometria, estabilidade e ausência de comportamento anômalo antes da aplicação de fluxo controlado.

Verificar:
- nível;
- estabilidade;
- deformação;
- overflow;
- flutuador;
- indicador;
- conexões;
- drenagem.

## 11. Teste de fluxo controlado

Executar pelo menos três condições:
- fluxo baixo;
- fluxo nominal;
- fluxo alto dentro da faixa de projeto.

Para cada condição registrar:
- Q_in;
- Q_out;
- nível;
- temperatura;
- tempo;
- estado do sistema.

O teste não deve prosseguir se o nível exceder o limite de segurança.

## 12. Teste do flutuador

Aplicar perturbações controladas e observar:
- tempo de retorno;
- histerese;
- travamento;
- oscilação;
- contato com guia;
- deslocamento do indicador.

Qualquer travamento mecânico reprova o ensaio até correção.

## 13. Teste de descarga e reinicialização

Verificar a sequência:

LIMITE_ATINGIDO → DESCARGA → NÍVEL_REDUZIDO → REINICIALIZAÇÃO → ESTABILIZAÇÃO

Registrar:
- nível de disparo;
- instante do disparo;
- duração da descarga;
- nível final;
- tempo de recuperação;
- número do ciclo;
- posição da escala/atuador após reset.

A descarga deve ocorrer de maneira repetível e sem gerar condição insegura.

## 14. Teste de overflow e proteção

Simular condição de alimentação acima do nominal, dentro dos limites seguros do protótipo.

Verificar:
- acionamento do overflow;
- contenção;
- drenagem;
- ausência de contato água/eletrônica;
- manutenção da estrutura estável.

O overflow é proteção secundária; não deve ser usado como controle normal do nível.

## 15. Comissionamento

Estados oficiais:

MONTAGEM
→ INSPEÇÃO
→ ESTANQUEIDADE
→ ENCHIMENTO
→ FLUXO_CONTROLADO
→ ESTABILIZAÇÃO
→ DESCARGA_TESTE
→ RESET_TESTE
→ COMISSIONADO

Qualquer falha crítica retorna o sistema para NÃO_CONFORME.

## 16. Checklist de segurança

Antes de cada série:
- reservatório fixado;
- base nivelada;
- contenção instalada;
- overflow livre;
- dreno disponível;
- conexões firmes;
- partes móveis protegidas;
- cabos afastados da água;
- alimentação elétrica protegida;
- procedimento de parada conhecido;
- volume máximo respeitado.

## 17. Não conformidades

Cada falha deve receber:
- ID;
- data;
- componente;
- condição do ensaio;
- descrição;
- evidência;
- risco;
- causa provável;
- ação corretiva;
- responsável;
- reteste;
- decisão final.

Classificação:
- **NC-C:** crítica — bloqueia o comissionamento;
- **NC-M:** maior — requer correção antes da próxima fase;
- **NC-m:** menor — pode ser acompanhada, desde que não afete segurança ou validade dos ensaios.

## 18. Evidências obrigatórias

O pacote de comissionamento deve conter:
- fotos da montagem;
- desenhos/revisões utilizadas;
- medições dimensionais;
- identificação dos componentes;
- registros de estanqueidade;
- dados brutos dos testes;
- logs de eventos;
- versões de firmware/software;
- certificados aplicáveis;
- lista de não conformidades;
- decisão de liberação.

## 19. Congelamento da configuração

Após aprovação:
- congelar BOM;
- congelar desenhos;
- congelar posições de sensores;
- congelar relações mecânicas;
- congelar parâmetros hidráulicos;
- identificar o protótipo;
- criar baseline de configuração.

Qualquer alteração posterior deve gerar nova revisão e novo registro de configuração.

## 20. Critérios de liberação para Etapa 8

O protótipo pode ser liberado para calibração somente se:
- não houver NC-C aberta;
- estanqueidade aprovada;
- overflow e drenagem funcionais;
- flutuador livre;
- descarga repetível;
- reinicialização funcional;
- aquisição de dados operacional;
- referência temporal disponível;
- configuração identificada;
- evidências do comissionamento arquivadas.

## 21. Distinção metrológica

**ACEITAÇÃO DA MONTAGEM:** o equipamento está fisicamente e funcionalmente apto para calibração.

**VALIDAÇÃO METROLÓGICA:** ainda não concluída nesta etapa.

A precisão final somente poderá ser declarada após calibração, ensaios de repetibilidade, análise de incerteza e validação definidos na Etapa 8.

## 22. Próxima etapa

### ETAPA 08 — CALIBRAÇÃO E VALIDAÇÃO METROLÓGICA

Objetivo: estabelecer a relação entre a indicação do sistema e uma referência independente, quantificar erro, repetibilidade, deriva, influência térmica e incerteza, e definir formalmente os critérios de aceitação.
