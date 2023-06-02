import shutil
import unittest
from pathlib import Path
from unittest.mock import mock_open, patch
from containers import NetworkOutputContainer, DatabaseContainer
from contents import NetworkOutputContent, DatabaseContent
from image import Image
from file_header import FileHeader


class TestFileHeader(unittest.TestCase):

    def setUp(self):
        shutil.copy("Files/networkOutput/146314118747-20230103-16h09m59s.txt",
                    "temp/network_output/146314118747-20230103-16h09m59s.txt")
        shutil.copy("Files/networkOutput/146314118747-20230103-16h09m59s.jpg",
                    "temp/network_output/146314118747-20230103-16h09m59s.jpg")
        shutil.copy("Files/database/146314118747-20230103-16h09m59s.txt",
                    "temp/database/146314118747-20230103-16h09m59s.txt")

        self.jpg_path = Path("temp/network_output/146314118747-20230103-16h09m59s.jpg")
        self.network_output_path = Path("temp/network_output/146314118747-20230103-16h09m59s.txt")
        self.database_path = Path("temp/database/146314118747-20230103-16h09m59s.txt")

        self.file_header_network = FileHeader(self.network_output_path)
        self.file_header_database = FileHeader(self.database_path)

    def tearDown(self):
        # Remove the test file if it exists

        # if self.network_output_path.exists():
        #     self.network_output_path.unlink()
        #
        # if self.jpg_path.exists():
        #     self.jpg_path.unlink()
        #
        # if self.database_path.exists():
        #     self.database_path.unlink()
        pass

    def test_init(self):
        self.assertEqual(self.file_header_network.path, self.network_output_path)
        self.assertEqual(self.file_header_network.file_name, "146314118747-20230103-16h09m59s.txt")
        self.assertEqual(self.file_header_network.driver_id, "146314118747")
        self.assertEqual(self.file_header_network.date, "20230103")
        self.assertEqual(self.file_header_network.time, "16h09m59s")

    def test_get_neighbor_image(self):
        image_path = self.network_output_path.with_suffix(".jpg")
        image = self.file_header_network.get_neighbor_image()
        self.assertIsInstance(image, Image)
        self.assertEqual(image.jpg_path, image_path)
        self.assertEqual(image.width, 1280)
        self.assertEqual(image.height, 960)

    def test_open_as_network_output_container(self):
        network_output_container = self.file_header_network.open_as_network_output_container()
        self.assertIsInstance(network_output_container, NetworkOutputContainer)

        self.assertEqual(network_output_container.contents[0],
                         NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"))

        self.assertEqual(network_output_container.contents,
                         [NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
                          NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
                          NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228")])

    def test_open_as_database_container(self):
        database_container = self.file_header_database.open_as_database_container()
        self.assertIsInstance(database_container, DatabaseContainer)

        self.assertEqual(database_container.contents[0],
                         DatabaseContent.create_from_line(
                             "23 450 472 259 36 0.491906 Sinalizacao_Horizontal -23.6383339 -46.7367179"))

        self.assertEqual(database_container.contents, [
            DatabaseContent.create_from_line("23 450 472 259 36 0.491906 Sinalizacao_Horizontal -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("23 992 592 576 364 0.535857 Sinalizacao_Horizontal -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("1 933 675 671 466 0.704676 Valeta -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("30 896 610 637 336 0.917303 Sarjetao_inadequado -23.6383339 -46.7367179")])

    def test_save_container(self):
        database_container = self.file_header_database.open_as_database_container()
        self.file_header_database.save_container(database_container)
        database_container = self.file_header_database.open_as_database_container()

        self.assertEqual(database_container.contents[0],
                         DatabaseContent.create_from_line(
                             "23 450 472 259 36 0.491906 Sinalizacao_Horizontal -23.6383339 -46.7367179"))

        self.assertEqual(database_container.contents, [
            DatabaseContent.create_from_line("23 450 472 259 36 0.491906 Sinalizacao_Horizontal -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("23 992 592 576 364 0.535857 Sinalizacao_Horizontal -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("1 933 675 671 466 0.704676 Valeta -23.6383339 -46.7367179"),
            DatabaseContent.create_from_line("30 896 610 637 336 0.917303 Sarjetao_inadequado -23.6383339 -46.7367179")])

    def test_save_network(self):
        network_container = self.file_header_network.open_as_network_output_container()
        self.file_header_network.save_container(network_container)
        network_container = self.file_header_network.open_as_network_output_container()

        self.assertEqual(network_container.contents[0],
                         NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"))

        self.assertEqual(network_container.contents,
                         [NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
                          NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228"),
                          NetworkOutputContent.create_from_line("1 0.730469 0.719792 0.539062 0.48125 0.649228")])

if __name__ == "__main__":
    unittest.main()
