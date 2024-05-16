import pygame
import sys
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1440, 720))
pygame.display.set_caption("Trash Can Game")
screen.fill((255, 255, 255))
# Define as cores
AMARELO = (234, 196, 58)
BRANCO = (255, 255, 255)

# Definindo Fonte e Renderizando frase
import pygame.freetype

pygame.freetype.init()
fonteTexto = pygame.freetype.Font("Fontes/pixelplay.ttf", 30)


def get_pygame_events():
    pygame_events = pygame.event.get()
    return pygame_events


# Teclas
keys_pressed = get_pygame_events()

# Declarando Sons
musica_inicio = pygame.mixer.Sound("Sons/inicio.mp3")
musica_inicio_abafado = pygame.mixer.Sound("Sons/inicio_abafado.wav")
musica_jogo = pygame.mixer.Sound("Sons/jogo.wav")
click = pygame.mixer.Sound("Sons/click.wav")
start_som = pygame.mixer.Sound("Sons/start.wav")
gameover_som = pygame.mixer.Sound("Sons/gameover.wav")
gameover_musica = pygame.mixer.Sound("Sons/gameover_musica.wav")
p_bem_vindo = pygame.mixer.Sound("Sons/bem-vindo.wav")
p_500 = pygame.mixer.Sound("Sons/500.wav")
p_1000 = pygame.mixer.Sound("Sons/1000.wav")
p_gameover = pygame.mixer.Sound("Sons/gameover_som.wav")
acerto_lixeira = pygame.mixer.Sound("Sons/acerto_lixeira.wav")
som_500 = pygame.mixer.Sound("Sons/som_500.wav")
som_1000 = pygame.mixer.Sound("Sons/som_1000.wav")
som_2000 = pygame.mixer.Sound("Sons/som_2000.wav")


fundo_inicio_img = [
    pygame.image.load("Inicio/1.gif"),
    pygame.image.load("Inicio/2.gif"),
    pygame.image.load("Inicio/3.gif"),
    pygame.image.load("Inicio/4.gif"),
    pygame.image.load("Inicio/5.gif"),
    pygame.image.load("Inicio/6.gif"),
    pygame.image.load("Inicio/7.gif"),
    pygame.image.load("Inicio/8.gif"),
    pygame.image.load("Inicio/9.gif"),
    pygame.image.load("Inicio/10.gif"),
    pygame.image.load("Inicio/11.gif"),
    pygame.image.load("Inicio/12.gif"),
    pygame.image.load("Inicio/13.gif"),
    pygame.image.load("Inicio/14.gif"),
    pygame.image.load("Inicio/15.gif"),
]

final = [
    pygame.image.load("Gameover/1.gif"),
    pygame.image.load("Gameover/2.gif"),
    pygame.image.load("Gameover/3.gif"),
    pygame.image.load("Gameover/4.gif"),
    pygame.image.load("Gameover/5.gif"),
    pygame.image.load("Gameover/6.gif"),
    pygame.image.load("Gameover/7.gif"),
    pygame.image.load("Gameover/8.gif"),
    pygame.image.load("Gameover/9.gif"),
    pygame.image.load("Gameover/10.gif"),
    pygame.image.load("Gameover/11.gif"),
    pygame.image.load("Gameover/12.gif"),
    pygame.image.load("Gameover/13.gif"),
    pygame.image.load("Gameover/14.gif"),
    pygame.image.load("Gameover/15.gif"),
    pygame.image.load("Gameover/16.gif"),
    pygame.image.load("Gameover/17.gif"),
]

