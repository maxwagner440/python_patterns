import types    

class Strategy:
    
    def __init__(self, function=None):
        self.name = "default strategy"
        
        # set new fuction to execute()
        if function:
            self.execute = types.MethodType(function, self)
        
    def execute(self):
        print("{} is used!".format(self.name))
        

def strategy_one(self):
    print("{} is used to execute method 1!".format(self.name))

def strategy_two(self):
    print("{} is used to execute method 2!".format(self.name))


s0 = Strategy()

s0.execute()

s1 = Strategy(function=strategy_one)

s1.name = "second strategy"

s1.execute()


s2 = Strategy(function=strategy_two)

s2.name = "third strategy"

s2.execute()
