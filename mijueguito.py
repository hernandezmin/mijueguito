import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aventura de Supervivencia")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

img_beach = pygame.image.load("playa.png")
img_jungle = pygame.image.load("Selva.png")
img_fruits = pygame.image.load("food.png")
img_fish = pygame.image.load("peces.png")
img_shelter = pygame.image.load("cueva.png")
img_water = pygame.image.load("agua.png")
img_cover = pygame.image.load("cover1.png")
img_frutas = pygame.image.load("frutas.png")
img_apple = pygame.image.load("apple.png")
img_mandarina = pygame.image.load("mandarina.png")
img_avocado = pygame.image.load("avocado.png")
img_trampa = pygame.image.load("trampa.png")
img_rio = pygame.image.load("rio.png")
img_madera = pygame.image.load("madera.png")
img_hojas= pygame.image.load("hojas.png")
img_paja = pygame.image.load("paja.png")
img_path = pygame.image.load("path.png")
img_animal =pygame.image.load("animal.png") 

img_beach = pygame.transform.scale(img_beach, (WIDTH, HEIGHT))
img_jungle = pygame.transform.scale(img_jungle, (WIDTH, HEIGHT))
img_fruits = pygame.transform.scale(img_fruits, (WIDTH, HEIGHT))
img_fish = pygame.transform.scale(img_fish, (WIDTH, HEIGHT))
img_shelter = pygame.transform.scale(img_shelter, (WIDTH, HEIGHT))
img_water = pygame.transform.scale(img_water, (WIDTH, HEIGHT))
img_cover = pygame.transform.scale(img_cover, (WIDTH, HEIGHT))
img_apple = pygame.transform.scale(img_apple, (WIDTH, HEIGHT))
img_mandarina = pygame.transform.scale(img_mandarina, (WIDTH, HEIGHT))
img_avocado = pygame.transform.scale(img_avocado, (WIDTH, HEIGHT))
img_trampa = pygame.transform.scale(img_trampa, (WIDTH, HEIGHT))
img_rio = pygame.transform.scale(img_rio, (WIDTH, HEIGHT))
img_madera = pygame.transform.scale(img_madera, (WIDTH, HEIGHT))
img_hojas = pygame.transform.scale(img_hojas, (WIDTH, HEIGHT))
img_paja = pygame.transform.scale(img_paja, (WIDTH, HEIGHT))
img_path = pygame.transform.scale(img_path, (WIDTH, HEIGHT))
img_animal = pygame.transform.scale(img_animal, (WIDTH, HEIGHT))