pontos = [
    pygame.image.load("Pontos/100.gif"),
    pygame.image.load("Pontos/200.gif"),
    pygame.image.load("Pontos/300.gif"),
    pygame.image.load("Pontos/400.gif"),
    pygame.image.load("Pontos/500.gif"),
    pygame.image.load("Pontos/600.gif"),
    pygame.image.load("Pontos/700.gif"),
    pygame.image.load("Pontos/800.gif"),
    pygame.image.load("Pontos/900.gif"),
    pygame.image.load("Pontos/1000.gif"),
    pygame.image.load("Pontos/1100.gif"),
    pygame.image.load("Pontos/1200.gif"),
    pygame.image.load("Pontos/1300.gif"),
    pygame.image.load("Pontos/1400.gif"),
    pygame.image.load("Pontos/1500.gif"),
    pygame.image.load("Pontos/1600.gif"),
    pygame.image.load("Pontos/1700.gif"),
    pygame.image.load("Pontos/1800.gif"),
    pygame.image.load("Pontos/1900.gif"),
    pygame.image.load("Pontos/2000.gif"),
    pygame.image.load("Pontos/2100.gif"),
    pygame.image.load("Pontos/2200.gif"),
    pygame.image.load("Pontos/2300.gif"),
    pygame.image.load("Pontos/2400.gif"),
    pygame.image.load("Pontos/2500.gif"),
    pygame.image.load("Pontos/2600.gif"),
    pygame.image.load("Pontos/2700.gif"),
    pygame.image.load("Pontos/2800.gif"),
    pygame.image.load("Pontos/2900.gif"),
    pygame.image.load("Pontos/3000.gif"),
    pygame.image.load("Pontos/0.gif"),
]

fundo_jogo_img = [
    pygame.image.load("Fundo/1.gif"),
    pygame.image.load("Fundo/2.gif"),
    pygame.image.load("Fundo/3.gif"),
    pygame.image.load("Fundo/4.gif"),
    pygame.image.load("Fundo/5.gif"),
    pygame.image.load("Fundo/6.gif"),
    pygame.image.load("Fundo/7.gif"),
    pygame.image.load("Fundo/8.gif"),
    pygame.image.load("Fundo/9.gif"),
    pygame.image.load("Fundo/10.gif"),
    pygame.image.load("Fundo/11.gif"),
    pygame.image.load("Fundo/12.gif"),
    pygame.image.load("Fundo/13.gif"),
    pygame.image.load("Fundo/14.gif"),
    pygame.image.load("Fundo/15.gif"),
    pygame.image.load("Fundo/16.gif"),
    pygame.image.load("Fundo/17.gif"),
    pygame.image.load("Fundo/18.gif"),
    pygame.image.load("Fundo/19.gif"),
    pygame.image.load("Fundo/20.gif"),
    pygame.image.load("Fundo/21.gif"),
    pygame.image.load("Fundo/22.gif"),
    pygame.image.load("Fundo/23.gif"),
    pygame.image.load("Fundo/24.gif"),
    pygame.image.load("Fundo/25.gif"),
    pygame.image.load("Fundo/26.gif"),
    pygame.image.load("Fundo/27.gif"),
    pygame.image.load("Fundo/28.gif"),
    pygame.image.load("Fundo/29.gif"),
    pygame.image.load("Fundo/30.gif"),
    pygame.image.load("Fundo/31.gif"),
    pygame.image.load("Fundo/32.gif"),
    pygame.image.load("Fundo/33.gif"),
    pygame.image.load("Fundo/34.gif"),
    pygame.image.load("Fundo/35.gif"),
    pygame.image.load("Fundo/36.gif"),
    pygame.image.load("Fundo/37.gif"),
    pygame.image.load("Fundo/38.gif"),
    pygame.image.load("Fundo/39.gif"),
    pygame.image.load("Fundo/40.gif"),
    pygame.image.load("Fundo/41.gif"),
    pygame.image.load("Fundo/42.gif"),
    pygame.image.load("Fundo/43.gif"),
]

p_bem_vindo.play()


# tela_inicial_menu
def fundo_inicio():
    gameover_musica.stop()
    musica_inicio_abafado.stop()
    musica_inicio.play(-50)
    musica_jogo.stop()
    sair = False
    while not sair:
        i = 0
        while i < 15:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # area_botao_jogo
                    if x > 608 and x < 850:
                        if y > 545 and y < 587:
                            click.play()
                            fundo_jogo()

                    # area_botao_sair
                    if x > 1374 and x < 1403:
                        if y > 24 and y < 54:
                            click.play()
                            botao_sair()

                    # area_botao_ajuda
                    if x > 1376 and x < 1404:
                        if y > 70 and y < 100:
                            click.play()
                            botao_ajuda()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()

            screen.blit(fundo_inicio_img[i], (0, 0))

            pygame.time.delay(100)
            pygame.display.update()
            i += 1


