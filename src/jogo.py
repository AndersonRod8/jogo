# src/jogo.py
import pygame
from src.funcoes import ALTURA

def mover_bola(x, y, vel_x, vel_y, tamanho, p1_rect, p2_rect):
    """Movimenta a bola e verifica colisões com as bordas e barras."""
    x += vel_x
    y += vel_y

    # Colisão com o topo ou base
    if y <= 0 or y >= ALTURA - tamanho:
        vel_y *= -1

    # Cria o retângulo da bola para verificar intersecção
    bola_rect = pygame.Rect(x, y, tamanho, tamanho)

    # Colisão com as barras
    if bola_rect.colliderect(p1_rect) or bola_rect.colliderect(p2_rect):
        vel_x *= -1

    return x, y, vel_x, vel_y
