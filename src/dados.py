# src/dados.py
from src.funcoes import LARGURA, BRANCO

def desenhar_placar(tela, fonte, pontos_1, pontos_2):
    """Renderiza a pontuação no topo do ecrã."""
    texto_p1 = fonte.render(str(pontos_1), True, BRANCO)
    texto_p2 = fonte.render(str(pontos_2), True, BRANCO)
    
    tela.blit(texto_p1, (LARGURA // 4, 30))
    tela.blit(texto_p2, (LARGURA * 3 // 4, 30))

def verificar_ponto(bola_x, tamanho, pontos_1, pontos_2):
    """Verifica se a bola saiu pelas laterais e atualiza os pontos."""
    if bola_x <= 0:
        pontos_2 += 1
        return True, pontos_1, pontos_2
    elif bola_x >= LARGURA - tamanho:
        pontos_1 += 1
        return True, pontos_1, pontos_2
        
    return False, pontos_1, pontos_2
