# src/sprites.py
import pygame
from src.funcoes import BRANCO

#dimensções da barra do jogador
def desenhar_barra(tela, x, y, largura, altura):
    """Desenha a barra do jogador no ecrã."""
    pygame.draw.rect(tela, BRANCO, (x, y, largura, altura))

#dimensções da bola
def desenhar_bola(tela, x, y, tamanho):
    """Desenha a bola no ecrã."""
    pygame.draw.rect(tela, BRANCO, (x, y, tamanho, tamanho))
