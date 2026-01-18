import pygame
import time
import random as rd

# Inicializa o Pygame
pygame.init()

# Configurações da tela em modo tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Jogo Mega Senha - Matemática")

# Cores
LIGHT_BLUE = (173, 216, 230)
SOFT_YELLOW = (255, 255, 204)
SOFT_PINK = (255, 182, 193)
SOFT_GREEN = (35, 95, 38, 0.85)
WHITE = (255, 255, 255)
DARK_BLUE = (25, 25, 112)
BLUE_SOFT = (75, 0, 130)
BLACK = (0, 0, 0)
RED = (255, 40, 30)
GREEN = (35, 95, 38, 0.85)
BLUE_SOFT = (2,114,224, 0.85)
BLUE_DARK = (24,33,48)


# Fonte estilizada
font = pygame.font.Font('8bitOperatorPlusSC-Bold.ttf', 48)
small_font = pygame.font.Font('8bitOperatorPlusSC-Bold.ttf', 28)

# Carregar imagens
victory_image = pygame.image.load('vitoria.png')
defeat_image = pygame.image.load('derrota.png')
cover_image = pygame.image.load('megasenha.png')

# Carregar a imagem de fundo
background_image = pygame.image.load('fundo.png')
background_image = pygame.transform.rotate(background_image, 90)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Rotacionar as imagens de vitória e derrota
victory_image = pygame.transform.rotate(victory_image, 90)
victory_image = pygame.transform.scale(victory_image, (WIDTH, HEIGHT))

defeat_image = pygame.transform.rotate(defeat_image, 90)
defeat_image = pygame.transform.scale(defeat_image, (WIDTH, HEIGHT))

# Escala a imagem de capa para preencher toda a tela
cover_image = pygame.transform.rotate(cover_image, 90)
cover_image = pygame.transform.scale(cover_image, (WIDTH, HEIGHT))

