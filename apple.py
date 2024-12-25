from random import randint, choice
import config 
# import simpleaudio as sa

# def play_music():
#     wave_obj = sa.WaveObject.from_wave_file("audio/div5.wav")
#     play_obj = wave_obj.play() 
#     play_obj.wait_done() 

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
            #play_music() - po skonczeniu dzwieku rozwala caly program