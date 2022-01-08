import unittest
from city_country import get_city_country

class CityTestCase(unittest.TestCase):
    """Test function city_country.py"""

    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')
        # pass
    
    def test_city_country_population(self):
        city_country_population = get_city_country('santiago', 'chile', '5000000')
        self.assertEqual(city_country_population,'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()