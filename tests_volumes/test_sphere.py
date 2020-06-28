import os
import pytest
import volumes

os.system('cls')

@pytest.mark.test1
def tests_sphere():
  sphere = volumes.Sphere(8, 20)
  assert sphere.radius == 8
  assert sphere.height == 20

@pytest.mark.test2
def tests_vol_sphere():
  sphere = volumes.Sphere(5, 3)
  assert sphere.radius == 5


