import unittest
from ai_object import AiObject
from containers import Container, DatabaseContainer, NetworkOutputContainer
from content import NetworkOutputContent, FileContent, DatabaseContent


class TestNetworkOutputContainer(unittest.TestCase):

    def test_create_from_line_list(self):
        lines = [
            "line 1",
            "line 2",
            "line 3"
        ]
        container = NetworkOutputContainer.create_from_line_list(lines)

        self.assertIsInstance(container, NetworkOutputContainer)
        self.assertEqual(len(container.contents), len(lines))
        self.assertIsInstance(container.contents[0], NetworkOutputContent)
        self.assertEqual(container.contents[0].line, "line 1")

    def test_concatenate(self):
        container1 = NetworkOutputContainer([NetworkOutputContent("line 1")])
        container2 = NetworkOutputContainer([NetworkOutputContent("line 2"), NetworkOutputContent("line 3")])

        container1.concatenate(container2)

        self.assertEqual(len(container1.contents), 3)
        self.assertEqual(container1.contents[0].line, "line 1")
        self.assertEqual(container1.contents[1].line, "line 2")
        self.assertEqual(container1.contents[2].line, "line 3")

    def test_convert_to_database_container(self):
        latitude = 1.0
        longitude = 2.0
        container = NetworkOutputContainer([NetworkOutputContent("line 1"), NetworkOutputContent("line 2")])

        database_container = container.convert_to_database_container(latitude, longitude)

        self.assertIsInstance(database_container, DatabaseContainer)
        self.assertEqual(len(database_container.contents), len(container.contents))
        self.assertIsInstance(database_container.contents[0], DatabaseContent)
        self.assertIsInstance(database_container.contents[1], DatabaseContent)
        self.assertEqual(database_container.latitude, latitude)
        self.assertEqual(database_container.longitude, longitude)

    def test_add(self):
        container = NetworkOutputContainer([])
        content = NetworkOutputContent("line 1")

        container.add(content)

        self.assertEqual(len(container.contents), 1)
        self.assertEqual(container.contents[0].line, "line 1")

class TestDatabaseContainer(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")
        ...
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")
        ...

    def test_create_from_line_list(self):
        lines = [
            "line 1",
            "line 2",
            "line 3"
        ]
        container = DatabaseContainer.create_from_line_list(lines)

        self.assertIsInstance(container, DatabaseContainer)
        self.assertEqual(len(container.contents), len(lines))
        self.assertEqual(container.latitude, float(lines[0].split(" ")[7]))
        self.assertEqual(container.longitude, float(lines[0].split(" ")[8]))

    def test_create_from_values(self):
        lines = [
            "line 1",
            "line 2",
            "line 3"
        ]
        latitude = 1.234
        longitude = 5.678

        container = DatabaseContainer.create_from_values(lines, latitude, longitude)

        self.assertIsInstance(container, DatabaseContainer)
        self.assertEqual(len(container.contents), len(lines))
        self.assertEqual(container.latitude, latitude)
        self.assertEqual(container.longitude, longitude)

    def test_concatenate(self):
        container1 = DatabaseContainer([], 1.0, 2.0)
        container2 = DatabaseContainer([DatabaseContent("line 1"), DatabaseContent("line 2")], 3.0, 4.0)

        container1.concatenate(container2)

        self.assertEqual(len(container1.contents), 2)
        self.assertEqual(container1.contents[0].line, "line 1")
        self.assertEqual(container1.contents[1].line, "line 2")

    def test_convert_to_network_output_container(self):
        container = DatabaseContainer([DatabaseContent("line 1"), DatabaseContent("line 2")], 1.0, 2.0)

        network_output_container = container.convert_to_network_output_container()

        self.assertIsInstance(network_output_container, NetworkOutputContainer)
        self.assertEqual(len(network_output_container.contents), len(container.contents))
        self.assertIsInstance(network_output_container.contents[0], NetworkOutputContent)
        self.assertIsInstance(network_output_container.contents[1], NetworkOutputContent)

    def test_add(self):
        container = DatabaseContainer([], 1.0, 2.0)
        content = DatabaseContent("line 1")

        container.add(content)

        self.assertEqual(len(container.contents), 1)
        self.assertEqual(container.contents[0].line, "line 1")


