import unittest
import math
from special_relativity import SpecialRelativityCalculator

class TestSpecialRelativityCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SpecialRelativityCalculator()
    
    def test_lorentz_factor_at_rest(self):
        """Test Lorentz factor when velocity is zero."""
        gamma = self.calc.lorentz_factor(0)
        self.assertAlmostEqual(gamma, 1.0, places=5)
    
    def test_time_dilation(self):
        """Test time dilation calculation."""
        velocity = 0.5 * self.calc.c  # Half speed of light
        dilated_time = self.calc.time_dilation(1.0, velocity)
        expected = 1.0 / math.sqrt(1 - 0.25)  # gamma = 1/sqrt(0.75)
        self.assertAlmostEqual(dilated_time, expected, places=5)
    
    def test_velocity_at_light_speed_raises_error(self):
        """Test that velocity at light speed raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.lorentz_factor(self.calc.c)
