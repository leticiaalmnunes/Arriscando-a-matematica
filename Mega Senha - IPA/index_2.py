import pygame
import time
import random as rd

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Jogo Mega Senha - Matemática")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 40, 30)
DARK_BLUE = (25, 25, 112)
BLUE_SOFT = (2, 114, 224, 0.85)
BLUE_DARK = (24, 33, 48)
SOFT_GREEN = (35, 95, 38)

# Fontes
try:
    font = pygame.font.Font('8bitOperatorPlusSC-Bold.ttf', 48)
    small_font = pygame.font.Font('8bitOperatorPlusSC-Bold.ttf', 28)
    title_font = pygame.font.Font('8bitOperatorPlusSC-Bold.ttf', 65)
except:
    font = pygame.font.SysFont('Arial', 48, bold=True)
    small_font = pygame.font.SysFont('Arial', 28, bold=True)
    title_font = pygame.font.SysFont('Arial', 65, bold=True)

# Carregar e preparar imagens
def load_and_fix_image(path):
    try:
        img = pygame.image.load(path)
        img = pygame.transform.rotate(img, 90)
        return pygame.transform.scale(img, (WIDTH, HEIGHT))
    except:
        surf = pygame.Surface((WIDTH, HEIGHT))
        surf.fill((20, 20, 50))
        return surf

victory_image = load_and_fix_image('vitoria.png')
defeat_image = load_and_fix_image('derrota.png')
cover_image = load_and_fix_image('megasenha.png')
background_image = load_and_fix_image('fundo.png')

# --- CONCEITOS ---
concepts_fundamental = [
    ("Adição", "Operação de somar valores."),
    ("Subtração", "Operação de retirar valores."),
    ("Multiplicação", "Soma repetida."),
    ("Divisão", "Repartição em partes iguais."),
    ("Contagem", "Ação de contar."),
    ("Sequência", "Números em ordem."),
    ("Antecessor", "Número anterior."),
    ("Sucessor", "Número seguinte."),
    ("Par", "Divisível por dois."),
    ("Ímpar", "Não divisível por dois."),
    ("Dobro", "Duas vezes."),
    ("Triplo", "Três vezes."),
    ("Metade", "Uma das duas partes."),
    ("Fração", "Representação de divisão."),
    ("Decimal", "Número com vírgula."),
    ("Inteiro", "Número sem parte decimal."),
    ("Natural", "Número positivo."),
    ("Medida", "Ato de medir."),
    ("Comprimento", "Distância."),
    ("Massa", "Quantidade de matéria."),
    ("Tempo", "Duração."),
    ("Relógio", "Instrumento do tempo."),
    ("Tabela", "Dados organizados."),
    ("Gráfico", "Representação visual."),
    ("Moda", "Valor mais frequente."),
    ("Média", "Valor central."),
    ("Ponto", "Indica posição."),
    ("Reta", "Linha infinita."),
    ("Segmento", "Parte da reta."),
    ("Ângulo", "Abertura entre retas."),
    ("Triângulo", "Figura de três lados."),
    ("Quadrado", "Quatro lados iguais."),
    ("Retângulo", "Lados opostos iguais."),
    ("Losango", "Quatro lados iguais."),
    ("Trapézio", "Dois lados paralelos."),
    ("Círculo", "Forma redonda."),
    ("Perímetro", "Soma dos lados."),
    ("Área", "Espaço interno."),
    ("Simetria", "Divisão equilibrada."),
    ("Cubo", "Sólido de seis faces."),
    ("Esfera", "Sólido redondo."),
    ("Cilindro", "Duas bases circulares."),
    ("Cone", "Base circular."),
    ("Volume", "Espaço ocupado."),
    ("Ordem", "Posição."),
    ("Comparação", "Análise de valores."),
    ("Maior", "Valor superior."),
    ("Menor", "Valor inferior."),
    ("Igual", "Mesmo valor."),
    ("Régua", "Instrumento de medida."),
    ("Compasso", "Desenha círculos."),
    ("Transferidor", "Mede ângulos."),
    ("Problema", "Situação a resolver."),
    ("Resultado", "Resposta final."),
]

