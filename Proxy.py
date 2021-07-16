
import time

class Producer:
    
    def produce(self):
        print("Producer is working hard!")
        
    def meet(self):
        print("Producer has time to meet with you!")
 
class Proxy:
    
    def __init__(self, occupied:str):
        self.occupied = occupied
        self.producer = None
        
    def produce(self):
        
        print("Artist checking if Producer avail")
        
        if self.occupied == "No":
            self.producer = Producer()
            time.sleep(2)
            
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")
            
         
# instantiated as busy (dont create producer)
proxy = Proxy("Yes")
# Producer is busy, can't meet
proxy.produce()
# Producer is not occupied anymore
proxy.occupied = "No"
# Producer can meet now
proxy.produce()
