import unittest
from content import *



class TestNetworkOutputContent(unittest.TestCase):


    def setUpClass(cls) -> None:
        print("setupclass")
    def setUp(self) -> None:
        print("setup")

    def test_create_from_line(self):
        string = "1 0.730469 0.719792 0.539062 0.48125 0.649228"

        content = NetworkOutputContent.create_from_line(string)

        self.assertIsInstance(content, NetworkOutputContent)
        self.assertEqual(content.ai_object.get_global_id(), 1)
        self.assertEqual(content.screen_space_center_x, 0.730469)
        self.assertEqual(content.screen_space_center_y, 0.719792)
        self.assertEqual(content.screen_space_size_x, 0.539062)
        self.assertEqual(content.screen_space_size_y, 0.48125)
        self.assertEqual(content.trust, 0.649228)

    # def test_convert_to_database(self):
    #     database_container = DatabaseContainer([], 1.0, 2.0)
    #     content = NetworkOutputContent(AiObject(1), 0.5, 0.5, 0.2, 0.2, 0.8)
    #
    #     database_content = content.convert_to_database(database_container)
    #
    #     self.assertIsInstance(database_content, DatabaseContent)
    #     self.assertEqual(database_content.ai_object.get_global_id(), 1)
    #     self.assertEqual(database_content.pixel_space_center_x, 1)
    #     self.assertEqual(database_content.pixel_space_center_y, 2)
    #     self.assertEqual(database_content.pixel_space_size_x, 3)
    #     self.assertEqual(database_content.pixel_space_size_y, 4)
    #     self.assertEqual(database_content.trust, 0.8)
    #     self.assertEqual(database_content.container, database_container)

    # Add additional test methods for other functionalities
#
#
if __name__ == '__main__':
    unittest.main()
