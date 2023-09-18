import unittest
Rectangle = __import__('models.rectangle').Rectangle

class TestRectangleMethods(unittest.TestCase):

    def setUp(self):
        # Create a Rectangle instance for testing
        self.rect = Rectangle(4, 5, 1, 2, 42)

    def test_width_property(self):
        self.assertEqual(self.rect.width, 4)
        self.rect.width = 7
        self.assertEqual(self.rect.width, 7)
        with self.assertRaises(TypeError):
            self.rect.width = "invalid"
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def test_height_property(self):
        self.assertEqual(self.rect.height, 5)
        self.rect.height = 8
        self.assertEqual(self.rect.height, 8)
        with self.assertRaises(TypeError):
            self.rect.height = "invalid"
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def test_x_property(self):
        self.assertEqual(self.rect.x, 1)
        self.rect.x = 3
        self.assertEqual(self.rect.x, 3)
        with self.assertRaises(TypeError):
            self.rect.x = "invalid"
        with self.assertRaises(ValueError):
            self.rect.x = -2

    def test_y_property(self):
        self.assertEqual(self.rect.y, 2)
        self.rect.y = 4
        self.assertEqual(self.rect.y, 4)
        with self.assertRaises(TypeError):
            self.rect.y = "invalid"
        with self.assertRaises(ValueError):
            self.rect.y = -1

    def test_area_method(self):
        self.assertEqual(self.rect.area(), 20)

    def test_display_method(self):
        # You can't easily test print output, but you can capture it and check.
        import io
        from unittest.mock import patch

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.rect.display()
            displayed_rect = mock_stdout.getvalue()

        expected_display = "\n\n   ####\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(displayed_rect, expected_display)

    def test_str_method(self):
        expected_str = "[Rectangle] (42) 1/2 - 4/5"
        self.assertEqual(str(self.rect), expected_str)

    def test_update_method(self):
        self.rect.update(10, 3, 6, 0, 0)
        self.assertEqual(str(self.rect), "[Rectangle] (10) 0/0 - 3/6")
        self.rect.update(height=7, width=2)
        self.assertEqual(str(self.rect), "[Rectangle] (10) 0/0 - 2/7")

    def test_to_dictionary_method(self):
        expected_dict = {'x': 1, 'y': 2, 'id': 42, 'height': 5, 'width': 4}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

