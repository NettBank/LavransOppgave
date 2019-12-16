# Importerer Pygame med kommandoen "pip install pygame".
import pygame
# Initialiserer pakken "Pygame".
pygame.init()

# Setter størrelsen på vinduet hvor 500 er høyden og 500 er bredden.
VINDU_HØYDE = 500
VINDU_BREDDEN = 500
# Funksjon som får det til å fungere.
def screen(VINDU_HØYDE, VINDU_BREDDEN, vindu):
  pygame.init()
vindu = pygame.display.set_mode((VINDU_BREDDEN, VINDU_HØYDE))
# Setter tittelen på vinduet.
pygame.display.set_caption("Lavrans sin høy måloppnåelse oppgave.")

# Dette er karakteren sin posisjon og størrelse.
x = 50
y = 50
bredde = 40
høyde = 60
# Velocity er hvor raskt karakteren beveger seg.
velocity = 7
# Main løkken.
run = True
while run:
    # Setter en tidsdelay i spillet. 100 = 100 millisekunder. 100 millisekunder = 0.1 sekund.
    pygame.time.delay(100)

    # Dette er en event som scanner alt som skjer fra brukeren, f.eks tastatur-trykk og musebevegelser.
    for event in pygame.event.get():
        # Hvis man trykket på "exit" button på toppen av høyre hjørnet.
        if event.type == pygame.QUIT:
            run = False

    # Lager en liste sånn at hvis jeg holder inne en knapp så beveger den seg.
    knapper = pygame.key.get_pressed()
    # Hvis man trykker på venstre pilknapp så går man til venstre.
    if knapper[pygame.K_LEFT]:
        x -= velocity
    # Hvis man trykker på høyre pilknapp så går man til høyre.
    if knapper[pygame.K_RIGHT]:
        x += velocity
    # Hvis man trykker på den øvre pilknapp så går man oppover.
    if knapper[pygame.K_UP]:
        y -= velocity
    # Hvis man trykker på den nedre pilknapp så går man nedover.
    if knapper[pygame.K_DOWN]:
        y += velocity
    # Tegner karakteren i vinduet.
    pygame.draw.rect(vindu, (74, 139, 190), (x, y, bredde, høyde))
    # Oppdaterer overflaten sånn at man kan se karakteren.
    pygame.display.update()

    # Gjør sånn at man ikke
    vindu.fill((0,0,0))

pygame.quit()
