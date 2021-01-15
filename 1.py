import os
import pygame
import pygame_menu

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((600, 400))


def set_difficulty(selected, value):
    """
    Set the difficulty of the game.
    """
    print('Set difficulty to {} ({})'.format(selected, value))


def start_the_game():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    print('Do the job here !')


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)

menu.add_text_input('Name: ', default='John Doe', maxchar=10)
menu.add_selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)