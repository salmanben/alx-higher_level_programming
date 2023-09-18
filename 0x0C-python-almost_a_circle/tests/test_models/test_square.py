import unittest
Square = __import__('models.sqaure').Square


class TestSquareMethods(unittest.TestCase):

    def setUp(self):
        # Create a Square instance for testing
        self.square = Square(5, 2, 3, 42)

    def test_size_property(self):
        self.assertEqual(self.square.size, 5)
        self.square.size = 7
        self.assertEqual(self.square.size, 7)
        with self.assertRaises(TypeError):
            self.square.size = "invalid"
        with self.assertRaises(ValueError):
            self.square.size = 0

    def test_x_property(self):
        self.assertEqual(self.square.x, 2)
        self.square.x = 4
        self.assertEqual(self.square.x, 4)
        with self.assertRaises(TypeError):
            self.square.x = "invalid"
        with self.assertRaises(ValueError):
            self.square.x = -2

    def test_y_property(self):
        self.assertEqual(self.square.y, 3)
        self.square.y = 5
        self.assertEqual(self.square.y, 5)
        with self.assertRaises(TypeError):
            self.square.y = "invalid"
        with self.assertRaises(ValueError):
            self.square.y = -1

    def test_str_method(self):
        expected_str = "[Square] (42) 2/3 - 5"
        self.assertEqual(str(self.square), expected_str)

    def test_update_method(self):
        self.square.update(10, 3, 6, 0)
        self.assertEqual(str(self.square), "[Square] (10) 3/6 - 3")
        self.square.update(size=7)
        self.assertEqual(str(self.square), "[Square] (10) 3/6 - 7")

    def test_to_dictionary_method(self):
        expected_dict = {'id': 42, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