# Função para mostrar texto na tela
def draw_text(text, font, color, surface, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    for line in lines:
        textobj = font.render(line, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        y += font.get_height()

# Função para desenhar a borda retangular em torno de um texto
def draw_rectangle_with_text(text, font, color, bg_color, border_color, surface, x, y, padding=20):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x + padding // 2, y + padding // 2)

    bubble_width = text_rect.width + padding
    bubble_height = text_rect.height + padding

    # Desenhar a borda retangular
    pygame.draw.rect(surface, border_color, (x, y, bubble_width, bubble_height), 4)  # Borda roxa
    pygame.draw.rect(surface, bg_color, (x + 4, y + 4, bubble_width - 8, bubble_height - 8))  # Fundo

    surface.blit(text_surface, text_rect)

# Tela de capa
def show_cover():
    pygame.mixer.music.stop() 
    pygame.mixer.init()  # Inicializa o mixer de áudio
    pygame.mixer.music.load("musica.mp3")  # Carrega sua música
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume (0.0 a 1.0)
    pygame.mixer.music.play(-1)
    
    screen.blit(cover_image, (0, 0))  # Exibe a imagem da capa
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Inicia o jogo ao pressionar Enter
                    waiting = False

concepts = [
    ("Parábola", "Curva em forma de U que aparece em funções quadráticas."),
("Exponencial", "Função que cresce ou diminui muito rápido."),
("Vértice", "Ponto mais alto ou mais baixo da parábola."),
("Aresta", "Lado de um polígono que conecta dois pontos."),
("Face", "Superfície plana de um sólido, como um cubo."),
("Figuras geométricas", "Formas como triângulos e quadrados."),
("Polígonos", "Figuras com vários lados, como pentágonos."),
("Triângulo retângulo", "Triângulo com um ângulo de 90 graus."),
("Proporção", "Comparação entre duas razões."),
("Bhaskara", "Usada para encontrar as raízes de uma equação quadrática."),
("Raízes", "Valores que tornam uma função igual a zero."),
("Constante", "Função que sempre dá o mesmo resultado."),
("Afim", "Função linear simples, como f(x) = ax + b."),
("polinomial", "Função que envolve potências de x."),
("Linear", "Função que forma uma linha reta no gráfico."),
("Função crescente", "Função que sobe quando x aumenta."),
("Função decrescente", "Função que desce quando x aumenta."),
("Função modular", "Função que mostra a distância de x a zero."),
("Função logarítmica", "Função que é o inverso da exponencial."),
("Funções trigonométricas", "Funções que lidam com ângulos e triângulos."),
("Função raiz", "Função que calcula a raiz quadrada."),
("Equilátero", "Triângulo com todos os lados iguais."),
("Isósceles", "Triângulo com dois lados iguais."),
("Escaleno", "Triângulo com todos os lados diferentes."),
("Circunscrito", "Triângulo que envolve um círculo."),
("Poliedros", "Sólidos com várias faces planas."),
("Circunferência", "Contorno de um círculo."),
("Área", "Espaço dentro de uma figura geométrica"),
("Trigonometria", "Relações entre ângulos de um triângulo."),
("Bissetriz", "Segmento que divide um ângulo ao meio."),
("Baricentro", "Ponto onde se encontram as medianas do triângulo."),
("União", "Conjunto que reúne todos os elementos."),
("Intersecção", "Conjunto com os elementos que se repetem."),
("Matriz", "Tabela de números organizados em linhas e colunas."),
("Reto", "Ângulo que mede exatamente 90 graus."),
("Agudo", "Ângulo menor que 90 graus."),
("Obtuso", "Ângulo maior que 90 graus e menor que 180."),
("Ângulos complementares", "Dois ângulos que somam 90 graus."),
("Ângulos suplementares", "Dois ângulos que somam 180 graus."),
("Conjunto Vazio", "Conjunto que não tem elementos."),
("Conjuntos Disjuntos", "Conjuntos que não compartilham elementos."),
("Régua", "Ferramentas para desenhar e medir."),
("Ábaco", "Antigo instrumento para fazer contas."),
("Transferidor", "Ferramenta para medir ângulos."),
("Paralelepípedo", "Sólido com seis faces retangulares."),
("Compasso", "Instrumento utilizado para desenhar circunferências."),
("Dodecaedro", "Sólido com doze faces."),
("Elipse", "Se assemelha a uma figura oval."),
("Histograma", "Gráfico que mostra a distribuição de dados."),
("Teorema de Pitágoras", "Relação entre os lados de um triângulo retângulo."),
("Complexos", "Números que têm uma parte real e uma imaginária."),
("Naturais", "Números inteiros e positivos"),
("Inteiros", "Números que não são quebrados"),
("Matriz Transposta", "Matriz obtida virando linhas em colunas."),
("Matriz Identidade", "Matriz que não muda os resultados na multiplicação."),
("Matriz Nula", "Matriz cheia de zeros."),
("Matriz Diagonal", "Matriz com valores apenas na diagonal principal."),
("Matriz Simétrica", "Matriz que é igual ao seu espelho."),
("Matriz Inversa", "Matriz que reverte o efeito da multiplicação."),
("Divisão", "Operação inversa da Multiplicação."), 
("Multiplicação", "Somas consecutivas de um mesmo elemento."),
("Potênciação", "Multiplicações consecutivas de um mesmo elemento."),
("Matriz","Organização de elementos em forma tabelar."),
("Fração","Outra maneira de representar divisão."),
("Múltiplo","Produto de dois números inteiros."),
("Razão","Resultado de uma divisão."),
("Cosseno","Cateto adjacente dividido pela hipotenusa."),
("Seno","Cateto oposto dividido pela hipotenusa."),
("Tangente","Cateto oposto dividido pelo cateto adjacente."),
("Geometria","Estudo de formas geométricas."),
("Probabilidade","A chance de um evento acontecer."),
("Moda","O valor que mais aparece em uma sequêncianumérica."),
("Mediana","O valor central de uma sequência númerica."),
("Média","O valor médio de uma sequência numérica."),
]


# Tela de vitória
def show_win_screen():
    screen.blit(victory_image, (0, 0))  # Exibe a imagem de vitória
    pygame.display.flip()
    pygame.mixer.music.stop() 
    pygame.mixer.init()  # Inicializa o mixer de áudio
    pygame.mixer.music.load("ayrton.mp3")  # Carrega sua música
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume (0.0 a 1.0)
    pygame.mixer.music.play(-1)  # Toca a música em loop (-1 significa loop infinito)



    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Retorna à tela inicial ao pressionar Enter
                    waiting = False
                    return True  # Retorna True para indicar que deve mostrar a tela inicial

# Tela de derrota
def show_defeat_screen():
    screen.blit(defeat_image, (0, 0))  # Exibe a imagem de derrota
    pygame.display.flip()
    pygame.mixer.music.stop() 
    pygame.mixer.init()  # Inicializa o mixer de áudio
    pygame.mixer.music.load("sad.mp3")  # Carrega sua música
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume (0.0 a 1.0)
    pygame.mixer.music.play(1)  # Toca a música em loop (-1 significa loop infinito)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Retorna à tela inicial ao pressionar Enter
                    waiting = False
                    return True  # Retorna True para indicar que deve mostrar a tela inicial


# Função principal do jogo
def main():  
    show_cover()  # Mostra a capa antes de começar o jogo


    running = True
    score = 0
    skips = 2
    current_concept_index = 0
    start_time = time.time()  # Marca o tempo inicial de 2 minutos
    total_game_time = 90  # Tempo total de jogo (2 minutos)
    max_attempts = 3  # Número máximo de tentativas para adivinhar

    exemplos = rd.sample(concepts, 7)

    while running:
        if score == 4:
            if show_win_screen():
                show_cover()  # Retorna à tela inicial após vencer
                exemplos = rd.sample(concepts, 6)
                score = 0  # Reinicia o score se desejar
                skips = 2  # Reinicia os skips se desejar
                current_concept_index = 0  # Reinicia o índice de conceitos
                start_time = time.time()

        if time.time() - start_time >= total_game_time:
            if show_defeat_screen():
                show_cover()  # Retorna à tela inicial após perder
                exemplos = rd.sample(concepts, 6)
                score = 0  # Reinicia o score se desejar
                skips = 2  # Reinicia os skips se desejar
                current_concept_index = 0  # Reinicia o índice de conceitos
                start_time = time.time()

        if current_concept_index >= len(exemplos):
            current_concept_index = 0  # Reiniciar a lista de conceitos se necessário

        concept, hint = exemplos[current_concept_index]

        # Exibe a tela de jogo
        screen.blit(background_image, (0, 0))  # Mantém a imagem de fundo durante o jogo
        draw_rectangle_with_text( concept, font, WHITE, BLUE_SOFT, BLACK, screen, 50, 100)
        draw_rectangle_with_text("Dica: " + hint, small_font, WHITE, BLUE_DARK, DARK_BLUE, screen, 50, 250)
        remaining_time = max(0, total_game_time - int(time.time() - start_time))

        # Mover o cronômetro para a direita
        draw_rectangle_with_text("Tempo restante: " + str(remaining_time) + " segundos", small_font, WHITE, RED, DARK_BLUE, screen, 400, 450)

        draw_rectangle_with_text("Acertos: " + str(score) + "/4", small_font, WHITE, SOFT_GREEN, DARK_BLUE, screen, 1000, 10)

        # Ajustar e centralizar o botão de Pular
        draw_rectangle_with_text("Pulos: " + str(skips) + "/2", small_font, WHITE, BLUE_SOFT, DARK_BLUE, screen, 1000, 530)

        pygame.display.flip()

        # Lógica de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Pressione Enter para acertar automaticamente
                    score += 1
                    current_concept_index += 1  # Avança para o próximo conceito

            if event.type == pygame.KEYDOWN:  # Verifica se o evento é de pressionar uma tecla
                     if event.key == pygame.K_p and skips > 0:  # Verifica se a tecla 'P' foi pressionada
                                skips -= 1
                                current_concept_index += 1  # Avança para o próximo conceito ao pular
    pygame.mixer.music.stop() 
    pygame.quit()

if __name__ == "__main__":
    main()
