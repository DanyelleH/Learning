class Points:
    def __init__(self, x_coordinate, y_coordinate) :
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

    def get_x_coord(self):
        return self._x_coordinate

    def get_y_coord (self):
        return self._y_coordinate
    
    def distance_to(self,point_object):
        x_diff =((self._x_coordinate) - (point_object._x_coordinate))**2
        y_diff = ((self._y_coordinate) - (point_object._y_coordinate))**2
        distance = (x_diff + y_diff)**.5
        return distance
    

class LineSegment:
    ##endpoint is an x and a y coordinate
    def __init__(self, point_object_1, point_object_2):
        self._endpoint_1= point_object_1
        self._endpoint_2= point_object_2

    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)
    
    def isParallelTo(self, line_object):
        x_diff_self =self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord()
        y_diff_self = self. _endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()
        x_diff_other = line_object._endpoint_2.get_x_coord() - line_object._endpoint_1.get_x_coord()
        y_diff_other = line_object._endpoint_2.get_y_coord() - line_object._endpoint_1.get_y_coord()
        slope_other = abs(y_diff_other / x_diff_other)
        slope_self = abs(y_diff_self / x_diff_self)
        if slope_other == slope_self:
            return True
        else:
            return False
        
    
point_1 = Points(7,4)
point_2 = Points(-6,18)
point_3 = Points(-6,18)
point_4 = Points(7,4)
print(point_1.distance_to(point_2))

line_1 = LineSegment(point_1,point_2) #line_1 is of the class Line segment, 
print (line_1.length())
line_2 = LineSegment(point_2, point_4)
print(line_1.isParallelTo(line_2))