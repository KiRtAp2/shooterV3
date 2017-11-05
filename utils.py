import constants


def display_text(window, pos, text, color):
    # displays 'color' coloured 'text' on 'window' at 'pos'
    surf = constants.text_font.render(text, True, color)
    window.blit(surf, pos)