import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aventura de Supervivencia")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



img_beach = pygame.image.load("playa.png")
img_jungle = pygame.image.load("selva.png")
img_fruits = pygame.image.load("frutas.png")
img_fish = pygame.image.load("peces.png")
img_shelter = pygame.image.load("cueva.png")
img_water = pygame.image.load("agua.png")
img_cover = pygame.image.load("cover1.png") 
img_apple = pygame.image.load("apple.png")
img_mandarina = pygame.image.load("mandarina.png")
img_avocado = pygame.image.load("avocado.png")
img_trampa = pygame.image.load("trampa.png")
img_rio = pygame.image.load("rio.png")
img_madera = pygame.image.load("madera.png")
img_hojas = pygame.image.load("hojas.png")
img_paja = pygame.image.load("paja.png")
img_path = pygame.image.load("path.png")
img_animal = pygame.image.load("animal.png")
img_cuerpo = pygame.image.load("muerte.png")
img_piedra = pygame.image.load("muerte.png")
img_wata = pygame.image.load("wata.png") 
img_shelter_building = pygame.image.load("shelter_building.png")
img_hidden_cave = pygame.image.load("hidden_cave.png")
img_firewood = pygame.image.load("firewood.png")
img_forest_path = pygame.image.load("forest_path.png")
img_mountain = pygame.image.load("mountain.png")
img_ocean = pygame.image.load("ocean.png")
img_shipwreck = pygame.image.load("shipwreck.png")
img_bird_nest = pygame.image.load("bird_nest.png")
img_coconut = pygame.image.load("coconut.png")
img_rescue = pygame.image.load("rescue.png")
img_no_rescue = pygame.image.load("no_rescue.png")


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
img_cuerpo = pygame.transform.scale(img_cuerpo, (WIDTH, HEIGHT))
img_piedra = pygame.transform.scale(img_piedra, (WIDTH, HEIGHT))
img_wata = pygame.transform.scale(img_wata, (WIDTH, HEIGHT))
img_shelter_building = pygame.transform.scale(img_shelter_building, (WIDTH, HEIGHT))
img_hidden_cave = pygame.transform.scale(img_hidden_cave, (WIDTH, HEIGHT))
img_firewood = pygame.transform.scale(img_firewood, (WIDTH, HEIGHT))
img_forest_path = pygame.transform.scale(img_forest_path, (WIDTH, HEIGHT))
img_mountain = pygame.transform.scale(img_mountain, (WIDTH, HEIGHT))
img_ocean = pygame.transform.scale(img_ocean, (WIDTH, HEIGHT))
img_shipwreck = pygame.transform.scale(img_shipwreck, (WIDTH, HEIGHT))
img_bird_nest = pygame.transform.scale(img_bird_nest, (WIDTH, HEIGHT))
img_coconut = pygame.transform.scale(img_coconut, (WIDTH, HEIGHT))
img_rescue = pygame.transform.scale(img_rescue, (WIDTH, HEIGHT))
img_no_rescue = pygame.transform.scale(img_no_rescue, (WIDTH, HEIGHT))