# tela_jogo_jogar
def fundo_jogo():
    gameover_musica.stop()
    musica_inicio.stop()
    musica_jogo.stop()
    start_som.play()
    musica_jogo.play(-1)
    pontuacao = 0

    # Props
    organico = pygame.image.load("Props/item-organico.png")
    plastico = pygame.image.load("Props/item-plastico.png")
    papel = pygame.image.load("Props/item-papel.png")
    vidro = pygame.image.load("Props/item-vidro.png")
    metal = pygame.image.load("Props/item-metal.png")

    clock = pygame.time.Clock()

    sair = False
    i = 0
    while not sair:
        while i < 43:
            screen.blit(fundo_jogo_img[i], (0, 0))

            for event in pygame.event.get():
                # Caso saia
                if event.type == pygame.QUIT:
                    pygame.quit()

                # MOUSEMOTION PARA CAPTURA DE POSIÇÕES
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

            # DEFINIÇÃO DE VARIÁVEIS
            # lixeiras
            lixeiras = pygame.image.load("Props/lixeiras.png")

            # MOVIMENTAÇÃO OBJETO
            # posições tela
            posX = 610
            posY = 20

            # Objeto aleatório
            numero = random.randint(1, 5)
            if numero == 1:
                objeto = plastico

            elif numero == 2:
                objeto = papel

            elif numero == 3:
                objeto = metal

            elif numero == 4:
                objeto = vidro

            elif numero == 5:
                objeto = organico

            while posY < 460:
                # Fica blitando o fundo animado (?)
                if i > 41:
                    i = 0
                    screen.blit(fundo_jogo_img[i], (0, 0))

                else:
                    i += 1
                    screen.blit(fundo_jogo_img[i], (0, 0))

                # Blita as lixeiras e o placar
                screen.blit(lixeiras, (0, 0))

                # Blita pontuacao
                # fonteTexto.render_to(screen, (50, 50), str(pontuacao), AMARELO)

                # Lógica do aumento da dificuldade
                if pontuacao == 0 or pontuacao < 500:
                    posY += 2

                elif pontuacao < 1000:
                    posY += 3

                elif pontuacao < 1500:
                    posY += 4

                elif pontuacao < 2000:
                    posY += 6

                elif pontuacao < 2500:
                    posY += 8

                else:
                    posY += 10

                if pontuacao == 0:
                    x = 30
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 100:
                    x = 0
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 200:
                    x = 1
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 300:
                    x = 2
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 400:
                    x = 3
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 500:
                    x = 4
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 600:
                    x = 5
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 700:
                    x = 6
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 800:
                    x = 7
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 900:
                    x = 8
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1000:
                    x = 9
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1100:
                    x = 10
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1200:
                    x = 11
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1300:
                    x = 12
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1400:
                    x = 13
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1500:
                    x = 14
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1600:
                    x = 15
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1700:
                    x = 16
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1800:
                    x = 17
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 1900:
                    x = 18
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2000:
                    x = 19
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2100:
                    x = 20
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2200:
                    x = 21
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2300:
                    x = 22
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2400:
                    x = 23
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2500:
                    x = 24
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2600:
                    x = 25
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2700:
                    x = 26
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2800:
                    x = 27
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 2900:
                    x = 28
                    screen.blit(pontos[x], (0, 0))

                if pontuacao == 3000:
                    x = 29
                    screen.blit(pontos[x], (0, 0))

                # Movimentação do X e aceleração do Y
                for event in pygame.event.get():
                    a = 0

                comandos = pygame.key.get_pressed()
                if comandos[pygame.K_LEFT]:
                    posX -= 15
                if comandos[pygame.K_RIGHT]:
                    posX += 15
                if comandos[pygame.K_DOWN]:
                    posY += 8

                # Vai blitando o objeto aleatório de acordo com a posição
                screen.blit(objeto, (posX, posY))
                pygame.display.update()

            # COLISÕES
            # Colisão lixeira plastico
            if objeto == plastico:
                if posX > 67 and posX < 233:
                    acerto_lixeira.play()
                    pontuacao += 100

                if posX < 67 or posX > 233:
                    gameover(pontuacao)

            # Colisão lixeira papel
            if objeto == papel:
                if posX > 296 and posX < 460:
                    acerto_lixeira.play()
                    pontuacao += 100

                if posX < 296 or posX > 460:
                    gameover(pontuacao)

            # Colisão lixeira metal
            if objeto == metal:
                if posX > 630 and posX < 805:
                    acerto_lixeira.play()
                    pontuacao += 100

                if posX < 630 or posX > 805:
                    gameover(pontuacao)

            # Colisão lixeira vidro
            if objeto == vidro:
                if posX > 928 and posX < 1089:
                    acerto_lixeira.play()
                    pontuacao += 100

                if posX < 928 or posX > 1089:
                    gameover(pontuacao)

            # Colisão lixeira organico
            if objeto == organico:
                if posX > 1152 and posX < 1320:
                    acerto_lixeira.play()
                    pontuacao += 100

                if posX < 1152 or posX > 1320:
                    gameover(pontuacao)

            if pontuacao == 500:
                som_500.play()
                pygame.time.delay(200)
                p_500.play()

            if pontuacao == 1000:
                som_1000.play()
                pygame.time.delay(200)
                p_1000.play()

            if pontuacao == 2000:
                som_2000.play()

            clock.tick(100)


