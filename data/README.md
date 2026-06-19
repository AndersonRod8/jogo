# Assets

Esta pasta reúne todos os recursos utilizados pelo jogo Pong Arena PUC, incluindo elementos visuais, sonoros e recursos de interface.

## Estrutura

assets/
├── fontes/
│   └── README.md
├── imagens/
│   ├── spritesheet.bmp
│   └── README.md
└── sons/
    ├── colisao.wav
    ├── ponto.wav
    └── README.md

## Recursos Utilizados

### Fontes

O projeto utiliza a fonte padrão do Pygame através da função:

pygame.font.Font(None, tamanho)

Tamanhos utilizados:

- 74 px: placar da partida.
- 36 px: mensagens informativas e tela de fim de jogo.

Não foram utilizadas fontes externas (.ttf ou .otf).

### Sons

Arquivos utilizados:

- colisao.wav
  - Reproduzido quando a bola colide com as barras ou com os limites da tela.

- ponto.wav
  - Reproduzido quando um jogador marca ponto.

Formato utilizado:

- WAV (.wav)

### Imagens

Arquivo presente na pasta:

- spritesheet.bmp

Os principais elementos gráficos do jogo são desenhados diretamente pelo código utilizando funções do Pygame, incluindo:

- Barra do Jogador 1
- Barra do Jogador 2
- Bola
- Linha central da quadra
- Placar

## Objetivo da Pasta

Centralizar e organizar os recursos do projeto, facilitando a manutenção, reutilização e futuras expansões do jogo.

## Observações

A estrutura foi organizada seguindo boas práticas de desenvolvimento, mantendo os recursos separados por categoria para melhorar a legibilidade e a manutenção do projeto.