font = pygame.font.SysFont("Times New Roman", 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

def show_state(state):
    screen.fill(BLACK)
    if state == "start":
        screen.blit(img_cover, (0, 0))
        draw_text("Naomi es una joven aventurera que, tras un naufragio, se encuentra sola", 30, 300)
        draw_text("en una isla desierta. Desorientada, despierta en una playa de arena blanca", 30, 330)
        draw_text("rodeada de selva espesa. Con el eco de la tormenta aún resonando en sus oídos,", 30, 360)
        draw_text("comienza a explorar la isla, enfrentándose a desafíos y peligros mientras", 30, 390)
        draw_text("busca una manera de sobrevivir y, eventualmente, regresar a casa", 30, 420)
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
        draw_text("cuanto tiempo pasaras aqui ¿Qué tipo de comida buscas?", 50, 130)
        draw_text("1. Buscar frutas en los arboles", 50, 160)
        draw_text("2. Buscar agua para pescar", 50, 210)
    elif state == "find_fruits":
        screen.blit(img_fruits, (0, 0))
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
        screen.blit(img_shelter_building, (0, 0))
        draw_text("Elige materiales: 1. Madera, 2. Hojas, 3. Paja", 50, 100)
    elif state == "madera":
        screen.blit(img_madera, (0, 0))
        draw_text("Construiste un refugio muy resistente", 50, 100)
    elif state == "hojas":
        screen.blit(img_hojas, (0, 0))
        draw_text("Construiste un refugio muy débil y no resistió la tormenta", 50, 100)
    elif state == "paja":
        screen.blit(img_paja, (0, 0))
        draw_text("Construiste un refugio resistente pero sin calor", 50, 100)
    elif state == "jungle":
        screen.blit(img_jungle, (0, 0))
        draw_text("Dentro de la jungla hay muchos peligros. ¿Qué decides?", 50, 100)
        draw_text("1. Seguir el camino de tierra", 50, 150)
        draw_text("2. Seguir el rastro de un animal", 50, 200)
    elif state == "path":
        screen.blit(img_path, (0, 0))
        draw_text("Siguiendo el camino te encuentras con una cueva oculta", 50, 100)
        draw_text("1. Entrar en la cueva", 50, 150)
        draw_text("2. Seguir el camino", 50, 200)
    elif state == "animal":
        screen.blit(img_animal, (0, 0))
        draw_text("Sigues el rastro del animal. ¿Qué decides hacer ahora?", 50, 100)
        draw_text("1. Intentar cazarlo", 50, 150)
        draw_text("2. Observarlo a distancia", 50, 200)
    elif state == "cazar_animal":
        screen.blit(img_animal, (0, 0))
        draw_text("Intentas cazar el animal, pero te encuentras con un peligro inesperado.", 50, 100)
        draw_text("1. Luchar", 50, 150)
        draw_text("2. Huir", 50, 200)
    elif state == "observar_animal":
        screen.blit(img_animal, (0, 0))
        draw_text("Observas el animal y descubres un nuevo camino.", 50, 100)
        draw_text("1. Seguir el camino", 50, 150)
        draw_text("2. Regresar", 50, 200)
    elif state == "luchar":
        screen.blit(img_cuerpo, (0, 0))
        draw_text("Luchas valientemente, pero el animal es demasiado fuerte. Mueres.", 50, 100)
    elif state == "huir":
        screen.blit(img_path, (0, 0))
        draw_text("Huyes rápidamente y encuentras un nuevo camino.", 50, 100)
        draw_text("1. Explorar el nuevo camino", 50, 150)
        draw_text("2. Regresar a la selva", 50, 200)
    elif state == "nuevo_camino":
        screen.blit(img_forest_path, (0, 0))
        draw_text("Exploras el nuevo camino y descubres una cueva.", 50, 100)
        draw_text("1. Entrar en la cueva", 50, 150)
        draw_text("2. Continuar explorando", 50, 200)
    elif state == "cave":
        screen.blit(img_hidden_cave, (0, 0))
        draw_text("Dentro de la cueva hay materiales para hacer una fogata", 50, 100)
        draw_text("1. Encender la fogata", 50, 150)
        draw_text("2. Salir de la cueva", 50, 200)
    elif state == "forest_path":
        screen.blit(img_forest_path, (0, 0))
        draw_text("Sigues el camino y encuentras una montaña", 50, 100)
        draw_text("1. Subir la montaña", 50, 150)
        draw_text("2. Seguir el camino", 50, 200)
    elif state == "mountain":
        screen.blit(img_mountain, (0, 0))
        draw_text("Subes la montaña y divisas un barco en el horizonte", 50, 100)
        draw_text("1. Nadar hacia el barco", 50, 150)
        draw_text("2. Gritar para llamar la atención", 50, 200)
    elif state == "ocean":
        screen.blit(img_ocean, (0, 0))
        draw_text("Te adentras en el océano y nadas hacia el barco", 50, 100)
        draw_text("1. Intentar llegar al barco", 50, 150)
        draw_text("2. Regresar a la playa", 50, 200)
    elif state == "shipwreck":
        screen.blit(img_shipwreck, (0, 0))
        draw_text("Encuentras un naufragio con provisiones", 50, 100)
        draw_text("1. Tomar provisiones y regresar", 50, 150)
        draw_text("2. Buscar más en el naufragio", 50, 200)
    elif state == "bird_nest":
        screen.blit(img_bird_nest, (0, 0))
        draw_text("Encuentras un nido de pájaros con huevos", 50, 100)
        draw_text("1. Tomar los huevos", 50, 150)
        draw_text("2. Dejar los huevos", 50, 200)
    elif state == "coconut":
        screen.blit(img_coconut, (0, 0))
        draw_text("Encuentras un cocotero con cocos frescos", 50, 100)
        draw_text("1. Tomar los cocos", 50, 150)
        draw_text("2. Dejar los cocos", 50, 200)
    elif state == "rescue":
        screen.blit(img_rescue, (0, 0))
        draw_text("Un barco te rescata y vuelves a casa", 50, 100)
    elif state == "no_rescue":
        screen.blit(img_no_rescue, (0, 0))
        draw_text("El barco no te ve y te quedas en la isla", 50, 100)
    pygame.display.flip()

state = "start"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if state == "start":
                if event.key == pygame.K_1:
                    state = "beach"
                elif event.key == pygame.K_2:
                    state = "jungle"
            elif state == "beach":
                if event.key == pygame.K_1:
                    state = "find_food"
                elif event.key == pygame.K_2:
                    state = "build_shelter"
            elif state == "find_food":
                if event.key == pygame.K_1:
                    state = "find_fruits"
                elif event.key == pygame.K_2:
                    state = "fish"
            elif state == "find_fruits":
                if event.key == pygame.K_1:
                    state = "take_apple"
                elif event.key == pygame.K_2:
                    state = "take_mandarina"
                elif event.key == pygame.K_3:
                    state = "take_avocado"
            elif state == "fish":
                if event.key == pygame.K_1:
                    state = "trampa"
                elif event.key == pygame.K_2:
                    state = "rio"
            elif state == "build_shelter":
                if event.key == pygame.K_1:
                    state = "madera"
                elif event.key == pygame.K_2:
                    state = "hojas"
                elif event.key == pygame.K_3:
                    state = "paja"
            elif state == "jungle":
                if event.key == pygame.K_1:
                    state = "path"
                elif event.key == pygame.K_2:
                    state = "animal"
            elif state == "path":
                if event.key == pygame.K_1:
                    state = "cave"
                elif event.key == pygame.K_2:
                    state = "forest_path"
            elif state == "animal":
                if event.key == pygame.K_1:
                    state = "cazar_animal"
                elif event.key == pygame.K_2:
                    state = "observar_animal"
            elif state == "cazar_animal":
                if event.key == pygame.K_1:
                    state = "luchar"
                elif event.key == pygame.K_2:
                    state = "huir"
            elif state == "observar_animal":
                if event.key == pygame.K_1:
                    state = "nuevo_camino"
                elif event.key == pygame.K_2:
                    state = "jungle"
            elif state == "luchar":
                if event.key == pygame.K_1:
                    state = "mountain"
                elif event.key == pygame.K_2:
                    state = "no_rescue"
            elif state == "huir":
                if event.key == pygame.K_1:
                    state = "nuevo_camino"
                elif event.key == pygame.K_2:
                    state = "forest_path"
            elif state == "nuevo_camino":
                if event.key == pygame.K_1:
                    state = "cave"
                elif event.key == pygame.K_2:
                    state = "forest_path"
            elif state == "cave":
                if event.key == pygame.K_1:
                    state = "rescue"
                elif event.key == pygame.K_2:
                    state = "forest_path"
            elif state == "forest_path":
                if event.key == pygame.K_1:
                    state = "mountain"
                elif event.key == pygame.K_2:
                    state = "ocean"
            elif state == "mountain":
                if event.key == pygame.K_1:
                    state = "ocean"
                elif event.key == pygame.K_2:
                    state = "shipwreck"
            elif state == "ocean":
                if event.key == pygame.K_1:
                    state = "shipwreck"
                elif event.key == pygame.K_2:
                    state = "rescue"
            elif state == "shipwreck":
                if event.key == pygame.K_1:
                    state = "bird_nest"
                elif event.key == pygame.K_2:
                    state = "coconut"
            elif state == "bird_nest":
                if event.key == pygame.K_1:
                    state = "rescue"
                elif event.key == pygame.K_2:
                    state = "no_rescue"
            elif state == "coconut":
                if event.key == pygame.K_1:
                    state = "rescue"
                elif event.key == pygame.K_2:
                    state = "no_rescue"
            elif state == "rescue" or state == "no_rescue":
                state = "start"

    show_state(state)
