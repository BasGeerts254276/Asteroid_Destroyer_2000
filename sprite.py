import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Asteroid Destroyer 2000"

class GameView(arcade.Window):

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Sprite placeholder
        self.spaceship = None
        self.all_sprites = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Load the transparent PNG as a sprite
        self.spaceship = arcade.Sprite(r"C:\Users\Bas\onedrive\spaceship alien.png", scale= 0.2)

        # Position the spaceship in the middle of the window
        self.spaceship.center_x = WINDOW_WIDTH / 2
        self.spaceship.center_y = WINDOW_HEIGHT / 2

        # Create a sprite list and add the spaceship
        self.all_sprites = arcade.SpriteList()
        self.all_sprites.append(self.spaceship)

    def on_draw(self):
        """Render the screen."""
        self.clear()  # Clear the screen

        # Draw all sprites
        if self.all_sprites:
            self.all_sprites.draw()


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
