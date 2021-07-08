class B:
    
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(B):
    """This class inherits from the B class every time its instantiated which allows access to the _shared_state object that is global"""
    def __init__(self, **kwargs):
        B.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

sing1 = Singleton(HTTP = "Hyper Text Transfer Protocol")

print(sing1)

sing2 = Singleton(TEST = "TEST")

# Every Singleton object will have access to the updated _shared_state so sing1 and sing2 will have two key-value pairs here
print(sing1)
print(sing2)