concepts_medio = [
    ("Função", "Relação entre variáveis."),
    ("Afim", "Função do 1º grau."),
    ("Constante", "Valor fixo."),
    ("Linear", "Forma de reta."),
    ("Quadrática", "Função do 2º grau."),
    ("Parábola", "Gráfico da quadrática."),
    ("Vértice", "Ponto máximo ou mínimo."),
    ("Raízes", "Zeram a função."),
    ("Bhaskara", "Fórmula quadrática."),
    ("Exponencial", "Crescimento acelerado."),
    ("Logaritmo", "Inverso da exponencial."),
    ("Modular", "Distância até zero."),
    ("Crescente", "Valor aumenta."),
    ("Decrescente", "Valor diminui."),
    ("Trigonometria", "Estudo dos ângulos."),
    ("Seno", "Oposto pela hipotenusa."),
    ("Cosseno", "Adjacente pela hipotenusa."),
    ("Tangente", "Oposto pelo adjacente."),
    ("Pitágoras", "Relação dos lados."),
    ("Polígono", "Figura de lados."),
    ("Semelhança", "Mesma forma."),
    ("Congruência", "Mesma forma e tamanho."),
    ("Razão", "Resultado da divisão."),
    ("Proporção", "Igualdade de razões."),
    ("Progressão", "Sequência numérica."),
    ("Aritmética", "Razão constante."),
    ("Geométrica", "Razão multiplicativa."),
    ("Probabilidade", "Chance de ocorrer."),
    ("Evento", "Resultado possível."),
    ("Amostra", "Parte do todo."),
    ("Estatística", "Estudo de dados."),
    ("Histograma", "Distribuição gráfica."),
    ("Média", "Valor representativo."),
    ("Moda", "Mais frequente."),
    ("Mediana", "Valor central."),
    ("Equação", "Igualdade matemática."),
    ("Sistema", "Conjunto de equações."),
    ("Inequação", "Desigualdade."),
    ("Intervalo", "Conjunto numérico."),
    ("Conjunto", "Coleção de elementos."),
    ("União", "Junção de conjuntos."),
    ("Interseção", "Elementos comuns."),
    ("Disjunto", "Sem interseção."),
    ("Plano", "Superfície bidimensional."),
    ("Coordenadas", "Localização numérica."),
    ("Cartesiano", "Plano XY."),
    ("Inclinação", "Coeficiente angular."),
    ("Intercepto", "Corte no eixo."),
    ("Racional", "Número fracionário."),
    ("Irracional", "Decimal infinito."),
    ("Real", "Conjunto numérico."),
    ("Absoluto", "Valor sem sinal."),
]

