from random import randint, choice
import config 
from functions import *
#do zrobienia bedzie konfiguracja venv jak bede oddawal projekt


class Apple:
    def __init__(self):
        self.all_positions = []
        self.position = []
        self.counter = 0

    def generate_pos(self, snake_positions) -> list: #skopiować liste z pozycjami i dodać do niej head snakea
        possible_positions = list(filter(lambda e: e not in snake_positions, self.all_positions))
        return choice(possible_positions)

    def create_all_position_list_and_first_position(self, player):
        for i in range(config.game_screen_x_start + 1, config.screen_x_size):
            for y in range(config.game_screen_y_start + 1, config.screen_y_size):
                self.all_positions.append([i, y])

        self.position = self.generate_pos(player.position_before_head)

    def eaten_apple(self, player):
        play_music(config.eat_sound)
        self.counter += 1 
        self.position = self.generate_pos(player.position_before_head)
        if self.counter % config.how_much_apple_to_speed_up == 0 and config.game_tick_ms > 15:
            config.game_tick_ms -= config.speed_up_tick_number
            play_music(config.speed_up_sound)
