
import arcade
import random
import math

# --- Vensterinstellingen ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Asteroid Destroyer 2000"

# --- Constantes ---
PLAYER_SPEED = 5
LASER_SPEED = 10
ASTEROID_COUNT = 6


class AsteroidDestroyer(arcade.Window):
    """Hoofdklasse van het spel"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.BLACK

        # Sprite lists
        self.player_list = None
        self.asteroid_list = None
        self.laser_list = None

        # Speler
        self.player_sprite = None

        # Beweging
        self.change_x = 0
        self.change_y = 0

        # Score
        self.score = 0

    def setup(self):
        """Game initialiseren"""
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.score = 0

        # --- Speler ---
        self.player_sprite = arcade.Sprite(arcade.resources.image_space_shooter_playerShip1_orange, 0.5)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # --- Asteroïden ---
        for i in range(ASTEROID_COUNT):
            asteroid = arcade.Sprite(arcade.resources.image_space_shooter_meteors_brown_big1, 0.5)
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.uniform(-2, 2)
            asteroid.change_y = random.uniform(-2, 2)
            self.asteroid_list.append(asteroid)

    def on_draw(self):
        """Teken het scherm"""
        self.clear()
        self.player_list.draw()
        self.asteroid_list.draw()
        self.laser_list.draw()

        # Score tekenen
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """Draai het schip richting de muispositie"""
        x_diff = x - self.player_sprite.center_x
        y_diff = y - self.player_sprite.center_y
        angle_rad = math.atan2(y_diff, x_diff)
        self.player_sprite.angle = -math.degrees(angle_rad)

    def on_key_press(self, key, modifiers):
        """Beweging toetsen"""
        if key in (arcade.key.W, arcade.key.UP):
            self.change_y = PLAYER_SPEED
        elif key in (arcade.key.S, arcade.key.DOWN):
            self.change_y = -PLAYER_SPEED
        elif key in (arcade.key.A, arcade.key.LEFT):
            self.change_x = -PLAYER_SPEED
        elif key in (arcade.key.D, arcade.key.RIGHT):
            self.change_x = PLAYER_SPEED
        elif key == arcade.key.SPACE:
            # Laser schieten
            laser = arcade.Sprite(arcade.resources.image_space_shooter_laser_blue, 0.8)
            laser.center_x = self.player_sprite.center_x
            laser.center_y = self.player_sprite.center_y
            laser.angle = self.player_sprite.angle
            # Richting bepalen op basis van hoek
            laser.change_x = math.cos(math.radians(-self.player_sprite.angle)) * LASER_SPEED
            laser.change_y = math.sin(math.radians(-self.player_sprite.angle)) * LASER_SPEED
            self.laser_list.append(laser)

    def on_key_release(self, key, modifiers):
        """Stop beweging bij loslaten toets"""
        if key in (arcade.key.W, arcade.key.UP) or key in (arcade.key.S, arcade.key.DOWN):
            self.change_y = 0
        elif key in (arcade.key.A, arcade.key.LEFT) or key in (arcade.key.D, arcade.key.RIGHT):
            self.change_x = 0

    def on_update(self, delta_time):
        """Beweging en botsingen"""
        # --- Speler bewegen ---
        self.player_sprite.center_x += self.change_x
        self.player_sprite.center_y += self.change_y

        # Houd speler binnen het scherm
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        if self.player_sprite.right > SCREEN_WIDTH:
            self.player_sprite.right = SCREEN_WIDTH
        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        if self.player_sprite.top > SCREEN_HEIGHT:
            self.player_sprite.top = SCREEN_HEIGHT

        # --- Sprites updaten ---
        self.asteroid_list.update()
        self.laser_list.update()

        # --- Botsingen lasers / asteroïden ---
        for laser in self.laser_list:
            hit_list = arcade.check_for_collision_with_list(laser, self.asteroid_list)
            for asteroid in hit_list:
                asteroid.remove_from_sprite_lists()
                laser.remove_from_sprite_lists()
                self.score += 10

        # --- Asteroïden bewegen / schermgrenzen ---
        for asteroid in self.asteroid_list:
            if asteroid.left < 0 or asteroid.right > SCREEN_WIDTH:
                asteroid.change_x *= -1
            if asteroid.bottom < 0 or asteroid.top > SCREEN_HEIGHT:
                asteroid.change_y *= -1


def main():
    game = AsteroidDestroyer()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()