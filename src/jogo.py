# src/jogo.py
import pygame
from src.funcoes import ALTURA

#Movimento da bola e verificação das colisões com as bordas e barras.

def mover_bola(x, y, vel_x, vel_y, tamanho, p1_rect, p2_rect):
    
    x += vel_x
    y += vel_y

    # se a bola bater no topo ou na base
    if y <= 0 or y >= ALTURA - tamanho:
        vel_y *= -1

    # dimensôes da bola
    bola_rect = pygame.Rect(x, y, tamanho, tamanho)

    # Colisão da bola com a barra
    if bola_rect.colliderect(p1_rect) or bola_rect.colliderect(p2_rect):
        vel_x *= -1

    return x, y, vel_x, vel_y
