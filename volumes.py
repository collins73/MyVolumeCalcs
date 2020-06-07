import math
import os
os.system('cls')


class Cylinder:
  """Calculates the volume of a Cylinder shape

  Args: The data will represent values for a given radius and height.
     The value of pi(3.14) is a constant.
  """
  def __init__(self, radius, height, unit_of_measurement="cubic meters"):
    self.radius = radius
    self.height = height
    self.unit_of_measurement = unit_of_measurement
    
  def vol_cylinder(self):
    """The formula for estimating the volume of a cylinder is:
     Vcyl = math.pi*(self.radius**2)*(self.height)
    """
    if self.height > 0:#checks for,and reminds the user to select positive values for the height
      print("Volumetric Calculations are fun!")
    else:
      print("Opps, please select a positive non-zero value")
    result = math.pi*(self.radius**2)*(self.height)
    return ("The volume of the cylinder is: " + str(round(result, 2)) + " " +  self.unit_of_measurement)


class Sphere(Cylinder):
  """ Calculates the volume of a Sphere shape. The Sphere class
    shall have its own method for estimating the volume of a Sphere.
    Sphere will inherit from Cylinder as shown.

  Args: The data will represent values for a given radius
     and unit of measurement(i.e. inches, feet, meters, ect).
     The value of pi(3.14) is a constant.
  """
  def __init__(self, radius, height, unit_of_measurement="cubic meters"):
    super().__init__(radius, height, unit_of_measurement=unit_of_measurement)
    self.radius = radius
    
  def vol_sphere(self):
    """The formula for estimating the volume of a Sphere is:
     Vsphr = 4/3 *math.pi*(self.radius**3)
    """
    vol_estimate = math.pi*(self.radius**3)*4/3
    return ("The volume of the Sphere is: " + str(round(vol_estimate, 2)) + " " +  self.unit_of_measurement)
  

class Cone(Cylinder):
  """ Calculates the volume of a Cone shape. The Cone class
    shall inherit the properties and attributes from the Cylinder class.

  Args: The data will represent values for a given radius, height,
     and unit of measurement(i.e. inches, feet, meters, ect).
     The value of pi(3.14) is a constant.
  """
  def __init__(self, radius,  height, color):
    Cylinder.__init__(self,radius, height, unit_of_measurement="cubic meters" )
    self.color = color
    
  def vol_cone(self):
    """The formula for estimating the volume of a Sphere is:
     Vcone = 1/3 *math.pi*(self.radius**2)*(self.height)
    """
    vol_cal = math.pi*(self.radius**2)*(self.height)*1/3
    return ("The volume of the Cone is: " + str(round(vol_cal, 2)) + " " + self.unit_of_measurement )
  

#Create instances/objects from each Class
cylinder = Cylinder(-9, -8, "cubic meters")
# print(cylinder.vol_cylinder())

sphere = Sphere(-6, "cubic meters")
# print(sphere.vol_sphere())
cone = Cone(6, -20, "cubic meters")
print(cone.vol_cylinder())# Method inheritance from the Cylinder class
# print(cone.vol_cone())