font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def show_state(state):
    screen.fill(WHITE)
    if state == "start":
        screen.blit(img_cover, (0, 0))
        draw_text("Naomi es una joven aventurera que, tras un naufragio, se encuentra sola", 30, 300)
        draw_text("en una isla desierta. Desorientada, despierta en una playa de arena blanca", 30, 330)
        draw_text("rodeada de selva espesa. Con el eco de la tormenta aún resonando en sus oídos,", 30, 360)
        draw_text("comienza a explorar la isla, enfrentándose a desafíos y peligros mientras", 30, 390)
        draw_text("busca una manera de sobrevivir y, eventualmente, regresar a casa", 30 , 420)
        draw_text("1. Explorar la playa", 50, 550)
        draw_text("2. Adentrarse en la jungla", 50, 600)
    elif state == "beach":
        screen.blit(img_beach, (0, 0))
        draw_text("Bien! llegaste a la playa, el viento está lo suficientemente", 50, 150)
        draw_text("fuerte cómo para no dejarte ver, Que prefieres hacer?", 50, 180)
        draw_text("1. Buscar comida a los alrededores", 50, 300)
        draw_text("2. Buscar materiales y construir un refugio", 50, 340)
    elif state == "find_food":
        screen.blit(img_fruits, (0, 0))
        draw_text("Buena opción, es necesario conservar energia, no sabes", 50, 100)
        draw_text("cuanto tiempo pasaras aqui ¿Qué tipo de comida buscas?", 50, 130 )
        draw_text("1. Buscar frutas en los arboles", 50, 160)
        draw_text("2. Buscar agua para pescar", 50, 210)
    elif state == "find_fruits":
        screen.blit(img_frutas, (0, 0))
        draw_text("Encuentras un arbol con distintas frutas, ¿Cual tomas?", 50, 50)
        draw_text("1. Manzanas verdes", 50, 100)
        draw_text("2. Mandarinas algo amarillas", 50, 150)
        draw_text("3. Aguacates color café", 50, 200)
    elif state == "take_apple":
        screen.blit(img_apple, (0, 0))
        draw_text("Agarras una manzana, la comes y lamentablemente mueres", 50, 100)
    elif state == "take_mandarina":
        screen.blit(img_mandarina, (0, 0))
        draw_text("Agarras una mandarina algo amarilla, agarras las pepitas", 50, 100)
        draw_text("y las plantas y en pocos días crecen nuevas cosechas", 50, 150)
    elif state == "take_avocado":
        screen.blit(img_avocado, (0, 0))
        draw_text("Agarras un aguacate podrido y mueres", 50, 100)
    elif state == "fish":
        screen.blit(img_fish, (0, 0))
        draw_text("1. Pescar con trampa", 50, 100)
        draw_text("2. Meterte al río", 50, 150)
    elif state == "trampa":
        screen.blit(img_trampa, (0, 0))
        draw_text("Consigues el suficiente pescado para sobrevivir unos días", 50, 100)
    elif state == "rio":
        screen.blit(img_rio, (0, 0))
        draw_text("En el río habían pirañas y mueres D:", 50, 100)
    elif state == "build_shelter":
        screen.blit(img_shelter, (0, 0))
        draw_text("Elige materiales: 1. Madera, 2. Hojas, 3. Paja", 50, 100)
    elif state == "madera":
        screen.blit(img_madera, (0, 0))
        draw_text("Construyes un refugio y sobrevives", 50, 100)
    elif state == "hojas":
        screen.blit(img_hojas, (0, 0))
        draw_text("No es lo suficientemente fuerte y mueres de frio", 50, 100)
    elif state == "paja":
        screen.blit(img_paja, (0, 0))
        draw_text("Construyes una casa pero no lo suficientemente fuerte y te", 50, 100)
        draw_text("matan los animales alrededor", 50, 140)
    elif state == "jungle":
        screen.blit(img_jungle, (0, 0))
        draw_text("¿Qué prefieres hacer primero?", 50, 100)
        draw_text("1. Seguir un sendero", 50, 150)
        draw_text("2. Buscar una fuente de agua", 50, 200)
    elif state == "follow_path":
        screen.blit(img_path, (0, 0))
        draw_text("¿Wow! huellas, Qué decides hacer?", 50, 100)
        draw_text("1. Cazar un animal", 50, 150)
        draw_text("2. Seguir las huellas hasta una fuente de agua", 50, 200)
    elif state == "hunt_animal":
        screen.blit(img_animal, (0, 0))
        draw_text("1. Cazar cuerpo a cuerpo o 2. Tirarle piedras hasta matarlo", 50, 50)
    elif state == "find_water_source":
        screen.blit(img_water, (0, 0))
        draw_text("Encuentras una fuente de agua y sobrevives", 50, 100)
    elif state == "find_water":
        draw_text("Encuentras una civilización caníbal y mueres", 50, 50)
    pygame.display.flip()

def ask_question(question):
    screen.fill(WHITE)
    draw_text(question, 50, 250)
    draw_text("1. Sí", 50, 300)
    draw_text("2. No", 50, 350)
    pygame.display.flip()

def game():
    state = "start"
    
    questions = [
        "¿Te gusta explorar?",
        "¿Tienes miedo a la oscuridad?",
        "¿Prefieres el calor o el frío?",
        "¿Eres bueno construyendo cosas?",
        "¿Te gustan los animales salvajes?"
    ]
    random.shuffle(questions)

    question_counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if state == "start":
                        state = "beach"
                    elif state == "beach":
                        state = "find_food"
                    elif state == "find_food":
                        state = "find_fruits"
                    elif state == "find_fruits":
                        state = "take_apple"
                    elif state == "build_shelter":
                        state = "madera"
                    elif state == "jungle":
                        state = "follow_path"
                    elif state == "follow_path":
                        state = "hunt_animal"
                    elif state == "fish":
                        state = "trampa"
                elif event.key == pygame.K_2:
                    if state == "start":
                        state = "jungle"
                    elif state == "beach":
                        state = "build_shelter"
                    elif state == "find_food":
                        state = "fish"
                    elif state == "find_fruits":
                        state = "take_mandarina"
                    elif state == "build_shelter":
                        state = "hojas"
                    elif state == "jungle":
                        state = "find_water"
                    elif state == "follow_path":
                        state = "find_water_source"
                    elif state == "fish":
                        state = "rio"
                elif event.key == pygame.K_3:
                    if state == "find_fruits":
                        state = "take_avocado"
                    elif state == "build_shelter":
                        state = "paja"

        if state == "start" and question_counter < len(questions):
            ask_question(questions[question_counter])
            question_counter += 1
        else:
            show_state(state)

        pygame.display.flip()

game()
