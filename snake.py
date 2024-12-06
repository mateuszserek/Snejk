import config

class Snake:
    head = [1, 1]
    position_before_head = [[1, 1], [2, 1], [3, 1]]
    current_direction = [1, 0]

    def check_self_collision(self) -> bool:
        if self.head in self.position_before_head:
            return True
        else:
            return False
        
    def check_screen_collision(self) -> bool:
        if self.head[0] == config.screen_x_size or self.head[1] == config.screen_y_size:
            return True 
        else:
            return False
    
    def move(self) -> None:
        new_head = [self.head[0] + self.current_direction[0], self.head[1] + self.current_direction[1]]
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
        
    