# Write a class named Taxicab that has three **private** data members: one that 
# holds the current x-coordinate, one that holds the current y-coordinate, and one 
# that holds the current odometer reading. An odometer simply measures the distance 
# a car or bicycle has traveled by keeping track of how many times its wheels have
# turned. So if you travel one unit left, and then one unit right, you'll be back 
# where you started, but your odometer will tell you that you've traveled 2 units. 
# **All three** data members should be updated as needed so that they are always 
# current. 

# The class should have an `init` method that takes two parameters and uses them 
# to initialize the coordinates, and also initializes the odometer to zero.  

# The class should have get methods for each data member: `get_x_coord`, 
# `get_y_coord`, and `get_odometer`. The class does not need any set methods.  

# It should have a method called `move_x` that takes a parameter that tells how 
# far the Taxicab should shift left or right. It should have a method called 
# `move_y` that takes a parameter that tells how far the Taxicab should shift 
# up or down.
class TaxiCab():

    def __init__(self, x_coord , y_coord):
        self._x_coordinate = x_coord
        self._y_coordinate = y_coord
        self._odometer = 0
        
    def get_x_coord(self):
       return self._x_coordinate
        
    def get_y_coord(self):
        return self._y_coordinate
        
    def get_odometer(self):
        return self._odometer
    
    def move_x(self, new_x):
        self._x_coordinate += new_x
        self._odometer += abs(new_x)
        
    def move_y (self, new_y):
        self._y_coordinate += new_y
        self._odometer += abs(new_y)

new_cab = TaxiCab(20,50)
print(new_cab.get_x_coord(), new_cab.get_y_coord())
new_cab.move_x(3)
new_cab.move_y(-4)
new_cab.move_x(-1)
print(new_cab.get_x_coord(), new_cab.get_y_coord())
print(new_cab.get_odometer())