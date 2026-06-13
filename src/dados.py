# src/dados.py
from src.funcoes import LARGURA, BRANCO

def desenhar_placar(tela, fonte, pontos_1, pontos_2):
    """Renderiza a pontuação no topo da tela."""
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

def salvar_historico(pontos_1, pontos_2):
    """Usa um dicionário para estruturar os dados e salva em um arquivo de texto."""
    partida = {
        "jogador_1": pontos_1,
        "jogador_2": pontos_2,
        "vencedor": "Jogador 1" if pontos_1 > pontos_2 else "Jogador 2"
    }
    
    # Modo 'a' (append) para adicionar as linhas sem apagar o que já existe
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        linha = f"Vencedor: {partida['vencedor']} | Placar Final: {partida['jogador_1']} x {partida['jogador_2']}\n"
        arquivo.write(linha)
