# Proposta Inicial do Jogo: Pong Arena PUC

O grupo pretende desenvolver um jogo inspirado no clássico Pong utilizando Python e a biblioteca Pygame. O jogo será composto por duas barras controladas pelos jogadores e uma bola que se movimenta pela tela. O objetivo é rebater a bola e impedir que ela ultrapasse a área de defesa do jogador, enquanto se tenta marcar pontos no adversário.

A proposta foi escolhida por apresentar um escopo viável para o tempo disponível do projeto, permitindo a aplicação de conceitos fundamentais de programação, como movimentação de objetos, detecção de colisões, controle de eventos do teclado, sistema de pontuação e organização modular do código.

## 1. Integrantes do grupo
- Anderson José Rodrigues Leal
- Kauã Rodrigues da Silva
- Maria Eduarda Madeira Santana
- Thales Pereira Leite

## 2. Tipo de jogo e Descrição geral
**Pong.** Dois jogadores controlarão barras laterais na tela e deverão rebater uma bola que se movimenta continuamente. O objetivo é impedir que a bola ultrapasse sua área de defesa enquanto tenta marcar pontos no adversário.

## 3. Regras principais e Condição de vitória
- Cada jogador controla uma barra vertical.
- A bola deve ser rebatida pelas barras.
- Quando a bola ultrapassa uma barra, o adversário ganha um ponto.
- Após cada ponto, a bola retorna ao centro da tela.
- **Vitória/Encerramento:** O jogador vence ao alcançar 20 pontos antes do adversário.

## 4. Controles previstos
- **Jogador 1:** W e S (mover para cima e para baixo).
- **Jogador 2:** Setas para cima e para baixo.
- **Sair:** Tecla ESC.

## 5. Escopo mínimo e Melhorias (Planejamento)
- **Mínimo:** Barras controladas pelo teclado, bola em movimento, sistema de colisão, placar funcional e tela de fim de partida.
- **Melhorias alcançadas:** Uso de estruturas de dados (Dicionários), leitura/escrita em arquivos (`historico.txt`), testes automatizados (`pytest`) e implementação de efeitos sonoros com reinício aleatório de direção.