class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
        # Define direction changes for left and right turns
        self.directions = ['N', 'E', 'S', 'W']
        
    def turn_left(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index - 1) % 4]
        
    def turn_right(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index + 1) % 4]
        
    def move(self, warehouse):
        new_x, new_y = self.x, self.y
        
        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'W':
            new_x -= 1
            
        # Check if new position is within warehouse bounds
        if warehouse.is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y
            
    def execute_commands(self, commands, warehouse):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move(warehouse)
                
    def get_position(self):
        return f"{self.x} {self.y} {self.direction}"