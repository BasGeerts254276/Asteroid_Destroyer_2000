import arcade
import math 

# Constants
WINDOW_WIDTH = 1480
WINDOW_HEIGHT = 750
WINDOW_TITLE = "Asteroid Destroyer 2000"
PLAYER_MOVEMENT_SPEED = 5

class StartView(arcade.View):
    """starting page view"""

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BYZANTIUM)

    def on_draw(self):
        self.clear()
        arcade.draw_text("ASTEROID DESTROYER 2000",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,
                         arcade.color.WHITE, 36, anchor_x="center")
        arcade.draw_text("Press SPACE to Start",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 20,
                         arcade.color.LIGHT_GRAY, 20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)