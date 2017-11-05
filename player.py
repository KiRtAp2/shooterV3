import base_class
import constants
import textures


class Player(base_class.Base):

    image = textures.player_image
    wall_timer_duration = constants.framerate * constants.wall_build_cooldown

    def __init__(self, pos):
        self.x, self.y = pos
        self.sx, self.sy = constants.player_size
        self.velocity = 0
        self.speed = constants.player_velocity
        self.score = 0
        self.wall_timer = 0

        self.powerup_durations = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }

    def show(self, window):
        """Blits self.image to the screen"""
        window.blit(self.image, (self.x, self.y))

    def start_movement(self, direction: int):
        """Starts movement based on direction"""
        if direction > 0:
            self.velocity = -self.speed
        else:
            self.velocity = self.speed

    def stop_moving(self):
        """Stops moving"""
        self.velocity = 0

    def move(self):
        """Updates position, should be called once per tick"""
        self.y += self.velocity
        if self.powerup_durations[4] > 0:
            if self.velocity > 0:
                self.y += constants.boosted_speed_add
            elif self.velocity < 0:
                self.y -= constants.boosted_speed_add
        self.correct_bounds()

    def score_up(self):
        self.score += 2 if self.powerup_durations[3] > 0 else 1

    def build_ok(self):
        return self.wall_timer <= 0

    def tick(self):
        """Should be called once per tick"""
        self.wall_timer -= 1
        for k in self.powerup_durations.keys():
            self.powerup_durations[k] -= 1
            if self.powerup_durations[k] < 0:
                self.powerup_durations[k] = 0

    def reset_timer(self):
        """Call at wall build time"""
        self.wall_timer = self.wall_timer_duration

    def boost(self, type):
        self.powerup_durations[type] = constants.powerup_durations[type]
