import unittest
from ai_object import AiObject
from bound_box import BoundBox
from geo_location import GeoLocation
from contents import DatabaseContent, NetworkOutputContent


class TestDatabaseContent(unittest.TestCase):

    def test_create_from_line(self):
        line = "1 933 675 671 466 0.704676 Valeta -23.6383339 -46.7367179"
        expected_ai_object = AiObject.create_from_global_id(1)
        expected_pixel_bound_box = BoundBox(933, 675, 671, 466)
        expected_trust = 0.704676
        expected_geo_location = GeoLocation.create_from_string("-23.6383339", "-46.7367179")

        result = DatabaseContent.create_from_line(line)

        self.assertEqual(result.ai_object, expected_ai_object)
        self.assertEqual(result.pixel_bound_box, expected_pixel_bound_box)
        self.assertEqual(result.trust, expected_trust)
        self.assertEqual(result.geo_location, expected_geo_location)

    def test_get_ai_object_name(self):
        ai_object = AiObject(3)
        file_content = DatabaseContent(ai_object, BoundBox(0, 0, 100, 100), 0.5, GeoLocation(0, 0))

        result = file_content.get_ai_object_name()

        self.assertEqual(result, "Tampa_de_PV_adequada")

    def test_get_pixel_space_xyxy(self):
        pixel_bound_box = BoundBox(100, 200, 50, 50)
        file_content = DatabaseContent(AiObject(1), pixel_bound_box, 0.5, GeoLocation(0, 0))

        result = file_content.get_pixel_space_xyxy()

        xyxy = (75, 175, 125, 225)

        self.assertEqual(result, xyxy)

    def test_convert_to_network_output(self):
        pixel_bound_box = BoundBox(100, 200, 300, 400)
        file_content = DatabaseContent(AiObject(1), pixel_bound_box, 0.5, GeoLocation(0, 0))
        screen_width = 800
        screen_height = 600

        result = file_content.convert_to_network_output(screen_width, screen_height)

        expected_bound_box = BoundBox(0.125, 0.3333333333333333, 0.375, 0.6666666666666666)


        self.assertEqual(result.ai_object, file_content.ai_object)
        self.assertEqual(result.screen_bound_box, expected_bound_box)
        self.assertEqual(result.trust, file_content.trust)


class TestNetworkOutputContent(unittest.TestCase):

    def test_create_from_line(self):
        line = "1 0.730469 0.719792 0.539062 0.48125 0.649228"
        expected_ai_object = AiObject.create_from_global_id(1)
        expected_screen_bound_box = BoundBox(0.730469, 0.719792, 0.539062, 0.48125)
        expected_trust = 0.649228

        result = NetworkOutputContent.create_from_line(line)

        self.assertEqual(result.ai_object, expected_ai_object)
        self.assertEqual(result.screen_bound_box, expected_screen_bound_box)
        self.assertEqual(result.trust, expected_trust)

    def test_convert_to_database(self):
        screen_bound_box = BoundBox(0.125, 0.3333333333333333, 0.375, 0.6666666666666666)
        network_output = NetworkOutputContent(AiObject(1), screen_bound_box, 0.649228)
        screen_width = 800
        screen_height = 600
        geo_location = GeoLocation(0, 0)

        result = network_output.convert_to_database(screen_width, screen_height, geo_location)

        expected_bound_box = BoundBox(100, 200, 300, 400)

        self.assertEqual(result.ai_object, network_output.ai_object)
        self.assertEqual(result.pixel_bound_box, expected_bound_box)
        self.assertEqual(result.trust, network_output.trust)
        self.assertEqual(result.geo_location, geo_location)


if __name__ == "__main__":
    unittest.main()
