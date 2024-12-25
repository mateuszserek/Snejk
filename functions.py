import pygame.mixer
import config

def play_music(url: str) -> None: #dziala, za 1 razem jest maly lag, wiec trzeba to zainicjowac na poczatku programu
    pygame.mixer.music.load(url)
    pygame.mixer.music.play()

def middle_screen_location(text: str) -> int:
    return (config.screen_x_size // 2) - (len(text) // 2)

def get_game_screen_size() -> int: #do solidnego potestowania (wstepnie dziala)
    x = config.screen_x_size - config.game_screen_x_start - 1
    y = config.screen_y_size - config.game_screen_y_start - 1
    return (x * y) 
