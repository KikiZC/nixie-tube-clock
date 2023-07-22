import pygame
import sys
from datetime import datetime

# Inicializace knihovny Pygame
pygame.init()

# Nastavení rozměrů okna
width, height = 850, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nixie Tube Hodiny")

# Barvy
background_color = (10, 10, 10)
nixie_tube = pygame.image.load("nixie blank.png")

# Funkce pro získání aktuálního času a rozdělení na jednotlivé číslice
def get_current_time():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    hours, minutes, seconds = time_str.split(":")
    return hours, minutes, seconds

# Načtení obrázků nixie tube číslic 0-9
nixie_digits = []
for i in range(10):
    digit_image = pygame.image.load(f"nixie_{i}.png")
    nixie_digits.append(digit_image)

# Hlavní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vymazání obrazovky
    screen.fill(background_color)

    # Získání aktuálního času a rozdělení na jednotlivé číslice
    hours, minutes, seconds = get_current_time()

    # Vykreslení hodin, minut a sekund pomocí obrázků nixie tube
    nixie_width = nixie_digits[0].get_width()
    nixie_height = nixie_digits[0].get_height()

    x_offset = 50
    y_offset = height // 2 - nixie_height // 2

    for digit in hours:
        digit_num = int(digit)
        screen.blit(nixie_digits[digit_num], (x_offset, y_offset))
        x_offset += nixie_width + 10

    x_offset += 50

    for digit in minutes:
        digit_num = int(digit)
        screen.blit(nixie_digits[digit_num], (x_offset, y_offset))
        x_offset += nixie_width + 10

    x_offset += 50

    for digit in seconds:
        digit_num = int(digit)
        screen.blit(nixie_digits[digit_num], (x_offset, y_offset))
        x_offset += nixie_width + 10

    # Obnovení obrazovky
    pygame.display.flip()

    # Omezení počtu snímků za sekundu na 1
    pygame.time.Clock().tick(1)
