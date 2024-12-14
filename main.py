from robot import Robot
from warehouse import Warehouse

def parse_input(filename):
    with open(filename, 'r') as f:
        # Read warehouse dimensions
        width, height = map(int, f.readline().strip().split())
        warehouse = Warehouse(width, height)
        
        robots = []
        # Keep reading robot positions and commands until EOF
        while True:
            # Try to read robot position
            pos = f.readline().strip()
            if not pos:  # EOF
                break
                
            x, y, direction = pos.split()
            robot = Robot(int(x), int(y), direction)
            
            # Read robot commands
            commands = f.readline().strip()
            
            robots.append((robot, commands))
        
    return warehouse, robots

def main():
    warehouse, robots = parse_input('input.txt')
    
    # Process each robot sequentially
    for robot, commands in robots:
        robot.execute_commands(commands, warehouse)
        print(robot.get_position())

if __name__ == "__main__":
    main()