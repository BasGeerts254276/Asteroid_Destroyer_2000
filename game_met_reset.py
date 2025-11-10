import arcade
 
# Constants
WINDOW_WIDTH = 1480
WINDOW_HEIGHT = 750
WINDOW_TITLE = "Asteroid Destroyer 2000"
PLAYER_MOVEMENT_SPEED = 5
 
class GameView(arcade.Window):
 
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
 
        # Sprite placeholders
        self.player_sprite = None
        self.all_sprites = None
        self.wall_list = None
        self.physics_engine = None
 
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
 
        # Create the player sprite
        self.player_sprite = arcade.Sprite(r"C:\Users\Bas\onedrive\spaceship alien.png", scale=0.1)
        self.player_sprite.center_x = WINDOW_WIDTH / 2
        self.player_sprite.center_y = WINDOW_HEIGHT / 2
 
        # Create a sprite list for all sprites
        self.all_sprites = arcade.SpriteList()
        self.all_sprites.append(self.player_sprite)
 
        # Create wall list (empty for now)
        self.wall_list = arcade.SpriteList()
 
        # Create the physics engine AFTER sprites exist
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
 
    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.all_sprites.draw()
 
    def on_update(self, delta_time):
        """Update the positions of all sprites"""
        if self.physics_engine:
            self.physics_engine.update()
 
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.setup()  # Reset the game when ESC is pressed

        if key in (arcade.key.UP, arcade.key.W):
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key in (arcade.key.LEFT, arcade.key.A):
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
 
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W, arcade.key.DOWN, arcade.key.S):
            self.player_sprite.change_y = 0
        if key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.player_sprite.change_x = 0
 
 
def main():
    window = GameView()
    window.setup()
    arcade.run()
 
 
if __name__ == "__main__":
    main()