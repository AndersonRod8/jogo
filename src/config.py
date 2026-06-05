# src/config.py
import pygame
from src.funcoes import ALTURA

def mover_barra_1(teclas, y, velocidade, altura_barra):
    """Controla a barra do Jogador 1 (W e S)."""
    if teclas[pygame.K_w] and y > 0:
        y -= velocidade
    if teclas[pygame.K_s] and y < ALTURA - altura_barra:
        y += velocidade
    return y

def mover_barra_2(teclas, y, velocidade, altura_barra):
    """Controla a barra do Jogador 2 (Setas Cima e Baixo)."""
    if teclas[pygame.K_UP] and y > 0:
        y -= velocidade
    if teclas[pygame.K_DOWN] and y < ALTURA - altura_barra:
        y += velocidade
    return y
