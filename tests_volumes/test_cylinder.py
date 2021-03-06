import os
import pytest
import volumes
import math

os.system('cls')


@pytest.mark.function1
def tests_cylinder():
    cylinder = volumes.Cylinder(5, 10, "cubic meters")
    assert cylinder._unit_of_measurement == "cubic meters"


@pytest.mark.function2
def tests_vol_cylinder():
    cylinder = volumes.Cylinder(5, 10, "cubic meters")
    assert cylinder.height == 10
    assert cylinder.radius == 5
    result = math.pi * (5 ** 2) * 10 == 785
    assert result != str


 