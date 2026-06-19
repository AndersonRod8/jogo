# Pong Arena PUC 🕹️

O **Pong Arena PUC** é um jogo inspirado no clássico Pong, desenvolvido em Python utilizando a biblioteca Pygame. O projeto foi elaborado como trabalho prático final, e sua proposta inicial completa pode ser lida em `docs/proposta.md`.

## 📌 Funcionalidades Implementadas (Jogo Completo e Executável)
* **Lógica e Colisão:** Movimentação fluida das barras, física de rebatida e reinício da bola no centro com direção aleatória a cada ponto (usando a biblioteca `random`).
* **Sistema de Pontuação:** Placar em tempo real. A partida encerra quando alguém atinge 20 pontos.
* **Armazenamento de Dados:** Salvamento persistente de resultados no arquivo `historico.txt`, usando Dicionários (estruturas de dados).
* **Efeitos Sonoros:** Feedback de áudio integrado para colisões e pontuação utilizando o `pygame.mixer`.
* **Testes Automatizados:** Implementação de testes da lógica de jogo usando `pytest`.

## 📂 Organização do Código-Fonte
O projeto segue uma arquitetura modularizada:
* `main.py`: Inicia o jogo, executa o loop principal e toca os áudios.
* `src/`: Pasta contendo toda a lógica modular (`config.py`, `dados.py`, `funcoes.py`, `jogo.py`, `sprites.py`).
* `tests/`: Pasta contendo os testes automatizados (`test_logica.py`).
* `docs/`: Pasta contendo a documentação e proposta inicial (`proposta.md`).
* `assets/`: Pasta destinada aos arquivos auxiliares, como áudios e imagens.

## 🎵 Referências de Assets Externos
Os seguintes recursos de terceiros foram utilizados no projeto:
* **Efeitos Sonoros:** Sons no formato `.wav` (`som_colisao.wav`, `som_ponto.wav`) simulando o áudio clássico de rebatida obtidos de bibliotecas gratuitas.
* **Fontes:** Fonte padrão nativa da biblioteca Pygame (`pygame.font.Font`).

## 🚀 Como Executar e Apresentar o Jogo
Este jogo está configurado e pronto para a **apresentação em sala de aula**.

**Pré-requisitos:** Python 3 instalado.

1. Instale as dependências necessárias:
   ```bash
   pip install pygame-ce pytest