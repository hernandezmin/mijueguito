import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_RED = (139, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aventura de Supervivencia")

def load_image(filename):
    return pygame.transform.scale(pygame.image.load(filename), (WIDTH, HEIGHT))

images = {
    "beach": load_image("playa.png"),
    "jungle": load_image("selva.png"),
    "fruits": load_image("frutas.png"),
    "fish": load_image("peces.png"),
    "shelter": load_image("cueva.png"),
    "water": load_image("agua.png"),
    "cover": load_image("cover1.png"),
    "apple": load_image("apple.png"),
    "mandarina": load_image("mandarina.png"),
    "avocado": load_image("avocado.png"),
    "trampa": load_image("trampa.png"),
    "rio": load_image("rio.png"),
    "madera": load_image("madera.png"),
    "hojas": load_image("hojas.png"),
    "paja": load_image("paja.png"),
    "path": load_image("path.png"),
    "animal": load_image("animal.png"),
    "cuerpo": load_image("muerte.png"),
    "piedra": load_image("muerte.png"),
    "wata": load_image("wata.png"),
    "shelter_building": load_image("shelter_building.png"),
    "hidden_cave": load_image("hidden_cave.png"),
    "firewood": load_image("firewood.png"),
    "forest_path": load_image("forest_path.png"),
    "mountain": load_image("mountain.png"),
    "ocean": load_image("ocean.png"),
    "shipwreck": load_image("shipwreck.png"),
    "bird_nest": load_image("bird_nest.png"),
    "coconut": load_image("coconut.png"),
    "rescue": load_image("rescue.png"),
    "no_rescue": load_image("no_rescue.png")
}

font = pygame.font.SysFont("Times New Roman", 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, DARK_RED)
    screen.blit(text_surface, (x, y))

def show_state(state):
    screen.fill(BLACK)
    if state in images:
        screen.blit(images[state], (0, 0))
    
    state_texts = {
        "start": [
            ("Naomi es una joven aventurera que, tras un naufragio, se encuentra sola", 30, 300),
            ("1. Explorar la playa", 50, 550),
            ("2. Adentrarse en la jungla", 50, 600)
        ],
        "beach": [
            ("Bien! llegaste a la playa. ¿Qué prefieres hacer?", 50, 150),
            ("1. Buscar comida a los alrededores", 50, 300),
            ("2. Buscar materiales y construir un refugio", 50, 340)
        ],
        "find_food": [
            ("Buena opción, es necesario conservar energia. ¿Qué tipo de comida buscas?", 50, 130),
            ("1. Buscar frutas en los arboles", 50, 160),
            ("2. Buscar agua para pescar", 50, 210)
        ],
        "find_fruits": [
            ("Encuentras un arbol con distintas frutas, ¿Cual tomas?", 50, 50),
            ("1. Manzanas verdes", 50, 100),
            ("2. Mandarinas algo amarillas", 50, 150),
            ("3. Aguacates color café", 50, 200)
        ],
        "take_apple": [
            ("Agarras una manzana, la comes y lamentablemente mueres", 50, 100)
        ],
        "take_mandarina": [
            ("Agarras una mandarina algo amarilla, agarras las pepitas", 50, 100),
            ("y las plantas y en pocos días crecen nuevas cosechas", 50, 150)
        ],
        "take_avocado": [
            ("Agarras un aguacate podrido y mueres", 50, 100)
        ],
        "fish": [
            ("1. Pescar con trampa", 50, 100),
            ("2. Meterte al río", 50, 150)
        ],
        "trampa": [
            ("Consigues el suficiente pescado para sobrevivir unos días", 50, 100)
        ],
        "rio": [
            ("En el río habían pirañas y mueres D:", 50, 100)
        ],
        "build_shelter": [
            ("Elige materiales: 1. Madera, 2. Hojas, 3. Paja", 50, 100)
        ],
        "madera": [
            ("Construiste un refugio muy resistente", 50, 100)
        ],
        "hojas": [
            ("Construiste un refugio muy débil y no resistió la tormenta", 50, 100)
        ],
        "paja": [
            ("Construiste un refugio resistente pero sin calor", 50, 100)
        ],
        "jungle": [
            ("Dentro de la jungla hay muchos peligros. ¿Qué decides?", 50, 100),
            ("1. Seguir el camino de tierra", 50, 150),
            ("2. Seguir el rastro de un animal", 50, 200)
        ],
        "path": [
            ("Siguiendo el camino te encuentras con una cueva oculta", 50, 100),
            ("1. Entrar en la cueva", 50, 150),
            ("2. Seguir el camino", 50, 200)
        ],
        "animal": [
            ("Sigues el rastro del animal. ¿Qué decides hacer ahora?", 50, 100),
            ("1. Intentar cazarlo", 50, 150),
            ("2. Observarlo a distancia", 50, 200)
        ],
        "cazar_animal": [
            ("Intentas cazar el animal, pero te encuentras con un peligro inesperado.", 50, 100),
            ("1. Luchar", 50, 150),
            ("2. Huir", 50, 200)
        ],
        "observar_animal": [
            ("Observas el animal y descubres un nuevo camino.", 50, 100),
            ("1. Seguir el camino", 50, 150),
            ("2. Regresar", 50, 200)
        ],
        "luchar": [
            ("Luchas valientemente, pero el animal es demasiado fuerte. Mueres.", 50, 100)
        ],
        "huir": [
            ("Huyes rápidamente y encuentras un nuevo camino.", 50, 100),
            ("1. Explorar el nuevo camino", 50, 150),
            ("2. Regresar a la selva", 50, 200)
        ],
        "nuevo_camino": [
            ("Exploras el nuevo camino y descubres una cueva.", 50, 100),
            ("1. Entrar en la cueva", 50, 150),
            ("2. Continuar explorando", 50, 200)
        ],
        "cave": [
            ("Dentro de la cueva hay materiales para hacer una fogata", 50, 100),
            ("1. Encender la fogata", 50, 150),
            ("2. Salir de la cueva", 50, 200)
        ],
        "forest_path": [
            ("Sigues el camino y encuentras una montaña", 50, 100),
            ("1. Subir la montaña", 50, 150),
            ("2. Seguir el camino", 50, 200)
        ],
        "mountain": [
            ("Subes la montaña y divisas un barco en el horizonte", 50, 100),
            ("1. Nadar hacia el barco", 50, 150),
            ("2. Gritar para llamar la atención", 50, 200)
        ],
        "ocean": [
            ("Te adentras en el océano y nadas hacia el barco", 50, 100),
            ("1. Intentar llegar al barco", 50, 150),
            ("2. Regresar a la playa", 50, 200)
        ],
        "shipwreck": [
            ("El barco naufragado está lleno de provisiones", 50, 100),
            ("1. Tomar provisiones", 50, 150),
            ("2. Seguir explorando el barco", 50, 200)
        ],
        "bird_nest": [
            ("Encuentras un nido de pájaro con huevos", 50, 100),
            ("1. Tomar los huevos", 50, 150),
            ("2. Dejar los huevos", 50, 200)
        ],
        "coconut": [
            ("Encuentras un coco y te hidratas", 50, 100)
        ],
        "rescue": [
            ("Felicidades! Has sido rescatado.", 50, 100)
        ],
        "no_rescue": [
            ("Nadie vino a rescatarte. Sigue intentando.", 50, 100)
        ]
    }
    
    if state in state_texts:
        for text, x, y in state_texts[state]:
            draw_text(text, x, y)

    pygame.display.flip()

def handle_event(event, state):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        state_transitions = {
            "start": {pygame.K_1: "beach", pygame.K_2: "jungle"},
            "beach": {pygame.K_1: "find_food", pygame.K_2: "build_shelter"},
            "find_food": {pygame.K_1: "find_fruits", pygame.K_2: "fish"},
            "find_fruits": {pygame.K_1: "take_apple", pygame.K_2: "take_mandarina", pygame.K_3: "take_avocado"},
            "fish": {pygame.K_1: "trampa", pygame.K_2: "rio"},
            "build_shelter": {pygame.K_1: "madera", pygame.K_2: "hojas", pygame.K_3: "paja"},
            "jungle": {pygame.K_1: "path", pygame.K_2: "animal"},
            "path": {pygame.K_1: "cave", pygame.K_2: "forest_path"},
            "animal": {pygame.K_1: "cazar_animal", pygame.K_2: "observar_animal"},
            "cazar_animal": {pygame.K_1: "luchar", pygame.K_2: "huir"},
            "observar_animal": {pygame.K_1: "nuevo_camino", pygame.K_2: "jungle"},
            "nuevo_camino": {pygame.K_1: "cave", pygame.K_2: "forest_path"},
            "cave": {pygame.K_1: "firewood", pygame.K_2: "forest_path"},
            "forest_path": {pygame.K_1: "mountain", pygame.K_2: "ocean"},
            "mountain": {pygame.K_1: "ocean", pygame.K_2: "rescue"},
            "ocean": {pygame.K_1: "shipwreck", pygame.K_2: "beach"},
            "shipwreck": {pygame.K_1: "bird_nest", pygame.K_2: "coconut"},
            "bird_nest": {pygame.K_1: "rescue", pygame.K_2: "no_rescue"},
        }

        if state in state_transitions and event.key in state_transitions[state]:
            return state_transitions[state][event.key]
        elif state in ["take_apple", "take_mandarina", "take_avocado", "trampa", "rio", "madera", "hojas", "paja", "luchar", "huir", "coconut", "rescue", "no_rescue"]:
            return "start"

    return state

state = "start"

while True:
    for event in pygame.event.get():
        state = handle_event(event, state)
    
    show_state(state)