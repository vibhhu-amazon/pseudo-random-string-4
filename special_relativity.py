import math

class SpecialRelativityCalculator:
    """A minimal special relativity calculator."""
    
    def __init__(self):
        self.c = 299792458  # Speed of light in m/s
    
    def lorentz_factor(self, velocity):
        """Calculate the Lorentz factor (gamma).
        
        Args:
            velocity: Velocity in m/s
            
        Returns:
            The Lorentz factor
        """
        if velocity >= self.c:
            raise ValueError("Velocity must be less than speed of light")
        return 1 / math.sqrt(1 - (velocity**2 / self.c**2))
    
    def time_dilation(self, proper_time, velocity):
        """Calculate time dilation effect."""
        gamma = self.lorentz_factor(velocity)
        return proper_time * gamma
    
    def length_contraction(self, proper_length, velocity):
        """Calculate length contraction effect."""
        gamma = self.lorentz_factor(velocity)
        return proper_length / gamma
    
    def relativistic_mass(self, rest_mass, velocity):
        """Calculate relativistic mass."""
        gamma = self.lorentz_factor(velocity)
        return rest_mass * gamma
