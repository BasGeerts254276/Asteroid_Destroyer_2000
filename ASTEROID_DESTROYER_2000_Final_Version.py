import arcade
import random
import math

# Constants
WINDOW_WIDTH = 1480
WINDOW_HEIGHT = 750
WINDOW_TITLE = "Asteroid Destroyer 2000"
PLAYER_MOVEMENT_SPEED = 5
ASTEROID_SPEED = 3
LASER_SPEED = 10


class StartView(arcade.View):
    """Starting page view"""

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


class GameView(arcade.View):
    """Main game view"""

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)

        self.player_sprite = None
        self.asteroid_list = None
        self.all_sprites = None
        self.wall_list = None
        self.physics_engine = None
        self.laser_list = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Create the player sprite
        self.player_sprite = arcade.Sprite(r"C:\Users\Bas\onedrive\spaceship alien.png", scale=0.1)
        self.player_sprite.center_x = WINDOW_WIDTH / 2
        self.player_sprite.center_y = WINDOW_HEIGHT / 2

        # Create sprite lists
        self.all_sprites = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()

        # Add player to all sprites
        self.all_sprites.append(self.player_sprite)

        # --- Create an asteroid ---
        asteroid_sprite = arcade.Sprite(r"C:\Users\Bas\onedrive\afbeeldingen\asteroid.png", scale=0.15)

        # Start it just off the right side of the screen
        asteroid_sprite.center_x = WINDOW_WIDTH + 50
        asteroid_sprite.center_y = random.randint(50, WINDOW_HEIGHT - 50)

        # Give it a speed to move left across the screen
        asteroid_sprite.change_x = -ASTEROID_SPEED

        self.asteroid_list.append(asteroid_sprite)
        self.all_sprites.append(asteroid_sprite)

        # Create the physics engine AFTER sprites exist
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.all_sprites.draw()
        self.laser_list.draw()  # <--- Add this line


    def on_update(self, delta_time):
        """Update the positions of all sprites"""
        if self.physics_engine:
            self.physics_engine.update()

        # Update asteroid positions
        self.asteroid_list.update()

        self.laser_list.update()

        # Check if any asteroid moved off the left side, reset it
        for asteroid in self.asteroid_list:
            if asteroid.right < 0:
                asteroid.center_x = WINDOW_WIDTH + 50
                asteroid.center_y = random.randint(50, WINDOW_HEIGHT - 50)
                asteroid.change_x = -ASTEROID_SPEED
        
        for laser in self.laser_list:
            if laser.bottom > WINDOW_HEIGHT or laser.top < 0 or laser.right < 0 or laser.left > WINDOW_WIDTH:
                laser.remove_from_sprite_lists()


    def on_key_press(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W):
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key in (arcade.key.LEFT, arcade.key.A):
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.ESCAPE:
            # Return to start menu
            start_view = StartView()
            self.window.show_view(start_view)
        # inside on_key_press under the last elif
        elif key == arcade.key.LSHIFT:
            # shoot laser
            laser = arcade.Sprite(r"C:\Users\Bas\onedrive\afbeeldingen\laser_sprite.png", scale=0.2)

            laser.center_x = self.player_sprite.center_x
            laser.center_y = self.player_sprite.center_y
            laser.angle = self.player_sprite.angle
            # speed of laser based on angle of ship
            laser.change_x = math.cos(math.radians(-self.player_sprite.angle)) * LASER_SPEED
            laser.change_y = math.sin(math.radians(-self.player_sprite.angle)) * LASER_SPEED
            self.laser_list.append(laser)
            self.all_sprites.append(laser)

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W, arcade.key.DOWN, arcade.key.S):
            self.player_sprite.change_y = 0
        if key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.player_sprite.change_x = 0


def main():
    """Main entry point"""
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()