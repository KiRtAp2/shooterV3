import pygame
import constants
import player
import colors
import bullet
import powerup
import textures
import utils

# sets up window
import wall

window = pygame.display.set_mode((constants.window_width, constants.window_height))

# sets up players
# the only parameter to Player() is position, which is calculated relative to frame borders
p1 = player.Player((100, constants.frame_height*0.45))
p2 = player.Player((constants.window_width-constants.player_size[0]-100, constants.frame_height*0.45))

# sets up game clock
clock = pygame.time.Clock()

# required for keeping track of sent bullets, spawned powerups and built walls
bullet_list = []
wall_list = []
powerup_list = []

POWERUPSPAWN = pygame.USEREVENT+1
pygame.time.set_timer(POWERUPSPAWN, constants.powerup_spawn_delay)

def draw_score():
    """Function displays player scores on screen"""
    utils.display_text(
        window,
        (p1.x, constants.frame_height+(constants.window_height-constants.frame_height)*0.43),
        str(p1.score),
        colors.text
    )
    utils.display_text(
        window,
        (p2.x, constants.frame_height+(constants.window_height-constants.frame_height)*0.43),
        str(p2.score),
        colors.text
    )


def draw_cooldown():
    """Function draws wall cooldowns for both players"""
    window.blit(
        textures.wall_available if p1.build_ok() else textures.wall_oncooldown,
        (p1.x+70, constants.frame_height+(constants.window_height-constants.frame_height)*0.33)
    )
    window.blit(
        textures.wall_available if p2.build_ok() else textures.wall_oncooldown,
        (p2.x-70-p2.sx, constants.frame_height+(constants.window_height-constants.frame_height)*0.33)
    )


