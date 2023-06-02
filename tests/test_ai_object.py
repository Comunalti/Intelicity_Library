import unittest

from ai_object import AiObject


class AiObjectTests(unittest.TestCase):

    def test_get_object_name_or_default_existing_id(self):
        object_name = AiObject.get_object_name_or_default(5)
        self.assertEqual(object_name, "Recomposição_asfáltica")

    def test_get_object_name_or_default_nonexistent_id(self):
        object_name = AiObject.get_object_name_or_default(99)
        self.assertEqual(object_name, "no ai object name found with id: 99")

    def test_get_object_name_existing_id(self):
        object_name = AiObject.get_object_name(10)
        self.assertEqual(object_name, "Sarjeta")

    def test_get_object_name_nonexistent_id(self):
        with self.assertRaises(Exception):
            AiObject.get_object_name(99)

    def test_create_from_local_id(self):
        ai_object = AiObject.create_from_local_id(1, 10)
        self.assertEqual(ai_object.get_global_id(), 11)

    def test_create_from_global_id(self):
        ai_object = AiObject.create_from_global_id(20)
        self.assertEqual(ai_object.get_global_id(), 20)

    def test_get_local_id(self):
        ai_object = AiObject(15)
        local_id = ai_object.get_local_id(10)
        self.assertEqual(local_id, 5)

    def test_get_global_id(self):
        ai_object = AiObject(25)
        global_id = ai_object.get_global_id()
        self.assertEqual(global_id, 25)

if __name__ == '__main__':
    unittest.main()
