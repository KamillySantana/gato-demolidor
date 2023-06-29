import pygame
import random

# Cores
BRANCO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
PRETO = (255, 255, 255)

# Dimensões da tela
largura_tela = 800
altura_tela = 600

# Dimensões da barra
largura_barra = 100
altura_barra = 20

# Dimensões do tijolo
largura_tijolo = 60
altura_tijolo = 20

pygame.init()

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Many Bricks Breaker")

relogio = pygame.time.Clock()

# Carregar a imagem do gato
gato_imagem = pygame.image.load("gatooo.png")
gato_imagem = pygame.transform.scale(gato_imagem, (25, 25))

# Carregar a imagem do peixe e redimensioná-la
peixe_imagem = pygame.image.load("peixinho.png")
peixe_imagem = pygame.transform.scale(peixe_imagem, (largura_tijolo, altura_tijolo))


def desenhar_barra(x, y):
    pygame.draw.rect(tela, VERDE, [x, y, largura_barra, altura_barra])


def desenhar_tijolo(x, y):
    tela.blit(peixe_imagem, (x, y))


def desenhar_gato(x, y):
    tela.blit(gato_imagem, (x, y))


def colisao_bola_tijolo(x, y, tijolo_x, tijolo_y):
    if x >= tijolo_x and x <= tijolo_x + largura_tijolo and y >= tijolo_y and y <= tijolo_y + altura_tijolo:
        return True
    return False


def tela_inicial():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                many_bricks_breaker()

        tela.fill(BRANCO)

        fonte_titulo = pygame.font.Font(None, 72)
        titulo = fonte_titulo.render("Gato Demolidor", True, VERMELHO)
        posicao_titulo = titulo.get_rect(center=(largura_tela / 2, altura_tela / 2 - 100))
        tela.blit(titulo, posicao_titulo)

        fonte = pygame.font.Font(None, 36)
        texto = fonte.render("Clique para jogar", True, VERMELHO)
        posicao_texto = texto.get_rect(center=(largura_tela / 2, altura_tela / 2))
        tela.blit(texto, posicao_texto)

        pygame.display.update()
        relogio.tick(60)


