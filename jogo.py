import pygame
import random

#----------------------------------------------------------------------------------------------------------#
# Função que inicializa o jogo: cria a janela, carrega recursos e define o estado inicial.
import pygame

def inicializa():
    pygame.init()
    janela = pygame.display.set_mode((400, 600))
    pygame.display.set_caption('Jogo do Rafak')

    # Carrega imagens e fontes como recursos do jogo.
    assets = {}
    assets['nave'] = pygame.image.load('assets/img/playerShip1_orange.png')
    assets['fundo'] = pygame.image.load('assets/img/starfield.png')
    assets['coracao'] = pygame.font.Font('assets/font/PressStart2P.ttf', 20)
    assets['fonte'] = pygame.font.Font('assets/font/PressStart2P.ttf', 13)

    # Define o estado inicial do jogo, incluindo o tempo, posição e velocidade da nave.
    state = {}
    state['t0'] = -1
    state['limite_fps'] = pygame.time.Clock()
    state['posicao_nave'] = [165, 500]
    state['vel_nave'] = [0, 0]

    return janela, assets, state

# Função que trata eventos do jogo, como fechar a janela e controlar a velocidade da nave.
def trata_eventos(state):
    jogo = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                state['vel_nave'][1] -= 2
            elif evento.key == pygame.K_s:
                state['vel_nave'][1] += 2
            elif evento.key == pygame.K_a:  
                state['vel_nave'][0] -= 2
            elif evento.key == pygame.K_d:
                state['vel_nave'][0] += 2
        if evento.type == pygame.KEYUP:
            state['vel_nave'] = [0, 0]

    # Atualiza a posição da nave com base na velocidade.
    state['posicao_nave'][0] += state['vel_nave'][0]
    state['posicao_nave'][1] += state['vel_nave'][1]

    # Corrige a verificação das posições x e y da nave.
    if state['posicao_nave'][0] < 0:
        state['posicao_nave'][0] = 0
    elif state['posicao_nave'][0] > 331:
        state['posicao_nave'][0] = 331

    if state['posicao_nave'][1] < 0:
        state['posicao_nave'][1] = 0
    elif state['posicao_nave'][1] > 562:
        state['posicao_nave'][1] = 562

    return jogo

#----------------------------------------------------------------------------------------------------------#
# Função que desenha os elementos do jogo na janela.
def desenha(janela, recursos, estrelas, state):
    janela.fill((0, 0, 0))  # Preenche a janela com a cor preta.
    fundo = pygame.transform.scale(recursos['fundo'], (400, 600))
    nave = pygame.transform.scale(recursos['nave'], (69, 38))
    janela.blit(fundo, (0, 0))
    
    # Desenha estrelas na tela.
    for x, y in estrelas:
        pygame.draw.circle(janela, (255, 255, 255), (x, y), 1, 5)
    
    # Desenha corações na tela.
    coracoes = chr(9829) * 3
    superficie_texto = recursos['coracao'].render(coracoes, True, (255, 0, 0))
    janela.blit(superficie_texto, (10, 10))
    
    # Calcula e exibe os quadros por segundo (FPS).
    fps = 0
    tempo_delta = 0.0001
    t1 = pygame.time.get_ticks()

    if state['t0'] >= 0:
        tempo_delta = t1 - state['t0']

    state['t0'] = t1
    fps = 1000 / tempo_delta
    texto_fps = recursos['fonte'].render(f'FPS: {fps:.2f}', True, (255, 255, 255))
    janela.blit(texto_fps, (250, 587))
    state['limite_fps'].tick(60)

    # Desenha a nave na nova posição.
    janela.blit(nave, state['posicao_nave'])

    pygame.display.update()
    return janela

#----------------------------------------------------------------------------------------------------------#
# Função que gera coordenadas aleatórias para estrelas.
def gera_estrelas():
    estrelas = [(random.randint(0, 400), random.randint(0, 600)) for _ in range(200)]
    return estrelas

#----------------------------------------------------------------------------------------------------------#
# Função que executa o loop principal do jogo.
def loop_jogo(janela, recursos, state):
    jogo = True
    estrelas = gera_estrelas()
    
    # Loop principal do jogo.
    while jogo:
        jogo = trata_eventos(state)  # Trata eventos do jogo.
        desenha(janela, recursos, estrelas, state)  # Desenha elementos na janela.

    return False

#----------------------------------------------------------------------------------------------------------#
# Função principal que inicia o jogo e chama o loop principal.
def principal():
    janela, recursos, state = inicializa()
    loop_jogo(janela, recursos, state)
    pygame.quit()

#----------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    principal()  




