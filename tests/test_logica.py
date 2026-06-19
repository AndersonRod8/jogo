# tests/test_logica.py
import pygame
from src.dados import verificar_ponto
from src.jogo import mover_bola
from src.config import mover_barra_1
from src.funcoes import LARGURA, ALTURA

# Inicializa Pygame para testes 
pygame.init()

# TESTES DE PONTUAÇÃO


def test_ponto_jogador_1():
    """Testa se o Jogador 1 recebe ponto quando a bola ultrapassa a borda direita."""
    marcou, p1, p2 = verificar_ponto(bola_x=LARGURA + 10, tamanho_bola=15, pontos_1=0, pontos_2=0)
    assert marcou == True
    assert p1 == 1  
    assert p2 == 0

def test_ponto_jogador_2():
    """Testa se o Jogador 2 recebe ponto quando a bola ultrapassa a borda esquerda."""
    marcou, p1, p2 = verificar_ponto(bola_x=-20, tamanho_bola=15, pontos_1=0, pontos_2=0)
    assert marcou == True
    assert p1 == 0
    assert p2 == 1  

def test_bola_meio_da_tela_sem_ponto():
    """Garante que nenhum ponto é marcado enquanto a bola está transitando no meio do campo."""
    marcou, p1, p2 = verificar_ponto(bola_x=LARGURA // 2, tamanho_bola=15, pontos_1=5, pontos_2=3)
    assert marcou == False
    assert p1 == 5
    assert p2 == 3


# TESTES DE COLISÃO DA BOLA


def test_colisao_topo():
    """Testa se a bola rebate ao bater no teto da tela."""
    p1_rect = pygame.Rect(0, 0, 10, 10)
    p2_rect = pygame.Rect(0, 0, 10, 10)
    # Bola em Y=0 indo para cima (vel_y = -5)
    _, _, _, vel_y, colidiu = mover_bola(400, 0, 5, -5, 15, p1_rect, p2_rect)
    
    assert colidiu == True
    assert vel_y == 5  # A velocidade deve descer

def test_colisao_chao():
    """Testa se a bola rebate ao bater no chão da tela."""
    p1_rect = pygame.Rect(0, 0, 10, 10)
    p2_rect = pygame.Rect(0, 0, 10, 10)
    # Bola indo para baixo (vel = 5)
    _, _, _, vel_y, colidiu = mover_bola(400, ALTURA - 15, 5, 5, 15, p1_rect, p2_rect)
    
    assert colidiu == True
    assert vel_y == -5  # A velocidade deve subir

def test_colisao_barra_esquerda():
    """Testa se a bola rebate corretamente ao bater na barra do Jogador 1."""
    p1_rect = pygame.Rect(30, 250, 15, 100)  #Barra na esquerda
    p2_rect = pygame.Rect(750, 250, 15, 100)
    
    #Bola na posição da barra 1, indo para a esquerda (vel = -5)
    _, _, vel_x, _, colidiu = mover_bola(45, 260, -5, 5, 15, p1_rect, p2_rect)
    
    assert colidiu == True
    assert vel_x == 5  

# TESTES DE FÍSICA DOS JOGADORES

def test_movimentacao_barra_respeita_teto():
    """Garante que a barra do jogador não ultrapasse a tela para cima."""
    # Simula a lista de teclas do Pygame, com a tecla W (cima) pressionada
    teclas = [False] * 512
    teclas[pygame.K_w] = True
    
    # Tenta mover para cima estando já na coordenada Y=0
    novo_y = mover_barra_1(teclas, y=0, vel=7, altura_barra=100)
    assert novo_y == 0  # Deve continuar em 0, não pode ficar negativo

def test_movimentacao_barra_respeita_chao():
    """Garante que a barra do jogador não ultrapasse a tela para baixo."""
    # Simula a lista de teclas do Pygame, com a tecla S (baixo) pressionada
    teclas = [False] * 512
    teclas[pygame.K_s] = True
    
    # Tenta mover para baixo estando já no limite do chão
    limite = ALTURA - 100
    novo_y = mover_barra_1(teclas, y=limite, vel=7, altura_barra=100)
    assert novo_y == limite  # Deve continuar no limite
