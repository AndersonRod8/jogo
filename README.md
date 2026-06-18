# Proposta Inicial do Jogo

O grupo pretende desenvolver um jogo inspirado no clássico Pong utilizando Python e a biblioteca Pygame. O jogo será composto por duas barras controladas pelos jogadores e uma bola que se movimenta pela tela. O objetivo é rebater a bola e impedir que ela ultrapasse a área de defesa do jogador, enquanto se tenta marcar pontos no adversário.

A proposta foi escolhida por apresentar um escopo viável para o tempo disponível do projeto, permitindo a aplicação de conceitos fundamentais de programação, como movimentação de objetos, detecção de colisões, controle de eventos do teclado, sistema de pontuação e organização modular do código.

Inicialmente, o jogo contará com um modo para dois jogadores, placar em tempo real e tela de encerramento ao final da partida. Caso haja tempo disponível, poderão ser adicionados recursos extras, como efeitos sonoros, menu inicial, aumento progressivo da dificuldade e melhorias visuais.


## 1. Nome do jogo

Pong Arena PUC

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Anderson José Rodrigues Leal
- Kauã Rodrigues da Silva
- Maria Eduarda Madeira Santana
- Thales Pereira Leite

## 3. Tipo de jogo

> Pong

## 4. Descrição geral do jogo

> O jogo será baseado no clássico Pong. Dois jogadores controlarão barras laterais na tela e deverão rebater uma bola que se movimenta continuamente. O objetivo é impedir que a bola ultrapasse sua área de defesa enquanto tenta marcar pontos no adversário. A velocidade da bola pode aumentar ao longo da partida, tornando o jogo mais desafiador.

## 5. Objetivo do jogador

> Marcar mais pontos que o adversário ao fazer a bola ultrapassar a barra de defesa do oponente.

## 6. Regras principais

- Regra 1: Cada jogador controla uma barra vertical.
- Regra 2: A bola deve ser rebatida pelas barras.
- Regra 3: Quando a bola ultrapassa uma barra, o adversário ganha um ponto.
- Regra 4: Após cada ponto, a bola retorna ao centro da tela.
- Regra 5: Vence o jogador que atingir a pontuação definida primeiro.

## 7. Condição de vitória

> O jogador vence ao alcançar 10 pontos antes do adversário.

## 8. Condição de derrota ou encerramento

> A partida termina quando um dos jogadores atingir a pontuação máxima estabelecida para a vitória.

## 9. Elementos previstos no jogo

Duas barras verticais controladas pelos jogadores através do teclado.

## Jogador ou elemento principal

> Duas barras verticais controladas pelos jogadores através do teclado.

## Obstáculos, inimigos ou desafios

> O principal desafio será acompanhar o movimento da bola e reagir rapidamente para impedir que ela ultrapasse a barra de defesa.

## Itens, alvos ou objetos de interação

> A bola é o principal objeto de interação, quicando nas barras e nas bordas superior e inferior da tela.

## Pontuação, vidas, tempo ou progresso

> Cada vez que um jogador marca um ponto, sua pontuação aumenta em uma unidade. O placar ficará visível durante toda a partida.

## 10. Controles previstos

Controles do grupo:

- W e S: mover a barra do jogador 1 para cima e para baixo.
- Seta: Seta para cima e seta para baixo, mover a barra do jogador 2.
- ESC: sair do jogo.

## 11. Organização inicial do código

Organização planejada.

>

- `main.py`: inicia o jogo e executa o loop principal;
- `src/jogo.py`: controla a movimentação e colisões da bola;
- `src/config.py`: controla as barras dos jogadores;
- `src/funcoes.py`: armazena configurações como tamanho da tela, cores e velocidade;
- `src/dados.py`: gerencia a pontuação e exibição do placar.

## 12. Recursos externos previstos

> Pretendemos utilizar sons gratuitos para colisões e pontuação, além de tutoriais como referência para implementação de funcionalidades no Pygame.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Implementar corretamente as colisões entre a bola e as barras.
- Dificuldade 2: Controlar a movimentação da bola de forma fluida.
- Dificuldade 3: Organizar o código e integrar as diferentes partes do projeto.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá duas barras controladas pelo teclado, uma bola em movimento, sistema de colisão, placar funcional e tela de fim de partida quando um jogador atingir a pontuação necessária para vencer.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Menu inicial e tela de pausa.
- Melhoria 2: Aumento gradual da velocidade da bola durante a partida.
- Melhoria 3: Efeitos sonoros e elementos visuais mais elaborados.
