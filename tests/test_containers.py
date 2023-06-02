import unittest
from pathlib import Path
from contents import *
from containers import *


class ContainerTests(unittest.TestCase):

    def test_save_network_output(self):
        # Create a Container instance with some contents
        network_output_content = [
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228")
            ]
        container = Container(network_output_content)

        # Specify a path for saving
        path = Path("temp/test.txt")

        # Call the save method
        container.save(path)

        # Assert that the file exists
        self.assertTrue(path.exists())

        # Assert the content of the file
        with open(path, 'r') as file:
            saved_contents = file.readlines()
            expected_contents = [str(content) + "\n" for content in network_output_content]
            self.assertEqual(saved_contents, expected_contents)

        # Clean up the created file
        path.unlink()

    def test_save(self):
        # Create a Container instance with some contents
        database_content = [
            DatabaseContent.create_from_line("23 450 472 259 36 0.491906 Sinalizacao_Horizontal -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("23 992 592 576 364 0.535857 Sinalizacao_Horizontal -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("1 933 675 671 466 0.704676 Valeta -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("30 896 610 637 336 0.917303 Sarjetao_inadequado -23.6383339 -46.7367179")
            ]
        container = Container(database_content)

        # Specify a path for saving
        path = Path("temp/test.txt")

        # Call the save method
        container.save(path)

        # Assert that the file exists
        self.assertTrue(path.exists())

        # Assert the content of the file
        with open(path, 'r') as file:
            saved_contents = file.readlines()
            expected_contents = [str(content) + "\n" for content in database_content]
            self.assertEqual(saved_contents, expected_contents)

        # Clean up the created file
        path.unlink()

class NetworkOutputContainerTests(unittest.TestCase):

    def setUp(self):
        # Create a NetworkOutputContainer instance with some contents
        self.contents = [
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228")
            ]
        self.container = NetworkOutputContainer(self.contents)

    def test_create_from_line_list(self):
        # Create a list of lines
        lines = [
            "1 0.730469 0.719792 0.539062 0.48125 0.649228",
            "1 0.730469 0.719792 0.539062 0.48125 0.649228",
            "1 0.730469 0.719792 0.539062 0.48125 0.649228",
            "1 0.730469 0.719792 0.539062 0.48125 0.649228",
        ]

        # Call the create_from_line_list class method
        new_container = NetworkOutputContainer.create_from_line_list(lines)

        # Assert that the contents of the new container are correctly created from the lines
        expected_contents = [NetworkOutputContent.create_from_line(line) for line in lines]
        self.assertEqual(new_container.contents, expected_contents)

    def test_concatenate(self):
        # Create another NetworkOutputContainer instance with additional contents
        additional_contents = [
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
        ]
        other_container = NetworkOutputContainer(additional_contents)

        # Call the concatenate method
        self.container.concatenate(other_container)

        # Assert that the contents of the container are correctly concatenated
        expected_contents = NetworkOutputContainer([
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
        ])

        self.assertEqual(self.container, expected_contents)

    def test_convert_to_database_container(self):
        # Specify screen width, screen height, and geolocation
        latitude = -23.6383339
        longitude = -46.7367179

        screen_width = 1920
        screen_height = 1080

        geo_location = GeoLocation(latitude, longitude)

        # Call the convert_to_database_container method
        database_container = self.container.convert_to_database_container(screen_width, screen_height, geo_location)

        # Assert that the contents of the new database container are correctly converted

        expected_contents = [
            DatabaseContent.create_from_line("1 1402 777 1034 519 0.649228 Sarjetão -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("1 1402 777 1034 519 0.649228 Sarjetão -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("1 1402 777 1034 519 0.649228 Sarjetão -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("1 1402 777 1034 519 0.649228 Sarjetão -23.6383339 -46.7367179"),
        ]

        self.assertEqual(database_container, DatabaseContainer(expected_contents))

    def test_add(self):
        # Create a new NetworkOutputContent instance
        new_content = NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228")

        # Call the add method
        self.container.add(new_content)

        # Assert that the new content is added to the container

        self.assertEqual(self.container, NetworkOutputContainer([
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
            NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
        ]))

# class DatabaseContainerTests(unittest.TestCase):
#
#     def setUp(self):
#         # Create a DatabaseContainer instance with some contents
#         self.contents = [
#             DatabaseContent("data1"),
#             DatabaseContent("data2"),
#             DatabaseContent("data3")
#         ]
#         self.container = DatabaseContainer(self.contents)
#
#     def test_create_from_line_list(self):
#         # Create a list of lines
#         lines = ["line1", "line2", "line3"]
#
#         # Call the create_from_line_list class method
#         new_container = DatabaseContainer.create_from_line_list(lines)
#
#         # Assert that the contents of the new container are correctly created from the lines
#         expected_contents = [DatabaseContent.create_from_line(line) for line in lines]
#         self.assertEqual(new_container.contents, expected_contents)
#
#     def test_concatenate(self):
#         # Create another DatabaseContainer instance with additional contents
#         additional_contents = [
#             DatabaseContent("data4"),
#             DatabaseContent("data5")
#         ]
#         other_container = DatabaseContainer(additional_contents)
#
#         # Call the concatenate method
#         self.container.concatenate(other_container)
#
#         # Assert that the contents of the container are correctly concatenated
#         expected_contents = self.contents + additional_contents
#         self.assertEqual(self.container.contents, expected_contents)
#
#     def test_convert_to_network_output_container(self):
#         # Specify screen width and screen height
#         screen_width = 1920
#         screen_height = 1080
#
#         # Call the convert_to_network_output_container method
#         network_output_container = self.container.convert_to_network_output_container(screen_width, screen_height)
#
#         # Assert that the contents of the new network output container are correctly converted
#         expected_contents = [content.convert_to_network_output(screen_width, screen_height) for content in self.contents]
#         self.assertEqual(network_output_container.contents, expected_contents)
#
#     def test_add(self):
#         # Create a new DatabaseContent instance
#         new_content = DatabaseContent("data4")
#
#         # Call the add method
#         self.container.add(new_content)
#
#         # Assert that the new content is added to the container
#         expected_contents = self.contents + [new_content]
#         self.assertEqual(self.container.contents, expected_contents)

if __name__ == "__main__":
    unittest.main()
