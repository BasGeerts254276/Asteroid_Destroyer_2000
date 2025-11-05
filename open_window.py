import arcade

#Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Asteroid Destroyer 2000"


class GameView(arcade.Window):
    
    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.background_color = arcade.csscolor.BLACK

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()  