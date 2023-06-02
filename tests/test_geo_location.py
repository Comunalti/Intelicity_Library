import unittest
from geo_location import GeoLocation


class GeoLocationTestCase(unittest.TestCase):

    def test_create_from_string(self):
        location = GeoLocation.create_from_string("37.7749", "-122.4194")
        self.assertIsInstance(location, GeoLocation)
        self.assertAlmostEqual(location.latitude, 37.7749)
        self.assertAlmostEqual(location.longitude, -122.4194)

    def test_is_valid_coordinate(self):
        valid_location = GeoLocation(37.7749, -122.4194)
        self.assertTrue(valid_location.is_valid_coordinate())

        # invalid_location = GeoLocation(100, 200)
        # self.assertFalse(invalid_location.is_valid_coordinate())

    def test_get_distance_to(self):
        location1 = GeoLocation(37.7749, -122.4194)
        location2 = GeoLocation(34.0522, -118.2437)
        distance = location1.get_distance_to(location2)
        self.assertAlmostEqual(distance, 6797.8, delta=0.1)  # Check if the distance is within a tolerance

    def test_str(self):
        location = GeoLocation(37.7749, -122.4194)
        self.assertEqual(str(location), "37.7749 -122.4194")


if __name__ == '__main__':
    unittest.main()




