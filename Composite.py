
class Component(object):

    def __init__(self, *args, **kwargs):
        pass
    def component_function(self):
        pass


class Child(Component):

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        
        self.name = args[0]
        
    def component_function(self):
        print("  "+self.name)
        


class Composite(Component):

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        
        self.name = args[0]
        
        self.children = []
        
    def append_child(self, child):
        self.children.append(child)
       
    def remove_child(self, child):
        self.children.remove(child)
        
    def component_function(self):
        print(self.name)
        
        for i in self.children:
            i.component_function()
        
top = Composite('top_menu')

sub1 = Composite('sub_menu 1')
sub11= Child('sub_menu 11')
sub12= Child('sub_menu 12')

sub1.append_child(sub11)
sub1.append_child(sub12)

sub2 = Composite('sub_menu 2')
sub21= Child('sub_menu 21')
sub2.append_child(sub21)

top.append_child(sub1)
top.append_child(sub2)

top.component_function()
