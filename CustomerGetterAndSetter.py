
class C:
  
    _x: int = None
    
    def __init__(self):
        pass
    
    def getx(self):
        return self._x

    def setx(self, value):
        """This setter checks value before setting"""
        if value < 6:
            raise ValueError("Uh oh!")
        else:
            self._x = value

    def delx(self):
        del self._x
    
    # https://docs.python.org/3/library/functions.html#property
    # property is like using "property" decorators
    x = property(getx, setx, delx, "I'm the 'x' property.")

c = C()

try:
   # should throw ValueError
   c.x = 3
except ValueError as e:
    print(e)