def game_loop():

    # self-explanatory
    exit_game = False

    while not exit_game:

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                # quits if told to quit
                exit_game = True

            if e.type == pygame.KEYDOWN:

                # moving up-down for p2
                if e.key == pygame.K_UP:
                    p2.start_movement(1)
                elif e.key == pygame.K_DOWN:
                    p2.start_movement(-1)

                # moving up-down for p1
                elif e.key == pygame.K_w:
                    p1.start_movement(1)
                elif e.key == pygame.K_s:
                    p1.start_movement(-1)

                elif e.key == pygame.K_RIGHT:
                    # shooting for p2
                    if constants.theme == "white":
                        bullet_list.append(bullet.Bullet(
                            (p2.x-constants.bullet_size[0]-1, (2*p2.y+p2.sy)*0.49),
                            colors.bullet_white_theme,
                            (-constants.bullet_powerup_velocity if p2.powerup_durations[1] > 0 else -constants.bullet_velocity, p2.velocity),  #*#
                            p2.powerup_durations[2] > 0
                        ))
                        if p2.powerup_durations[5] > 0:
                            bullet_list.append(bullet.Bullet(
                                (p2.x - constants.bullet_size[0] - 1, (2 * p2.y + p2.sy) * 0.49+constants.tripleshot_distance),
                                colors.bullet_white_theme,
                                (-constants.bullet_powerup_velocity if p2.powerup_durations[1] > 0 else -constants.bullet_velocity, p2.velocity),  #*#
                                p2.powerup_durations[2] > 0
                            ))
                            bullet_list.append(bullet.Bullet(
                                (p2.x - constants.bullet_size[0] - 1,
                                 (2 * p2.y + p2.sy) * 0.49 - constants.tripleshot_distance),
                                colors.bullet_white_theme,
                                (-constants.bullet_powerup_velocity if p2.powerup_durations[1] > 0 else -constants.bullet_velocity,p2.velocity),  #*#
                                p2.powerup_durations[2] > 0
                            ))
                    elif constants.theme == "black":
                        bullet_list.append(
                            bullet.Bullet(
                                (p2.x-constants.bullet_size[0]-1, (2*p2.y+p2.sy)*0.49),
                                colors.bullet_black_theme,
                                (-constants.bullet_powerup_velocity if p2.powerup_durations[1] > 0 else -constants.bullet_velocity, p2.velocity),  #*#
                                p2.powerup_durations[2] > 0
                            )
                        )
                        if p2.powerup_durations[5] > 0:
                            bullet_list.append(bullet.Bullet(
                                (p2.x - constants.bullet_size[0] - 1, (2 * p2.y + p2.sy) * 0.49+constants.tripleshot_distance),
                                colors.bullet_black_theme,
                                (-constants.bullet_powerup_velocity if p2.powerup_durations[1] > 0 else -constants.bullet_velocity, p2.velocity),  #*#
                                p2.powerup_durations[2] > 0
                            ))
                            bullet_list.append(bullet.Bullet(
                                (p2.x - constants.bullet_size[0] - 1,
                                 (2 * p2.y + p2.sy) * 0.49 - constants.tripleshot_distance),
                                colors.bullet_black_theme,
                                (-constants.bullet_powerup_velocity if p2.powerup_durations[1] > 0 else -constants.bullet_velocity,p2.velocity),  #*#
                                p2.powerup_durations[2] > 0
                            ))

                elif e.key == pygame.K_d:
                    # shooting for p1
                    if constants.theme == "white":
                        bullet_list.append(bullet.Bullet(
                            (p1.x+p1.sx+1, (2*p1.y+p1.sy)*0.49),
                            colors.bullet_white_theme,
                            (constants.bullet_powerup_velocity if p1.powerup_durations[1] > 0 else constants.bullet_velocity, p1.velocity),  #*#
                            p1.powerup_durations[2] > 0
                        ))
                        if p1.powerup_durations[5] > 0:
                            bullet_list.append(bullet.Bullet(
                                (p1.x + p1.sx + 1, (2 * p1.y + p1.sy) * 0.49 + constants.tripleshot_distance),
                                colors.bullet_white_theme,
                                (-constants.bullet_powerup_velocity if p1.powerup_durations[1] > 0 else -constants.bullet_velocity, p1.velocity),  # *#
                                p2.powerup_durations[2] > 0
                            ))
                            bullet_list.append(bullet.Bullet(
                                (p1.x + p1.sx + 1, (2 * p1.y + p1.sy) * 0.49 - constants.tripleshot_distance),
                                colors.bullet_white_theme,
                                (constants.bullet_powerup_velocity if p1.powerup_durations[1] > 0 else -constants.bullet_velocity, p1.velocity),  # *#
                                p2.powerup_durations[2] > 0
                            ))
                    elif constants.theme == "black":
                        bullet_list.append(bullet.Bullet(
                            (p1.x + p1.sx + 1, (2 * p1.y + p1.sy) * 0.49),
                            colors.bullet_black_theme,
                            (constants.bullet_powerup_velocity if p1.powerup_durations[1] > 0 else constants.bullet_velocity, p1.velocity), #*#
                            p1.powerup_durations[2] > 0
                        ))
                        if p1.powerup_durations[5] > 0:
                            bullet_list.append(bullet.Bullet(
                                (p1.x + p1.sx + 1, (2 * p1.y + p1.sy) * 0.49+constants.tripleshot_distance),
                                colors.bullet_black_theme,
                                (constants.bullet_powerup_velocity if p1.powerup_durations[1] > 0 else constants.bullet_velocity, p1.velocity), #*#
                                p2.powerup_durations[2] > 0
                            ))
                            bullet_list.append(bullet.Bullet(
                                (p1.x + p1.sx + 1, (2 * p1.y + p1.sy) * 0.49-constants.tripleshot_distance),
                                colors.bullet_black_theme,
                                (constants.bullet_powerup_velocity if p1.powerup_durations[1] > 0 else constants.bullet_velocity, p1.velocity), #*#
                                p2.powerup_durations[2] > 0
                            ))

                ### HOW TO GET OLD BULLETS:
                ### in the blocks marked with #*#, switch the last value (p1.velocity or p2.velocity, but only the last occurence!) with 0

                elif e.key == pygame.K_LEFT:
                    # wall build for p2
                    if p2.build_ok():
                        wall_list.append(
                            wall.Wall(
                                p2.sy/2+p2.y,
                                p2.x-10-constants.wall_width
                            )
                        )
                        p2.reset_timer()
                elif e.key == pygame.K_a:
                    # wall build for p1
                    if p1.build_ok():
                        wall_list.append(
                            wall.Wall(
                                p1.sy/2+p1.y,
                                p1.x+p1.sx+10
                            )
                        )
                        p1.reset_timer()

            if e.type == pygame.KEYUP:
                # strops moving if player stopped pressing key
                if e.key in (pygame.K_DOWN, pygame.K_UP):
                    p2.stop_moving()
                elif e.key in (pygame.K_s, pygame.K_w):
                    p1.stop_moving()

            if e.type == POWERUPSPAWN:
                # spawns powerup
                powerup.Powerup.spawn(powerup_list)

        if constants.theme == "white":
            # draws background
            window.fill(colors.white)
        elif constants.theme == "black":
            # draws background
            window.fill(colors.black)

        # moves players
        p1.move()
        p2.move()

        # updates players
        p1.tick()
        p2.tick()
        p1.show(window)
        p2.show(window)

        for w in wall_list[:]:
            # updates and displays walls
            w.tick()
            if w.is_old():
                wall_list.remove(w)
            else:
                w.show(window)

        for b in bullet_list[:]:
            # updates and displays bullets
            b.move()
            b.show(window)

            # checks for hits
            if p1.is_hit(b):
                p2.score_up()
                bullet_list.remove(b)
            elif p2.is_hit(b):
                p1.score_up()
                bullet_list.remove(b)
            if not b.pierce_walls:
                for w in wall_list:
                    if w.is_hit(b):
                        bullet_list.remove(b)
            for p in powerup_list[:]:
                if p.is_hit(b):
                    if b.owner_num == 1:
                        p1.boost(p.type)
                    else:
                        p2.boost(p.type)
                    bullet_list.remove(b)
                    powerup_list.remove(p)

        for p in powerup_list[:]:
            p.tick()
            p.show(window)
            if p.is_old():
                powerup_list.remove(p)

        if constants.theme == "white":
            # draws frame
            window.fill(colors.gray, (0, constants.frame_height, constants.window_width, constants.window_height - constants.frame_height))
        elif constants.theme == "black":
            # draws frame
            window.fill(colors.frame_black_theme, (0, constants.frame_height, constants.window_width, constants.window_height - constants.frame_height))

        draw_score()
        draw_cooldown()

        pygame.display.update()
        clock.tick(constants.framerate)


if __name__ == '__main__':
    pygame.init()
    game_loop()
