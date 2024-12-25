from random import randint, choice
import config 
from functions import *
#do zrobienia bedzie konfiguracja venv jak bede oddawal projekt

def generate_pos() -> list:
    return [randint(config.game_screen_x_start + 1, config.screen_x_size - 1), randint(config.game_screen_y_start + 1, config.screen_y_size - 1)]

class Apple:
    def __init__(self):
        self.position = generate_pos()
        self.counter = 0
    
    def eaten_apple(self):
        play_music(config.eat_sound)
        self.counter += 1 
        self.position = generate_pos()
        if self.counter % 5 == 0 and config.game_tick_ms > 15:
            config.game_tick_ms -= 5
            play_music(config.speed_up_sound)
