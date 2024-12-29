from random import randint, choice
import config 
from functions import *
#do zrobienia bedzie konfiguracja venv jak bede oddawal projekt


class Apple:
    def __init__(self):
        self.position = [5, 13] #do zmiany
        self.counter = 0
        self.all_positions = []

    def generate_pos(self, snake_positions) -> list:
        possible_positions = list(filter(lambda e: e not in snake_positions, self.all_positions))
        return choice(possible_positions)

    def create_all_position_list(self):
        for i in range(config.game_screen_x_start + 1, config.screen_x_size):
            for y in range(config.game_screen_y_start + 1, config.screen_y_size):
                self.all_positions.append([i, y])

    def eaten_apple(self, player):
        play_music(config.eat_sound)
        self.counter += 1 
        self.position = self.generate_pos(player.position_before_head)
        if self.counter % 5 == 0 and config.game_tick_ms > 15:
            config.game_tick_ms -= 5
            play_music(config.speed_up_sound)
