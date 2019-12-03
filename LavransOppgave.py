# Importerer libraryen "Arcade" installert med pip install arcade kommandoen i ledetekts.
import arcade

# Setter størrelsen på vinduet.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Åpner vinduet hvor "SCREEN_WIDTH" er bredden, "SCREEN_HEIGHT" er høyden og "Labbes Spill" er tittelen.
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Labbes Spill")

# Setter bakgrunns fargen, "http://arcade.academy/arcade.color.html" er linken til listen over fargen.
arcade.set_background_color(arcade.color.WHEAT)

# Starter rendering prosessen.
arcade.start_render()

# Denne funksjoner tegner et tre på en spesifikkt sted.
def draw_maple_tree(x, y):
    # Vi trenger 3 x, y punkter for en trekant, som skal være toppen av treet.
    arcade.draw_triangle_filled(x + 40, y,
                x, y - 100,
                x + 80, y - 100,
                arcade.color.DARK_GREEN)
    # Tegner tømmeret
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)
