# tests/test_logica.py
import pygame
from src.dados import verificar_ponto
from src.jogo import mover_bola

def test_ponto_jogador_1():
    marcou, p1, p2 = verificar_ponto(bola_x=810, tamanho=15, pontos_1=0, pontos_2=0)
    assert marcou == True
    assert p1 == 1  
    assert p2 == 0

def test_ponto_jogador_2():
    marcou, p1, p2 = verificar_ponto(bola_x=-10, tamanho=15, pontos_1=0, pontos_2=0)
    assert marcou == True
    assert p1 == 0
    assert p2 == 1  

def test_colisao_topo():
    p1_rect = pygame.Rect(0, 0, 10, 10)
    p2_rect = pygame.Rect(0, 0, 10, 10)
    _, _, _, vel_y, colidiu = mover_bola(400, 0, 5, -5, 15, p1_rect, p2_rect)
    assert colidiu == True
    assert vel_y == 5