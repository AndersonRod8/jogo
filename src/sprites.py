# src/sprites.py
import pygame
from src.funcoes import BRANCO

def desenhar_barra(tela, x, y, largura, altura):
    """Renderiza a barra na tela."""
    pygame.draw.rect(tela, BRANCO, (x, y, largura, altura))

def desenhar_bola(tela, x, y, tamanho):
    """Renderiza a bola na tela."""
    pygame.draw.rect(tela, BRANCO, (x, y, tamanho, tamanho))