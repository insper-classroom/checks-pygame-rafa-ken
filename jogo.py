# TODO: Escreva seu código aqui (fique à vontade para adicionar outros arquivos, mas use este como ponto de entrada)
import pygame
#inicializa
def inicializa():
    pygame.init()

    #janela
    window = pygame.display.set_mode((320, 240))
    pygame.display.set_caption('Jogo do Rafak')

    #retorno
    return window

def recebe_eventos():
    #Inicia estruturas de dados
    game = True

    # Loop principal
    while game:
        #Trata eventos
        for event in pygame.event.get():
            #Verifica consequências
            if event.type == pygame.QUIT:
                game = False
        return game

def desenha(window):
    #Gera saídas
    window.fill((0,0,0))  #Preenche com a cor vermelha

    #Atualiza estado do jogo
    pygame.display.update()  #Mostra o novo frame para o jogador
    return window

def game_loop(window):
    game = True
    #Loop principal
    while game:
        #Trata eventos
        game = recebe_eventos()
        if game == False:
            return game

        #gera saidas
        desenha(window)
janela = inicializa()
loop = game_loop(janela)

