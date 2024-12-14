# Task1
# Robot Navigation System

## Overview
This project implements a **Robot Navigation System** that simulates the movement of robots within a warehouse grid. Robots can move, turn, and execute a series of commands while respecting the boundaries of the warehouse.

The program is written in Python and contains the following components:

1. **Input File (`input.txt`)**: Contains the warehouse size, robot initial positions, orientations, and movement commands.
2. **Robot Class (`robot.py`)**: Manages robot state, movement, and commands.
3. **Warehouse Class (`warehouse.py`)**: Validates positions within the warehouse.
4. **Unit Tests (`test_robot.py`)**: Ensures the correctness of the robot navigation logic.

---

## Files and Their Purpose

### 1. `input.txt`
This file provides input to the system, including:
- **Warehouse dimensions**: The width and height of the warehouse.
- **Robot initial states**: Starting positions and orientations of robots.
- **Commands**: A sequence of instructions (`L`, `R`, `M`) for robot movement.

**Example:**
```txt
5 5
1 0 N
MMRMMLMMR
3 2 E
MLLMMRMM
```
- **`5 5`**: Warehouse dimensions (5x5 grid).
- **`1 0 N`**: Robot starts at position (1, 0) facing North.
- **`MMRMMLMMR`**: Command sequence for the robot.

---

### 2. `robot.py`
Defines the `Robot` class, which handles:
- Robot initialization with starting position and direction.
- Commands to turn left (`L`), turn right (`R`), and move (`M`).
- Validation of movements based on warehouse boundaries.

**Key Methods:**
```python
class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        """Turns the robot 90 degrees counterclockwise."""
        ...

    def turn_right(self):
        """Turns the robot 90 degrees clockwise."""
        ...

    def move(self, warehouse):
        """Moves the robot one step forward in its current direction if the move is valid."""
        ...

    def execute_commands(self, commands, warehouse):
        """Executes a sequence of commands."""
        ...

    def get_position(self):
        """Returns the robot’s current position and orientation as a string."""
        ...
```

---

### 3. `warehouse.py`
Defines the `Warehouse` class, which:
- Initializes the warehouse dimensions.
- Checks if a position is valid within the grid boundaries.

**Key Method:**
```python
class Warehouse:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_valid_position(self, x, y):
        """Returns True if the position (x, y) is within the warehouse boundaries."""
        return 0 <= x <= self.width and 0 <= y <= self.height
```

---

### 4. `test_robot.py`
Contains unit tests for the robot navigation system using the `unittest` framework.

**Test Cases:**
```python
class TestRobot(unittest.TestCase):
    def test_movement_and_turns(self):
        robot1 = Robot(1, 0, 'N')
        robot1.execute_commands('MMRMMLMMR', self.warehouse)
        self.assertEqual(robot1.get_position(), '3 4 E')

    def test_boundary_checks(self):
        robot = Robot(0, 0, 'S')
        robot.execute_commands('M', self.warehouse)
        self.assertEqual(robot.get_position(), '0 0 S')
```

---

## How to Run

### 1. Prerequisites
- Python 3.6 or higher.

### 2. Run the Program
To simulate robot movements, execute the following commands in your terminal:
```bash
python robot.py
```

### 3. Run the Tests
To ensure everything works as expected, run the unit tests:
```bash
python -m unittest test_robot.py
```

---

## Example Output
Given the input in `input.txt`, the robots navigate the warehouse and their final positions are printed:

**Input:**
```txt
5 5
1 0 N
MMRMMLMMR
3 2 E
MLLMMRMM
```

**Output:**
```txt
Robot 1: 3 4 E
Robot 2: 2 4 N
```

---

## Future Improvements
- Add obstacle handling within the warehouse.
- Support multiple robots navigating simultaneously.
- Implement a graphical interface to visualize robot movements.