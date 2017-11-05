from pygame.image import load as image

player_image = image("textures/player.png")

wall_available = image("textures/wall/wall_black.png")
wall_oncooldown = image("textures/wall/wall_black_crossed.png")

powerup_null = image("textures/powerup/null.png")

powerup_images = {
    0: image("textures/powerup/null.png"),
    1: image("textures/powerup/bulletspeed.png"),
    2: image("textures/powerup/piercewalls.png"),
    3: image("textures/powerup/doublepoints.png"),
    4: image("textures/powerup/speed.png"),
    5: image("textures/powerup/tripleshot.png")
}
