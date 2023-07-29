import pygame, random, time

# configuração da tela
largura_tela = 800
altura_tela = 600
tamanho_celula = 40

# inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("labirinto")
clock = pygame.time.Clock()

# criação do labirinto com função recursiva. Função utilizando o algoritmo de busca em profundidade
def cria_labirinto(a, b):
    labirinto[a][b] = 1
    direcao = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(direcao)
    for ab, ba in direcao:
        x, y = a + ab, b + ba
        if x >= 0 and x < largura_labirinto and y >= 0 and y < altura_labirinto and labirinto[x][y] == 0:
            labirinto[a + ab // 2][b + ba // 2] = 1
            cria_labirinto(x, y)

# configuração do labirinto
largura_labirinto = largura_tela // tamanho_celula
altura_labirinto = altura_tela // tamanho_celula

# cria matriz do labirinto
labirinto = [[0] * altura_labirinto for _ in range(largura_labirinto)]

# Cria as surfaces para os elementos do labirinto
parabens = pygame.image.load('graficos/parabens.png').convert_alpha()
background = pygame.image.load('graficos/route216.png').convert_alpha()
grass_horizontal = pygame.image.load('graficos/grass.png').convert_alpha()
player = pygame.image.load('graficos/guto.png').convert_alpha()
superficie_g = pygame.image.load('graficos/pokeball.png').convert_alpha()
background2 = pygame.image.load('graficos/Maze.png').convert_alpha()

# cria o labirinto
cria_labirinto(0, 0)

# posição inicial do jogador
jogador_x = 0
jogador_y = 0

# encontra um lugar válido para o destino final
lugar_valido = []
for i in range(altura_labirinto):
    for j in range(largura_labirinto):
        if labirinto[j][i] == 1:
            lugar_valido.append((j, i))
saida_x, saida_y = random.choice(lugar_valido)

#exibe tela inicial por 2 segundos
background2 = pygame.transform.scale(background2, (800, 600))
tela.blit(background2, (0, 0))
pygame.display.flip()
pygame.time.wait(2000)

# loop principal do jogo
rodando = True
fim = False
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jogador_x > 0 and labirinto[jogador_x - 1][jogador_y] == 1:
        jogador_x -= 1
    if keys[pygame.K_RIGHT] and jogador_x < largura_labirinto - 1 and labirinto[jogador_x + 1][jogador_y] == 1:
        jogador_x += 1
    if keys[pygame.K_UP] and jogador_y > 0 and labirinto[jogador_x][jogador_y - 1] == 1:
        jogador_y -= 1
    if keys[pygame.K_DOWN] and jogador_y < altura_labirinto - 1 and labirinto[jogador_x][jogador_y + 1] == 1:
        jogador_y += 1

    # fundo da tela
    tela.blit(background, (0, 0))

    # desenha o labirinto
    for i in range(largura_labirinto):
        for j in range(altura_labirinto):
            if labirinto[i][j] == 0:
                tela.blit(grass_horizontal, (i * tamanho_celula, j * tamanho_celula, tamanho_celula, tamanho_celula))

    # desenha o jogador
    tela.blit(player, (jogador_x * tamanho_celula, jogador_y * tamanho_celula, tamanho_celula, tamanho_celula))

    # desenha a saída
    tela.blit(superficie_g, (saida_x * tamanho_celula, saida_y * tamanho_celula, tamanho_celula, tamanho_celula))

    # verifica se o jogador chegou à saída
    if jogador_x == saida_x and jogador_y == saida_y:
        tela.blit(parabens, (0,0))
        pygame.display.flip()
        rodando = False
        pygame.time.wait(2000)
    
    # atualiza a tela
    pygame.display.flip()

    # velocidade do jogador
    clock.tick(10)

# Encerra o Pygame
pygame.quit()
