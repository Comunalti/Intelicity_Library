import shutil
import unittest
from unittest.mock import patch
from pathlib import Path

from PIL import Image
from PIL import UnidentifiedImageError

from image import *

class TestImage(unittest.TestCase):
    def setUp(self):

        shutil.copy("Files/networkOutput/146314118747-20230103-16h09m59s.jpg",
                    "temp/network_output/146314118747-20230103-16h09m59s.jpg")


        self.jpg_path = Path("temp/network_output/146314118747-20230103-16h09m59s.jpg")

    def tearDown(self):
        if self.jpg_path.exists():
            self.jpg_path.unlink()

    def test_is_corrupted_when_valid_image(self):
        # Create a valid test image
        self.image = Image(self.jpg_path)

        self.assertFalse(self.image.is_corrupted())


        with open(self.jpg_path, "wb") as f:
            f.write(b"\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x02\x03\x04\x05")

        self.assertTrue(self.image.is_corrupted())

    def test_is_corrupted_when_zero_width(self):
        self.image = Image(self.jpg_path)

        self.image.width = 0

        self.assertTrue(self.image.is_corrupted())

    def test_is_corrupted_when_zero_height(self):

        self.image = Image(self.jpg_path)

        self.image.height = 0

        self.assertTrue(self.image.is_corrupted())

    def test_is_corrupted_when_file_size_less_than_100_bytes(self):
        # Create an empty file
        if self.jpg_path.exists():
            self.jpg_path.unlink()
        self.jpg_path.touch()
        self.image = Image(self.jpg_path)

        self.assertTrue(self.image.is_corrupted())


if __name__ == "__main__":
    unittest.main()
