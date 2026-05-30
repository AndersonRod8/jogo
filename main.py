"""
Ponto de entrada da aplicação Pong
"""
import pygame
from src.game import Game

def main():
    """Inicializa e executa o jogo"""
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()