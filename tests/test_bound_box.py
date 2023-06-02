import unittest

from bound_box import BoundBox


class BoundBoxTestCase(unittest.TestCase):
    def test_to_pixel_space(self):
        # Test conversion to pixel space
        box = BoundBox(0.5, 0.5, 0.2, 0.4)
        pixel_box = box.to_pixel_space(800, 600)
        self.assertAlmostEqual(pixel_box.center_x, 400)
        self.assertAlmostEqual(pixel_box.center_y, 300)
        self.assertAlmostEqual(pixel_box.width, 160)
        self.assertAlmostEqual(pixel_box.height, 240)

    def test_to_screen_space(self):
        # Test conversion to screen space
        pixel_box = BoundBox(400, 300, 160, 240)
        screen_box = pixel_box.to_screen_space(800, 600)
        self.assertAlmostEqual(screen_box.center_x, 0.5)
        self.assertAlmostEqual(screen_box.center_y, 0.5)
        self.assertAlmostEqual(screen_box.width, 0.2)
        self.assertAlmostEqual(screen_box.height, 0.4)

    def test_to_pixel_space_edge_cases(self):
        # Test edge case of zero size
        with self.assertRaises(ValueError):

            box = BoundBox(0.5, 0.5, 0, 0)

        # Test edge case of non-zero size but zero screen dimensions
        box = BoundBox(0.5, 0.5, 0.2, 0.4)
        with self.assertRaises(ValueError):
            pixel_box = box.to_pixel_space(0, 0)

    def test_to_screen_space_edge_cases(self):
        # Test edge case of zero size
        with self.assertRaises(ValueError):
            screen_box = BoundBox(0.5, 0.5, 0, 0)

        # Test edge case of non-zero size but zero screen dimensions
        screen_box = BoundBox(0.5, 0.5, 0.2, 0.4)
        with self.assertRaises(ValueError):
            pixel_box = screen_box.to_screen_space(0, 0)


if __name__ == '__main__':
    unittest.main()
