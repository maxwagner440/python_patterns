import types    

class Strategy:
    
    def __init__(self, function=None):        
        # set new fuction to execute()
        if function:
            self.execute = types.MethodType(function, self)
        
    def execute(self, a):
        print("no sorting: {}".format(a))
        

def strategy_one_ascending(self, a):
    a.sort()
    print("ascending: {}".format(a))

def strategy_two_decending(self, a):
    a.sort(reverse=True)
    print("descending: {}".format(a))

array = [122, 444, 3, 25234, 2]
s0 = Strategy()

s0.execute(array)

s1 = Strategy(function=strategy_one_ascending)
s1.execute(array)


s2 = Strategy(function=strategy_two_decending)
s2.execute(array)
