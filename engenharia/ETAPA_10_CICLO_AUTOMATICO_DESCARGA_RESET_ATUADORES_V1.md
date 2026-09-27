# ETAPA 10 — CICLO AUTOMÁTICO, DESCARGA, RESET E ATUADORES V1

## 1. Objetivo

Validar o ciclo automático completo do sistema, desde o enchimento até a descarga, reinicialização e atualização da indicação, mantendo separadas as funções hidráulica, mecânica, eletrônica e de registro.

## 2. Máquina de estados

Estados oficiais:

INICIALIZAÇÃO
→ ENCHIMENTO
→ ESTABILIZAÇÃO
→ MEDIÇÃO
→ LIMITE_ATINGIDO
→ DESCARGA
→ RESET
→ RECUPERAÇÃO
→ VERIFICAÇÃO
→ PRONTO

Falha crítica em qualquer estado:

ESTADO_ATUAL → FALHA → MODO_SEGURO

## 3. Condições de transição

### ENCHIMENTO → ESTABILIZAÇÃO
Quando o nível entrar na faixa de referência.

### ESTABILIZAÇÃO → MEDIÇÃO
Quando a variação de nível permanecer abaixo do limite definido durante o tempo mínimo de estabilização.

### MEDIÇÃO → LIMITE_ATINGIDO
Quando o nível ou posição atingir o limiar configurado.

### LIMITE_ATINGIDO → DESCARGA
Após validação do evento e confirmação de que a descarga pode ocorrer com segurança.

### DESCARGA → RESET
Quando o nível atingir o limite inferior ou o evento de descarga terminar.

### RESET → RECUPERAÇÃO
Quando a escala, engrenagem ou atuador estiver na posição inicial validada.

### RECUPERAÇÃO → VERIFICAÇÃO
Quando o nível retornar à faixa operacional.

### VERIFICAÇÃO → PRONTO
Quando todas as condições de integridade forem satisfeitas.

## 4. Detecção do limite

O disparo não deve depender exclusivamente de uma única observação instantânea quando isso puder gerar falsos eventos.

Métodos possíveis:
- posição mecânica;
- sensor de nível;
- sensor de posição;
- combinação de sensores;
- confirmação temporal do estado.

Registrar:
- valor de disparo;
- timestamp;
- sensor responsável;
- valor antes/depois;
- estado anterior.

## 5. Acionamento da descarga

O mecanismo deve possuir:
- ponto de disparo definido;
- energia suficiente para completar o ciclo;
- retorno previsível;
- proteção contra acionamento repetido;
- inspeção e limpeza;
- drenagem segura.

O sifão ou atuador equivalente deve ser caracterizado experimentalmente quanto a:
- tempo de acionamento;
- vazão;
- volume descarregado;
- nível final;
- repetibilidade;
- sensibilidade à geometria.

## 6. Reset

O reset deve restabelecer uma condição conhecida.

Variáveis:
- posição inicial;
- nível inicial;
- posição da escala;
- estado do atuador;
- número do ciclo.

O reset não deve depender de intervenção manual em operação normal.

## 7. Atuadores

Podem ser utilizados:
- mecanismo puramente hidráulico;
- mola;
- engrenagem;
- came;
- motor de baixa potência;
- servo;
- solenóide;
- atuador linear.

A seleção deve considerar:
- força;
- curso;
- precisão;
- repetibilidade;
- consumo;
- desgaste;
- segurança;
- facilidade de manutenção;
- possibilidade de operação manual de emergência.

## 8. Intertravamentos

Implementar, conforme arquitetura:
- bloqueio de descarga com reservatório fora da condição segura;
- bloqueio de acionamento repetido;
- detecção de curso incompleto;
- limite de nível;
- proteção contra overflow;
- timeout de estados;
- detecção de sensor inválido.

Exemplo:

TIMEOUT_DESCARGA → PARAR_ATUADOR → REGISTRAR_FALHA → MODO_SEGURO

## 9. Timeout

Cada estado automático deve possuir tempo máximo esperado.

Se excedido:

ESTADO → TIMEOUT → FALHA_CONTROLADA

O timeout não deve simplesmente reiniciar o sistema sem registrar a causa.

## 10. Detecção de falhas