def many_bricks_breaker():
    # Posição inicial da barra
    barra_x = largura_tela / 2 - largura_barra / 2
    barra_y = altura_tela - altura_barra - 10

    # Posição inicial do gato
    gato_x = largura_tela / 2
    gato_y = altura_tela - altura_barra - 20

    # Velocidade do gato
    gato_dx = 3
    gato_dy = -3

    # Níveis de dificuldade
    niveis = [
        {"linhas": 1, "tijolos_por_linha": 10},
        {"linhas": 2, "tijolos_por_linha": 10},
        {"linhas": 3, "tijolos_por_linha": 10},
        {"linhas": 4, "tijolos_por_linha": 10},
        {"linhas": 5, "tijolos_por_linha": 10},
        {"linhas": 6, "tijolos_por_linha": 10},
        {"linhas": 7, "tijolos_por_linha": 10},
        {"linhas": 8, "tijolos_por_linha": 10},
        {"linhas": 9, "tijolos_por_linha": 10},
        {"linhas": 10, "tijolos_por_linha": 10},
    ]

    nivel_atual = 0
    tijolos = []

    # Pontuação
    pontuacao = 0

    # Variável para controlar a pausa
    pausado = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = not pausado

        if pausado:
            continue  # Pausa o jogo

        tela.fill(BRANCO)

        # Movimento da barra
        posicao_mouse = pygame.mouse.get_pos()
        barra_x = posicao_mouse[0]

        # Verificar colisão do gato com a barra
        if gato_y + 10 >= barra_y and gato_y + 10 <= barra_y + altura_barra and gato_x >= barra_x and gato_x <= barra_x + largura_barra:
            gato_dy = -gato_dy

        # Verificar colisão do gato com os tijolos
        for tijolo in tijolos:
            tijolo_x, tijolo_y = tijolo
            if colisao_bola_tijolo(gato_x, gato_y, tijolo_x, tijolo_y):
                tijolos.remove(tijolo)
                gato_dy = -gato_dy
                pontuacao += 10

        # Atualizar posição do gato
        gato_x += gato_dx
        gato_y += gato_dy

        # Verificar colisão com as paredes laterais
        if gato_x >= largura_tela - 10 or gato_x <= 10:
            gato_dx = -gato_dx

        # Verificar colisão com a parede superior
        if gato_y <= 10:
            gato_dy = -gato_dy

        # Verificar se o gato saiu da tela
        if gato_y >= altura_tela:
            tela.fill(BRANCO)
            fonte = pygame.font.Font(None, 36)
            texto = fonte.render("Você Perdeu :(", True, PRETO)
            posicao_texto = texto.get_rect(center=(largura_tela / 2, altura_tela / 2 - 50))
            tela.blit(texto, posicao_texto)

            texto_pontuacao = fonte.render(f"Miau miau a sua pontuação é de {pontuacao} Miau", True, PRETO)
            posicao_texto_pontuacao = texto_pontuacao.get_rect(center=(largura_tela / 2, altura_tela / 2))
            tela.blit(texto_pontuacao, posicao_texto_pontuacao)

            texto_fim = fonte.render("FIM", True, PRETO)
            posicao_texto_fim = texto_fim.get_rect(center=(largura_tela / 2, altura_tela / 2 + 50))
            tela.blit(texto_fim, posicao_texto_fim)

            reiniciar_texto = fonte.render("Clique para reiniciar", True, VERMELHO)
            posicao_reiniciar_texto = reiniciar_texto.get_rect(center=(largura_tela / 2, altura_tela / 2 + 100))
            tela.blit(reiniciar_texto, posicao_reiniciar_texto)

            pygame.display.update()

            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        many_bricks_breaker()

        desenhar_barra(barra_x, barra_y)
        desenhar_gato(gato_x, gato_y)

        if not tijolos:
            if nivel_atual >= len(niveis):
                tela.fill(BRANCO)
                fonte = pygame.font.Font(None, 36)
                texto = fonte.render(f"Voce ganhou! Pontuação: {pontuacao}", True, PRETO)
                posicao_texto = texto.get_rect(center=(largura_tela / 2, altura_tela / 2 - 50))
                tela.blit(texto, posicao_texto)

                texto_pontuacao = fonte.render(f"Miau miau a sua pontuação é de {pontuacao} Miau", True, PRETO)
                posicao_texto_pontuacao = texto_pontuacao.get_rect(center=(largura_tela / 2, altura_tela / 2))
                tela.blit(texto_pontuacao, posicao_texto_pontuacao)

                texto_fim = fonte.render("FIM", True, PRETO)
                posicao_texto_fim = texto_fim.get_rect(center=(largura_tela / 2, altura_tela / 2 + 50))
                tela.blit(texto_fim, posicao_texto_fim)

                reiniciar_texto = fonte.render("Clique para reiniciar", True, VERMELHO)
                posicao_reiniciar_texto = reiniciar_texto.get_rect(center=(largura_tela / 2, altura_tela / 2 + 100))
                tela.blit(reiniciar_texto, posicao_reiniciar_texto)

                pygame.display.update()

                while True:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif evento.type == pygame.MOUSEBUTTONDOWN:
                            many_bricks_breaker()
            else:
                nivel_atual += 1
                nivel = niveis[nivel_atual - 1]
                tijolos = []
                for i in range(nivel["linhas"]):
                    for j in range(nivel["tijolos_por_linha"]):
                        tijolo_x = j * (largura_tijolo + 10) + 50
                        tijolo_y = i * (altura_tijolo + 10) + 50
                        tijolos.append((tijolo_x, tijolo_y))

        for tijolo in tijolos:
            tijolo_x, tijolo_y = tijolo
            desenhar_tijolo(tijolo_x, tijolo_y)

        # Exibir a pontuação
        fonte_pontuacao = pygame.font.Font(None, 36)
        texto_pontuacao = fonte_pontuacao.render(f"Pontuação: {pontuacao}", True, PRETO)
        posicao_texto_pontuacao = texto_pontuacao.get_rect(topright=(largura_tela - 10, 10))
        tela.blit(texto_pontuacao, posicao_texto_pontuacao)

        pygame.display.update()
        relogio.tick(60)


tela_inicial()