concepts_graduação = [
    ("Limite", "Valor do qual uma função se aproxima infinitamente."),
    ("Derivada", "Taxa de variação instantânea ou inclinação da tangente."),
    ("Integral", "Operação que calcula a área sob uma curva."),
    ("Gradiente", "Vetor que aponta para a direção de máximo crescimento."),
    ("Divergente", "Operador que mede o fluxo de saída de um campo."),
    ("Rotacional", "Operador que mede a tendência de giro de um campo."),
    ("Jacobiano", "Determinante da matriz de derivadas parciais."),
    ("Hessiana", "Matriz das segundas derivadas parciais."),
    ("Laplaciano", "Divergente do gradiente de uma função escalar."),
    ("Wronskiano", "Determinante que testa independência linear de soluções."),
    ("Autovalor", "Escalar que satisfaz a equação característica."),
    ("Autovetor", "Vetor cuja direção não muda em uma transformação."),
    ("Matriz", "Arranjo retangular de números em linhas e colunas."),
    ("Determinante", "Número escalar associado a uma matriz quadrada."),
    ("Inversa", "Matriz que multiplicada pela original gera a identidade."),
    ("Transposta", "Matriz obtida trocando-se linhas por colunas."),
    ("Ortogonal", "Propriedade de vetores com produto escalar nulo."),
    ("Base", "Conjunto mínimo de vetores que gera um espaço."),
    ("Dimensão", "Número de vetores na base de um subespaço."),
    ("Núcleo", "Conjunto de vetores mapeados no vetor nulo."),
    ("Imagem", "Conjunto de todos os valores de saída de uma função."),
    ("Isomorfismo", "Mapeamento que preserva estrutura entre espaços."),
    ("Homeomorfismo", "Deformação contínua entre espaços topológicos."),
    ("Topologia", "Estudo de propriedades preservadas por deformações."),
    ("Convergência", "Propriedade de uma sequência que possui limite."),
    ("Divergência", "Sequência ou série que não tende a um limite finito."),
    ("Série", "Soma dos termos de uma sequência infinita."),
    ("Resíduo", "Valor importante no cálculo de integrais complexas."),
    ("Singularidade", "Ponto onde uma função não é analítica."),
    ("Holomorfa", "Função complexa que possui derivada."),
    ("Variedade", "Espaço que localmente se parece com o euclidiano."),
    ("Métrica", "Função que define a distância entre pontos."),
    ("Norma", "Função que define o comprimento de um vetor."),
    ("Hilbert", "Espaço vetorial completo com produto interno."),
    ("Banach", "Espaço vetorial normado e completo."),
    ("Compacto", "Conjunto que é fechado e limitado no R^n."),
    ("Conexo", "Espaço que não pode ser dividido em duas partes abertas."),
    ("Supremo", "O menor dos limites superiores de um conjunto."),
    ("Ínfimo", "O maior dos limites inferiores de um conjunto."),
    ("Fatorial", "Produto de todos os inteiros positivos até n."),
    ("Permutação", "Reordenamento dos elementos de um conjunto."),
    ("Probabilidade", "Medida da chance de um evento ocorrer."),
    ("Variância", "Medida de dispersão em relação à média."),
    ("Covariância", "Medida da variação conjunta de duas variáveis."),
    ("Correlação", "Grau de relação entre duas variáveis."),
    ("Esperança", "Valor médio ponderado de uma variável aleatória."),
    ("Histograma", "Representação gráfica de distribuição de frequências."),
    ("Interpolação", "Método de estimar valores entre pontos conhecidos."),
    ("Algoritmo", "Passo a passo lógico para resolver um problema."),
    ("Complexidade", "Custo de tempo ou memória de um algoritmo."),
    ("Teorema", "Afirmação matemática que foi provada logicamente."),
    ("Axioma", "Verdade matemática aceita sem necessidade de prova."),
    ("Corolário", "Consequência imediata de um teorema."),
    ("Lema", "Resultado auxiliar usado para provar um teorema."),
    ("Abstração", "Processo de isolar propriedades essenciais."),
    ("Difeomorfismo", "Mapeamento diferenciável com inversa diferenciável."),
    ("Tensor", "Objeto que generaliza escalares, vetores e matrizes."),
    ("Manifold", "Estrutura geométrica que generaliza curvas e superfícies."),
    ("Simetria", "Invariância sob um grupo de transformações."),
    ("Invariante", "Propriedade que não muda após uma operação."),
    ("Cauchy", "Sequência cujos termos se aproximam arbitrariamente."),
    ("Fourier", "Decomposição de sinais em ondas senoidais."),
    ("Laplace", "Transformada usada para resolver EDOs."),
    ("Poisson", "Distribuição usada para eventos raros no tempo."),
    ("Normal", "Distribuição em formato de sino ou Gaussiana."),
    ("Logaritmo", "Inverso da função exponencial."),
    ("Assíntota", "Reta da qual uma curva se aproxima sem tocar."),
    ("Parábola", "Seção cônica com excentricidade igual a um."),
    ("Elipse", "Lugar geométrico com soma das distâncias constante."),
    ("Hipérbole", "Lugar geométrico com diferença das distâncias constante."),
    ("Polo", "Tipo de singularidade isolada de uma função."),
    ("Dualidade", "Relação entre dois tipos de estruturas matemáticas."),
    ("Recursão", "Definição de algo em termos de si mesmo."),
    ("Iteração", "Repetição de um processo matemático."),
    ("Infinitésimo", "Quantidade menor que qualquer real positivo."),
    ("Cardinalidade", "Medida do número de elementos de um conjunto."),
    ("Ordinário", "Refere-se a EDOs que dependem de uma variável."),
    ("Parcial", "Refere-se a EDPs com múltiplas variáveis."),
    ("Harmônica", "Função que satisfaz a equação de Laplace."),
    ("Analítica", "Função que pode ser expressa como série de potências.")
]