Falhas mínimas a testar:
- sensor desconectado;
- sensor congelado;
- leitura fora de faixa;
- descarga incompleta;
- descarga excessiva;
- atuador travado;
- flutuador travado;
- perda de alimentação;
- overflow;
- perda de comunicação;
- reinicialização durante ciclo;
- alteração indevida de parâmetro.

## 11. Recuperação

A recuperação deve seguir:

DETECTAR
→ ISOLAR
→ PRESERVAR DADOS
→ COLOCAR EM ESTADO SEGURO
→ IDENTIFICAR CAUSA
→ CORRIGIR
→ REINICIAR
→ VERIFICAR
→ LIBERAR

Não apagar o estado anterior sem registrar o evento.

## 12. Registro de ciclo

Cada ciclo deve receber identificador único.

Campos mínimos:
- cycle_id;
- início;
- fim;
- duração;
- nível inicial;
- nível de disparo;
- duração da descarga;
- nível final;
- estado final;
- eventos;
- falhas;
- versão de configuração;
- versão de firmware/software.

## 13. Atualização da escala

Quando houver atuador mecânico ou digital, a atualização deve ocorrer somente após confirmação de conclusão do ciclo hidráulico.

Sequência:

DESCARGA CONCLUÍDA
→ CONFIRMAR NÍVEL
→ ACIONAR ATUADOR
→ CONFIRMAR POSIÇÃO
→ REGISTRAR NOVA ESCALA
→ LIBERAR NOVO CICLO

Isso evita que uma escala seja atualizada antes de o sistema realmente ter reiniciado.

## 14. Testes

### A10-01 — ciclo nominal
Executar ciclo completo em condições normais.

### A10-02 — ciclos repetidos
Executar série de ciclos e verificar acumulação de erro.

### A10-03 — descarga incompleta
Interromper/controlar a descarga e verificar detecção.

### A10-04 — atuador travado
Impedir movimento e verificar timeout.

### A10-05 — sensor inválido
Fornecer condição inválida e verificar bloqueio.

### A10-06 — perda de energia
Interromper alimentação em estados diferentes.

### A10-07 — overflow
Simular condição de proteção.

### A10-08 — reinicialização
Reiniciar o controlador durante um ciclo e verificar recuperação segura.

## 15. Critérios de aceitação

Definir antes dos ensaios:
- tolerância do nível de disparo;
- tolerância do nível de reset;
- duração máxima da descarga;
- duração máxima do reset;
- taxa máxima de ciclos incompletos;
- tempo máximo de recuperação;
- erro máximo acumulado por ciclo;
- taxa máxima de falsos disparos;
- taxa máxima de falhas não detectadas.

## 16. Análise de repetibilidade

Após série de ciclos, comparar:
- nível de disparo;
- volume descarregado;
- nível final;
- posição de reset;
- duração;
- erro de indicação.

Avaliar tendência de desgaste ou deriva.

## 17. Segurança funcional

A prioridade em qualquer falha deve ser:

1. impedir transbordamento;
2. impedir movimento perigoso;
3. proteger eletrônica;
4. preservar dados;
5. manter condição recuperável.

A indicação temporal não deve prevalecer sobre a segurança física.

## 18. Comparação com o princípio histórico

| Princípio histórico | Implementação moderna |
|---|---|
| Sifão/descarga automática | Sifão caracterizado ou atuador equivalente |
| Reinício do ciclo | Reset hidráulico/mecânico controlado |
| Engrenagens | Engrenagem, came, motor ou software |
| Atualização da escala | Atuador mecânico ou atualização digital |
| Ciclo periódico | Máquina de estados auditável |
| Controle físico | Intertravamentos e sensores |

As soluções modernas são equivalentes funcionais, não afirmações de reprodução arqueológica literal.

## 19. Liberação para Etapa 11

A etapa será liberada somente quando:
- ciclo completo comprovado;
- descarga repetível;
- reset repetível;
- falhas críticas detectadas;
- recuperação segura;
- registros completos;
- atuadores caracterizados;
- parâmetros congelados;
- testes de segurança aprovados.

## 20. Próxima etapa

### ETAPA 11 — INTEGRAÇÃO DO SISTEMA, REGISTRO DE DADOS E AUDITABILIDADE

Objetivo: consolidar hidráulica, mecânica, instrumentação, controle, compensação e registro em uma arquitetura integrada, com trilha de auditoria capaz de reconstruir qualquer ciclo experimental.
