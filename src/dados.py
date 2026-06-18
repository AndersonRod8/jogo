# src/dados.py
import datetime
from src.funcoes import LARGURA, BRANCO

def verificar_ponto(bola_x, tamanho_bola, pontos_1, pontos_2):
    """Verifica se a bola passou da defesa e atualiza a pontuação."""
    marcou_ponto = False
    
    if bola_x >= LARGURA:
        pontos_1 += 1
        marcou_ponto = True
    elif bola_x <= -tamanho_bola:
        pontos_2 += 1
        marcou_ponto = True
        
    return marcou_ponto, pontos_1, pontos_2

def desenhar_placar(tela, fonte, pontos_1, pontos_2):
    """Desenha os pontos na tela."""
    texto_p1 = fonte.render(str(pontos_1), True, BRANCO)
    texto_p2 = fonte.render(str(pontos_2), True, BRANCO)
    tela.blit(texto_p1, (LARGURA // 4, 20))
    tela.blit(texto_p2, (3 * LARGURA // 4 - texto_p2.get_width(), 20))

def salvar_historico(pontos_1, pontos_2):
    """Grava o histórico de vencedores usando Dicionários."""
    vencedor = "Jogador 1" if pontos_1 > pontos_2 else "Jogador 2"
    placar = f"{pontos_1} x {pontos_2}"
    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    dados_partida = {
        "data": data_hora,
        "vencedor": vencedor,
        "placar": placar
    }
    
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"[{dados_partida['data']}] Vencedor: {dados_partida['vencedor']} | Placar: {dados_partida['placar']}\n"
        )