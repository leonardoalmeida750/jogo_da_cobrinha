# Importando as bibliotecas:
import pygame
import random
# Criando e Dimensionando a tela:
pygame.init()
pygame.display.set_caption("Cobrinha")
largura = 800
altura = 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
#Cores RGB
preta = (0, 0, 0)
branca =(255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
#Proporções de elementos e velocidade de execução
tamanho_quadrado = 10
velocidade_jogo= 30
# Posicionando Comida:
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    return comida_x, comida_y
# Adicionando Comida na Tela:
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho,
tamanho])

# Adicionando a Cobrinha na Tela:
def desenhar_cobra(tamanho, pixel_cobra):
    for pixel in pixel_cobra:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])
# Controles:
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    else:
        velocidade_x = 0
        velocidade_y = 0
    return velocidade_x, velocidade_y
#Criando o loop infinito da aplicação
def rodar_jogo():
    fim_jogo = False
    # Criando a Cobrinha:
    x = largura /2
    y = altura /2
    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixel_cobra = [0]
    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)


        #Desenhar-Comida:

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #Atualizar a posição:
        x += velocidade_x
        y += velocidade_y
    
        #Desenhar-Cobra:

        pixel_cobra.append([x, y])
        if len(pixel_cobra) > tamanho_cobra:
            del pixel_cobra[0]


        desenhar_cobra(tamanho_quadrado, pixel_cobra)

        
        #Atualização da Tela:
        pygame.display.update()
        

        #Criar uma nova comida:
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        
        relogio.tick(velocidade_jogo)

rodar_jogo()