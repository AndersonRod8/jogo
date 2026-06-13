# Pong Arena PUC 

O **Pong Arena PUC** é um jogo inspirado no clássico Pong, desenvolvido em Python utilizando a biblioteca Pygame. O projeto foi elaborado como trabalho prático, permitindo a aplicação de conceitos fundamentais de programação, como movimentação de objetos, detecção de colisões, controle de eventos do teclado, sistema de pontuação, uso de estruturas de dados e organização modular do código.

## Integrantes do Grupo
* Anderson José Rodrigues Leal
* Kauã Rodrigues da Silva
* Maria Eduarda Madeira Santana
* Thales Pereira Leite

---

## Descrição Geral do Jogo
Dois jogadores controlam barras laterais na tela e devem rebater uma bola que se movimenta continuamente. O objetivo é impedir que a bola ultrapasse sua área de defesa enquanto tenta marcar pontos no adversário. 

**Objetivo do Jogador:** Marcar mais pontos que o adversário ao fazer a bola ultrapassar a barra de defesa do oponente.

### Regras Principais
1. Cada jogador controla uma barra vertical.
2. A bola deve ser rebatida pelas barras.
3. Quando a bola ultrapassa uma barra, o adversário ganha um ponto.
4. Após cada ponto, a bola retorna ao centro da tela.
5. Vence o jogador que atingir a pontuação definida primeiro.

###  Condições de Vitória e Encerramento
* **Vitória:** O jogador vence ao alcançar **20 pontos** antes do adversário.
* **Encerramento:** A partida termina quando um dos jogadores atinge a pontuação máxima, exibindo a tela de fim de jogo e salvando os resultados da partida de forma persistente.

---

## Controles
* **Jogador 1 (Esquerda):** Teclas `W` (Cima) e `S` (Baixo)
* **Jogador 2 (Direita):** Setas Direcionais `↑` (Cima) e `↓` (Baixo)
* **Sair do Jogo:** Tecla `ESC`

---

##  Elementos do Jogo
* **Jogadores (Elementos Principais):** Duas barras verticais controladas através do teclado.
* **Objeto de Interação:** A bola, que quica nas barras e nas bordas superior e inferior da tela.
* **Desafio:** Acompanhar o movimento da bola e reagir rapidamente para impedir que ela ultrapasse a barra de defesa.
* **Progresso e Dados:** O placar fica visível durante toda a partida em tempo real. Ao final, o histórico do vencedor e a pontuação são gravados no arquivo `historico.txt`.

---

## 📂 Organização do Código
O código foi estruturado de forma modular para facilitar a manutenção e aplicação de testes:

* `main.py`: Inicia o jogo, executa o loop principal e gerencia a condição de vitória.
* `src/jogo.py`: Controla a movimentação e a física de colisões da bola.
* `src/config.py`: Controla a movimentação das barras dos jogadores.
* `src/funcoes.py`: Armazena configurações globais como tamanho da tela, cores e velocidade (FPS).
* `src/dados.py`: Gerencia a pontuação, exibição do placar e salvamento em arquivo usando Dicionários.
* `src/sprites.py`: Responsável por desenhar os elementos visuais na tela.
* `tests/test_logica.py`: Testes automatizados da lógica de pontuação usando `pytest`.

---

