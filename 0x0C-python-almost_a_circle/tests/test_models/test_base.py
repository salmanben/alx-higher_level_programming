import unittest
Base = __import__('models.base').Base

class TestBaseMethods(unittest.TestCase):

    def test_id_assignment(self):
        # Test id assignment when no id is provided
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        # Test id assignment when id is provided
        base3 = Base(100)
        self.assertEqual(base3.id, 100)

    def test_to_json_string(self):
        # Test to_json_string method with empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test to_json_string method with a list of dictionaries
        dict_list = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_from_json_string(self):
        # Test from_json_string method with empty string
        self.assertEqual(Base.from_json_string(""), [])

        # Test from_json_string method with a JSON string
        json_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}])

    def test_create(self):
        # Test create method with a dictionary
        dictionary = {'id': 1, 'name': 'John'}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'John')

    def test_load_from_file(self):
        # Test load_from_file method with an empty file
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

        # Test load_from_file method with a file containing JSON data
        with open('Base.json', 'w') as file:
            file.write('[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].name, 'Jane')

if __name__ == '__main__':
    unittest.main()
