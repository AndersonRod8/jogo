# main.py
import pygame
import sys
import os
import random

from src.funcoes import LARGURA, ALTURA, PRETO, BRANCO, FPS
from src.config import mover_barra_1, mover_barra_2
from src.jogo import mover_bola
from src.dados import desenhar_placar, verificar_ponto, salvar_historico
from src.sprites import desenhar_barra, desenhar_bola

def main():
    # Inicializa o Pygame e o Mixer de Áudio
    pygame.mixer.init()
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pong Arena PUC")
    relogio = pygame.time.Clock()
    
    # Fontes de texto
    fonte = pygame.font.Font(None, 74)
    fonte_menor = pygame.font.Font(None, 36)

    # Carrega os Efeitos Sonoros com a organização de pastas correta
    try:
        som_colisao = pygame.mixer.Sound(os.path.join("assets", "sons", "colisao.wav"))
        som_ponto = pygame.mixer.Sound(os.path.join("assets", "sons", "ponto.wav"))
    except FileNotFoundError:
        print("AVISO: Arquivos de áudio não encontrados na pasta 'assets/sons'. O jogo ficará mudo.")
        som_colisao = None
        som_ponto = None

    # Configurações das Barras
    largura_barra, altura_barra = 15, 100
    vel_barra = 7
    p1_x, p1_y = 30, ALTURA // 2 - altura_barra // 2
    p2_x, p2_y = LARGURA - 30 - largura_barra, ALTURA // 2 - altura_barra // 2

    # Configurações da Bola
    tamanho_bola = 15
    bola_x, bola_y = LARGURA // 2 - tamanho_bola // 2, ALTURA // 2 - tamanho_bola // 2
    bola_vel_x, bola_vel_y = 5, 5

    # Estado Inicial do Jogo
    pontos_1, pontos_2 = 0, 0
    pontos_para_vencer = 20
    jogo_acabou = False
    historico_salvo = False

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        teclas = pygame.key.get_pressed()
        tela.fill(PRETO)

        if not jogo_acabou:
            # Movimentação dos jogadores
            p1_y = mover_barra_1(teclas, p1_y, vel_barra, altura_barra)
            p2_y = mover_barra_2(teclas, p2_y, vel_barra, altura_barra)

            p1_rect = pygame.Rect(p1_x, p1_y, largura_barra, altura_barra)
            p2_rect = pygame.Rect(p2_x, p2_y, largura_barra, altura_barra)

            # Movimentação e colisão da bola
            bola_x, bola_y, bola_vel_x, bola_vel_y, colidiu = mover_bola(
                bola_x, bola_y, bola_vel_x, bola_vel_y, tamanho_bola, p1_rect, p2_rect
            )

            # Toca o som se houver colisão
            if colidiu and som_colisao:
                som_colisao.play()

            # Verificação de pontos
            marcou_ponto, pontos_1, pontos_2 = verificar_ponto(bola_x, tamanho_bola, pontos_1, pontos_2)
            if marcou_ponto:
                if som_ponto:
                    som_ponto.play()
                
                # Reinicia a bola no centro com direção aleatória
                bola_x, bola_y = LARGURA // 2 - tamanho_bola // 2, ALTURA // 2 - tamanho_bola // 2
                bola_vel_x = random.choice([5, -5])
                bola_vel_y = random.choice([5, -5])

            # Verifica condição de vitória
            if pontos_1 >= pontos_para_vencer or pontos_2 >= pontos_para_vencer:
                jogo_acabou = True

            # Desenha os elementos na tela
            pygame.draw.aaline(tela, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))
            desenhar_barra(tela, p1_x, p1_y, largura_barra, altura_barra)
            desenhar_barra(tela, p2_x, p2_y, largura_barra, altura_barra)
            desenhar_bola(tela, bola_x, bola_y, tamanho_bola)
            desenhar_placar(tela, fonte, pontos_1, pontos_2)

        else:
            # Salva o resultado no histórico uma única vez ao terminar
            if not historico_salvo:
                salvar_historico(pontos_1, pontos_2)
                historico_salvo = True

            # Tela de fim de jogo
            texto_fim = fonte.render("FIM DE JOGO", True, BRANCO)
            texto_esc = fonte_menor.render("Pressione ESC para sair", True, BRANCO)
            tela.blit(texto_fim, (LARGURA // 2 - 160, ALTURA // 2 - 50))
            tela.blit(texto_esc, (LARGURA // 2 - 130, ALTURA // 2 + 20))

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

# Estas são as linhas que dão a "partida" no jogo
if __name__ == "__main__":
    main()