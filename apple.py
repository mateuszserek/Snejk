from random import randint, choice
import config 
import pygame
#do zrobienia bedzie konfiguracja venv jak bede oddawal projekt
def play_music(): #dziala, za 1 razem jest maly lag, wiec trzeba to zainicjowac na poczatku programu
    pygame.mixer.init()
    pygame.mixer.music.load("audio/div5.wav")
    pygame.mixer.music.play()

def generate_pos():
    return [randint(config.game_screen_x_start + 1, config.screen_x_size - 1), randint(config.game_screen_y_start + 1, config.screen_y_size - 1)]

class Apple:
    counter = 0
    def __init__(self):
        self.position = generate_pos()
    
    def eaten_apple(self):
        self.counter += 1 
        self.position = generate_pos()
        if self.counter % 5 == 0 and config.game_tick_ms > 15:
            config.game_tick_ms -= 5
            play_music()