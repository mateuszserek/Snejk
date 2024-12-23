import config
from apple import Apple

class Snake:
    head = [config.game_screen_x_start + 1, config.game_screen_y_start + 1]
    position_before_head = [[config.game_screen_x_start, config.game_screen_y_start]]
    current_direction = [1, 0]

    def check_self_collision(self) -> bool: 
        if self.head in self.position_before_head:
            return True
        else:
            return False
        
    def check_screen_collision(self) -> bool:
        if self.head[0] == config.screen_x_size or self.head[1] == config.screen_y_size or self.head[0] == config.game_screen_x_start or self.head[1] == config.game_screen_y_start:
            return True 
        else:
            return False
    
    def move(self, apple_eaten: bool) -> None:
        new_head = [self.head[0] + self.current_direction[0], self.head[1] + self.current_direction[1]]

        if not apple_eaten:
            self.position_before_head.pop(0)

        self.position_before_head.append(self.head)
        self.head = new_head

    def next_direction(self, dir) -> None:
        if (dir == -1):
            return 
        
        match chr(dir):
            case 'd':
                self.current_direction = [1, 0]
            case 's':
                self.current_direction = [0, 1]
            case 'a':
                self.current_direction = [-1, 0]
            case 'w':
                self.current_direction = [0, -1]
        
    def check_if_apple_is_eaten(self, apple: Apple) -> bool:
        if self.head == apple.position:
            return True 
        else:
            return False