levels = {"fundamental": concepts_fundamental, "medio": concepts_medio, "graduação": concepts_graduação}

def draw_rectangle_with_text(text, font, color, bg_color, border_color, surface, x, y, padding=20):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=(x + padding // 2, y + padding // 2))
    bubble_width = text_rect.width + padding
    bubble_height = text_rect.height + padding
    pygame.draw.rect(surface, border_color, (x, y, bubble_width, bubble_height), 4)
    pygame.draw.rect(surface, bg_color, (x + 4, y + 4, bubble_width - 8, bubble_height - 8))
    surface.blit(text_surface, text_rect)

def show_cover():
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load("musica.mp3")
        pygame.mixer.music.play(-1)
    except: pass
    
    waiting = True
    while waiting:
        screen.blit(cover_image, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: waiting = False

def choose_level():
    button_width, button_height = 500, 80
    # Valores de Y diminuídos para os botões subirem
    buttons = {
        "fundamental": pygame.Rect(WIDTH//2 - 250, 220, button_width, button_height),
        "medio": pygame.Rect(WIDTH//2 - 250, 340, button_width, button_height),
        "graduação": pygame.Rect(WIDTH//2 - 250, 460, button_width, button_height),
    }

    while True:
        screen.blit(background_image, (0, 0))
        
        # Desenha o Título no topo
        title_surf = title_font.render("Escolha o Nível do Jogo", True, WHITE)
        title_rect = title_surf.get_rect(center=(WIDTH//2, 100))
        screen.blit(title_surf, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        
        for nivel, rect in buttons.items():
            # Efeito visual de passar o mouse
            color = BLUE_SOFT if rect.collidepoint(mouse_pos) else BLUE_DARK
            pygame.draw.rect(screen, color, rect, border_radius=15)
            pygame.draw.rect(screen, WHITE, rect, 3, border_radius=15) # Borda branca
            
            # Texto do botão
            txt = font.render(nivel.capitalize(), True, WHITE)
            txt_rect = txt.get_rect(center=rect.center)
            screen.blit(txt, txt_rect)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for nivel, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        return nivel

def show_end_screen(img, music_file):
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
    except: pass
    
    waiting = True
    while waiting:
        screen.blit(img, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: waiting = False

def main():
    while True: # Loop que permite voltar para a capa
        show_cover()
        nivel_escolhido = choose_level()
        exemplos = rd.sample(levels[nivel_escolhido], len(levels[nivel_escolhido]))
        
        score = 0
        skips = 2
        idx = 0
        total_time = 90
        start_time = time.time()
        
        game_on = True
        while game_on:
            timer = max(0, total_time - int(time.time() - start_time))
            
            if score >= 4:
                show_end_screen(victory_image, "ayrton.mp3")
                game_on = False
                continue

            if timer <= 0:
                show_end_screen(defeat_image, "sad.mp3")
                game_on = False
                continue

            concept, hint = exemplos[idx % len(exemplos)]
            screen.blit(background_image, (0, 0))
            draw_rectangle_with_text(concept, font, WHITE, BLUE_SOFT, BLACK, screen, 50, 100)
            draw_rectangle_with_text(f"Dica: {hint}", small_font, WHITE, BLUE_DARK, WHITE, screen, 50, 250)
            draw_rectangle_with_text(f"Tempo: {timer}s", small_font, WHITE, RED, WHITE, screen, 400, 450)
            draw_rectangle_with_text(f"Acertos: {score}/4", small_font, WHITE, SOFT_GREEN, WHITE, screen, WIDTH - 300, 50)
            draw_rectangle_with_text(f"Pulos: {skips}/2 (P)", small_font, WHITE, BLUE_SOFT, WHITE, screen, WIDTH - 300, 150)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        score += 1
                        idx += 1
                    if event.key == pygame.K_p and skips > 0:
                        skips -= 1
                        idx += 1

if __name__ == "__main__":
    main()