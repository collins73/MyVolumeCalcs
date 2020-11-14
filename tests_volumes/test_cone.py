import os
import pytest

import volumes 

os.system('cls')


@pytest.mark.test3
def tests_cone():
  cone = volumes.Cone(6, 2, "Red")
  assert cone.color == "Red"
  
  

@pytest.mark.test4
def tests_vol_cone():
  cone = volumes.Cone(7, 9, "Blue")
  assert cone.radius == 7
  assert cone.height == 9
  assert cone.unit_of_measurement == "cubic meters"
  assert cone.color == "Blue"

