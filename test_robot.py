import unittest
from robot import Robot
from warehouse import Warehouse

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.warehouse = Warehouse(5, 5)
        
    def test_movement_and_turns(self):
        # Test case 1
        robot1 = Robot(1, 0, 'N')
        robot1.execute_commands('MMRMMLMMR', self.warehouse)
        self.assertEqual(robot1.get_position(), '3 4 E')
        
        # Test case 2
        robot2 = Robot(3, 2, 'E')
        robot2.execute_commands('MLLMMRMM', self.warehouse)
        self.assertEqual(robot2.get_position(), '2 4 N')
        
    def test_boundary_checks(self):
        robot = Robot(0, 0, 'S')
        robot.execute_commands('M', self.warehouse)  # Try to move south from (0,0)
        self.assertEqual(robot.get_position(), '0 0 S')  # Should stay at same position
        
    def test_turns(self):
        robot = Robot(0, 0, 'N')
        robot.turn_right()
        self.assertEqual(robot.direction, 'E')
        robot.turn_right()
        self.assertEqual(robot.direction, 'S')
        robot.turn_left()
        self.assertEqual(robot.direction, 'E')

if __name__ == '__main__':
    unittest.main()