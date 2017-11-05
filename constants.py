import pygame

window_width = 1024
window_height = 676
frame_height = 500

player_size = (49, 49)
player_velocity = 3

theme = "black"
# "black" and "white" supported!

framerate = 60

bullet_size = (10,5)
bullet_velocity = 8

if not pygame.font.get_init(): pygame.font.init()
text_font = pygame.font.SysFont("consolas", 30)

wall_height = 100
wall_width = 20
wall_build_cooldown = 9  # seconds
wall_last = 5  # seconds

powerup_spawn_delay = 40*1000  # miliseconds
powerup_size = (49, 49)
powerup_timer = 10  # seconds
powerup_durations = [5*framerate, 12*framerate, 10*framerate, 7*framerate, 11*framerate, 6*framerate]  # in ticks

bullet_powerup_velocity = bullet_velocity+2
boosted_speed_add = 2
tripleshot_distance = 20  # pixels
