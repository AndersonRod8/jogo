# main.py
import pygame
import sys

# Importações dos módulos organizados na pasta src
from src.funcoes import LARGURA, ALTURA, PRETO, BRANCO, FPS
from src.config import mover_barra_1, mover_barra_2
from src.jogo import mover_bola
from src.dados import desenhar_placar, verificar_ponto
from src.sprites import desenhar_barra, desenhar_bola

def main():
    # Inicializa o Pygame
    pygame.init()
    
    # Configuração da janela
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("O Meu Primeiro Pong")
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 74)

    # Configurações das Barras
    largura_barra, altura_barra = 15, 100
    vel_barra = 7
    p1_x, p1_y = 30, ALTURA // 2 - altura_barra // 2
    p2_x, p2_y = LARGURA - 30 - largura_barra, ALTURA // 2 - altura_barra // 2

    # Configurações da Bola
    tamanho_bola = 15
    bola_x, bola_y = LARGURA // 2 - tamanho_bola // 2, ALTURA // 2 - tamanho_bola // 2
    bola_vel_x, bola_vel_y = 5, 5

    # Placar Inicial
    pontos_1, pontos_2 = 0, 0

    # Ciclo Principal do Jogo (Loop)
    rodando = True
    while rodando:
        # 1. Tratamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        teclas = pygame.key.get_pressed()

        # 2. Movimentação e Atualização
        p1_y = mover_barra_1(teclas, p1_y, vel_barra, altura_barra)
        p2_y = mover_barra_2(teclas, p2_y, vel_barra, altura_barra)

        p1_rect = pygame.Rect(p1_x, p1_y, largura_barra, altura_barra)
        p2_rect = pygame.Rect(p2_x, p2_y, largura_barra, altura_barra)

        bola_x, bola_y, bola_vel_x, bola_vel_y = mover_bola(
            bola_x, bola_y, bola_vel_x, bola_vel_y, tamanho_bola, p1_rect, p2_rect
        )

        marcou_ponto, pontos_1, pontos_2 = verificar_ponto(bola_x, tamanho_bola, pontos_1, pontos_2)
        if marcou_ponto:
            # Bola é reposicionada ao centro após adversário marcar 1 ponto
            bola_x, bola_y = LARGURA // 2 - tamanho_bola // 2, ALTURA // 2 - tamanho_bola // 2
            bola_vel_x *= -1 

        # 3. Renderização (Desenhar no Ecrã)
        tela.fill(PRETO)
        
        # Linha central divisória
        pygame.draw.aaline(tela, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

        # Funções importadas de src/sprites.py
        desenhar_barra(tela, p1_x, p1_y, largura_barra, altura_barra)
        desenhar_barra(tela, p2_x, p2_y, largura_barra, altura_barra)
        desenhar_bola(tela, bola_x, bola_y, tamanho_bola)
        
        # Função importada de src/dados.py
        desenhar_placar(tela, fonte, pontos_1, pontos_2)

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
