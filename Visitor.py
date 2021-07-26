
class MyHouse(object):
    def accept(self, visitor):
        visitor.visit(self)
    
    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)
    
    def work_on_electrical(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        return self.__class__.__name__
        
      
class Visitor(object):
    def __str__(self):
        return self.__class__.__name__
        
        
class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)
        
        
class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electrical(self)

hv = HvacSpecialist()
e = Electrician()

house = MyHouse()

house.accept(hv)
house.accept(e)

house.work_on_hvac
house.work_on_electrical
