# src/jogo.py
import pygame
from src.funcoes import ALTURA

def mover_bola(x, y, vel_x, vel_y, tamanho, p1_rect, p2_rect):
    """Movimenta a bola e verifica colisões. Retorna se houve colisão."""
    x += vel_x
    y += vel_y
    colidiu = False

    # Colisão com o topo ou base
    if y <= 0 or y >= ALTURA - tamanho:
        vel_y *= -1
        colidiu = True

    bola_rect = pygame.Rect(x, y, tamanho, tamanho)

    # Colisão com as barras
    if bola_rect.colliderect(p1_rect) or bola_rect.colliderect(p2_rect):
        vel_x *= -1
        colidiu = True

    return x, y, vel_x, vel_y, colidiu