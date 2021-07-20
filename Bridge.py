
class DrawingApiOne(object):
    
    def draw_circle(self, x, y, radius):
        print(f"API ONE drawing circle with {x}, {y}, {radius}")
       

class DrawingApiTwo(object):

    def draw_circle(self, x, y, radius):
        print(f"API TWO drawing circle: with {x}, {y}, {radius}")
    
    
class Circle(object):
    
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y 
        self._radius = radius
        self._drawing_api = drawing_api
        
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)
    
    def scale(self, percent):
        self._radius *= percent
        
        
circle = Circle(1,2,3,DrawingApiOne())

circle.draw()


circle_two = Circle(2,3,4,DrawingApiTwo())

circle_two.draw()