# botao_sair
def botao_sair():
    pygame.quit()


def botao_ajuda():
    musica_inicio.stop()
    musica_inicio_abafado.play(-1)
    sair = False
    while not sair:
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    print("Mouse Movendo X:", x)
                    print("Mouse Movendo Y:", y)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 30 and x < 78:
                        if y > 30 and y < 73:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()

            screen.blit(fundo_inicio_img[i], (0, 0))
            # botao-voltar
            voltar = pygame.image.load("Props/botao-voltar.png")
            screen.blit(voltar, (0, 0))

            # botao-voltar
            como_jogar = pygame.image.load("Props/como_jogar.png")
            screen.blit(como_jogar, (0, 0))

            pygame.time.delay(120)
            pygame.display.update()
            i += 1


def botao_creditos():
    musica_inicio.stop()
    musica_inicio_abafado.play(-1)
    sair = False
    while not sair:
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    print("Mouse Movendo X:", x)
                    print("Mouse Movendo Y:", y)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 30 and x < 78:
                        if y > 30 and y < 73:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()

            screen.blit(fundo_inicio_img[i], (0, 0))
            # botao-voltar
            voltar = pygame.image.load("Props/botao-voltar.png")
            screen.blit(voltar, (0, 0))

            # desenvolvedores
            desenvolvedores = pygame.image.load("Props/desenvolvedores.png")
            screen.blit(desenvolvedores, (0, 0))

            pygame.time.delay(120)
            pygame.display.update()
            i += 1


def gameover(pontuacao):
    musica_jogo.stop()
    gameover_som.play()
    p_gameover.play()
    gameover_musica.play(-1)
    sair = False
    while not sair:
        i = 0
        while i < 17:
            for event in pygame.event.get():
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if event.type == pygame.MOUSEMOTION:
                    print("Mouse Movendo X:", x)
                    print("Mouse Movendo Y:", y)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 821 and x < 943:
                        if y > 420 and y < 466:
                            click.play()
                            fundo_jogo()

                    if x > 965 and x < 1087:
                        if y > 420 and y < 467:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()

            screen.blit(final[i], (0, 0))
            fonteTexto.render_to(screen, (1023, 238), str(pontuacao), BRANCO)

            pygame.time.delay(120)
            pygame.display.update()
            i += 1


def main():
    fundo_inicio()


main()
