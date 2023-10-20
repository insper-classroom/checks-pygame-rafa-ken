import pygame
import random

#----------------------------------------------------------------------------------------------------------#
def inicializa():
    pygame.init()
    janela = pygame.display.set_mode((400, 600))
    pygame.display.set_caption('Jogo do Rafak')

    # dicionario assets
    assets = {}
    assets['nave'] = pygame.image.load('assets/img/playerShip1_orange.png')
    assets['fundo'] = pygame.image.load('assets/img/starfield.png')
    assets['coracao'] = pygame.font.Font('assets/font/PressStart2P.ttf', 20)
    assets['fonte'] = pygame.font.Font('assets/font/PressStart2P.ttf', 13)
    assets['meteoros'] = pygame.image.load('assets/img/meteorBrown_med1.png')
    
    # dicionario state
    state = {}
    state['t0'] = -1
    state['limite_fps'] = pygame.time.Clock()
    state['posicao_nave'] = [165, 500]
    state['vel_nave'] = [0, 0]
    state['tiro'] = pygame.mixer.Sound('assets/snd/pew.wav')
    state['barulho_colisao'] = pygame.mixer.Sound('assets/snd/expl6.wav')
    state['vel_meteoro'] = [0, 0]
    state['vidas'] = 3
    state['oof'] = pygame.mixer.Sound('assets/snd/roblox-death-sound_1.mp3')
    # musica
    pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    pygame.mixer.music.play()

    return janela, assets, state
#----------------------------------------------------------------------------------------------------------#
def trata_eventos(state):
    jogo = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False
            pygame.quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                state['tiro'].play()
            if evento.key == pygame.K_w:
                state['vel_nave'][1] -= 6
            elif evento.key == pygame.K_s:
                state['vel_nave'][1] += 6
            elif evento.key == pygame.K_a:  
                state['vel_nave'][0] -= 6
            elif evento.key == pygame.K_d:
                state['vel_nave'][0] += 6
        if evento.type == pygame.KEYUP:
            state['vel_nave'] = [0, 0]

    # atualiza a posição da nave com base na velocidade
    state['posicao_nave'][0] += state['vel_nave'][0]
    state['posicao_nave'][1] += state['vel_nave'][1]

    # limite
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
def gera_meteoros():
    meteoros = [{'posicao': [random.randint(0, 400), random.randint(0, 100)], 'velocidade': [0, random.randint(1, 5)]} for _ in range(10)]
    return meteoros
#----------------------------------------------------------------------------------------------------------#
def verifica_colisoes(ob1, ob2):
    x1, y1, largura1, altura1 = ob1
    x2, y2, largura2, altura2 = ob2
    if (x1 < x2 + largura2 and x1 + largura1 > x2 and y1 < y2 + altura2 and y1 + altura1 > y2):
        return True
    return False
#----------------------------------------------------------------------------------------------------------#
def desenha(janela, recursos, estrelas, state,meteoros):
    janela.fill((0, 0, 0))
    fundo = pygame.transform.scale(recursos['fundo'], (400, 600))
    nave = pygame.transform.scale(recursos['nave'], (69, 38))
    janela.blit(fundo, (0, 0))
    
    # estrelas
    for x, y in estrelas:
        pygame.draw.circle(janela, (255, 255, 255), (x, y), 1, 5)
    
    # meteoros
    for meteoro in meteoros:
        x, y = meteoro['posicao']
        meteoro_surface = pygame.transform.scale(recursos['meteoros'], (30, 30))
        janela.blit(meteoro_surface, (x, y))
    
    # coracoes
    coracoes = chr(9829) * state['vidas']
    superficie_texto = recursos['coracao'].render(coracoes, True, (255, 0, 0))
    janela.blit(superficie_texto, (10, 10))

    #fps
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

    # desenha a nave na nova posição
    janela.blit(nave, state['posicao_nave'])
 
    pygame.display.update()
    return janela
#----------------------------------------------------------------------------------------------------------#
def gera_estrelas():
    estrelas = [(random.randint(0, 400), random.randint(0, 600)) for _ in range(200)]
    return estrelas
#----------------------------------------------------------------------------------------------------------#
def loop_jogo(janela, recursos, state):
    jogo = True
    estrelas = gera_estrelas()
    meteoros = gera_meteoros()  

    while jogo:
        trata_eventos(state)

        for meteoro in meteoros:
            meteoro['posicao'][0] += meteoro['velocidade'][0]
            meteoro['posicao'][1] += meteoro['velocidade'][1]

            if meteoro['posicao'][1] > 600:
                meteoro['posicao'] = [random.randint(0, 400), random.randint(-30, 0)]
                meteoro['velocidade'] = [0, random.randint(1, 5)]

            if verifica_colisoes(state['posicao_nave'] + [69, 38], meteoro['posicao'] + [30, 30]):
                state['vidas'] -= 1
                state['oof'].play()
                meteoro['posicao'] = [random.randint(0, 400), random.randint(-30, 0)]
                meteoro['velocidade'] = [0, random.randint(1, 5)]

        if state['vidas'] == 0:
            jogo = False
        
        desenha(janela, recursos, estrelas, state, meteoros)
#----------------------------------------------------------------------------------------------------------#
def principal():
    janela, recursos, state = inicializa()
    loop_jogo(janela, recursos, state)
    pygame.quit()
#----------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    principal()  




