# src/config.py
import pygame
from src.funcoes import ALTURA

def mover_barra_1(teclas, y, vel, altura_barra):
    """Move a barra do Jogador 1 (Esquerda) com W e S."""
    if teclas[pygame.K_w] and y > 0:
        y -= vel
    if teclas[pygame.K_s] and y < ALTURA - altura_barra:
        y += vel
    return y

def mover_barra_2(teclas, y, vel, altura_barra):
    """Move a barra do Jogador 2 (Direita) com Setas Cima e Baixo."""
    if teclas[pygame.K_UP] and y > 0:
        y -= vel
    if teclas[pygame.K_DOWN] and y < ALTURA - altura_barra:
        y += vel
    return y