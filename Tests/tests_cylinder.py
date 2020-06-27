import math
import os
from Tests import volumes

os.system('cls')


def test_vol_cylinder(self):
    result = math.pi * (self.radius ** 2) * self.height
    assert result == volumes.vol_cylinder(3.14, 4, 8)

