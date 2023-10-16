# TODO: Escreva seu código aqui (fique à vontade para adicionar outros arquivos, mas use este como ponto de entrada)
import pygame
import random
#inicializa
def inicializa():
    pygame.init()

    #janela
    window = pygame.display.set_mode((400, 600))
    pygame.display.set_caption('Jogo do Rafak')

    #dicionario assets
    assets = {}
    assets['nave'] = pygame.image.load('assets/img/playerShip1_orange.png')
    assets['fundo'] = pygame.image.load('assets/img/starfield.png')

    return window, assets

def recebe_eventos():
    #inicia estruturas de dados
    game = True

    # loop principal
    while game:
        #trata eventos
        for event in pygame.event.get():
            #verifica consequências
            if event.type == pygame.QUIT:
                game = False
        return game

def desenha(window, assets, estrelas):
    # gera saídas
    window.fill((0, 0, 0))
    fundo = pygame.transform.scale(assets['fundo'], (400, 600))
    nave = pygame.transform.scale(assets['nave'], (69, 38))
    window.blit(fundo, (0, 0))
    window.blit(nave, (162, 530))

    # desenha estrelas
    for x, y in estrelas:
        pygame.draw.circle(window, (255, 255, 255), (x, y), 1, 5)

    # atualiza estado do jogo
    pygame.display.update()  
    return window

def gera_estrelas():
    estrelas = [(random.randint(0, 400), random.randint(0, 600)) for _ in range(40)]
    return estrelas

def game_loop(window, assets):
    game = True
    estrelas = gera_estrelas() 
    # loop principal
    while game:
        # trata eventos
        game = recebe_eventos()
        # gera saídas
        desenha(window, assets, estrelas)
        if game == False:
            return False

janela, assets = inicializa()
loop = game_loop(janela, assets)
