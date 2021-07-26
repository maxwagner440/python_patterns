class Subject(object):
    # one subject that is monitored by several observers
    def __init__(self):
        self._observers = []
        
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
    
class Core(Subject):
    
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._phone = None
        self._email = None
        
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        self._phone = phone
        self.notify()
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
        self.notify()
           
class DoPhone:
    
    def update(self, subject: Subject):
        print(f"Viewer: DoPhone, has phone of: {subject.phone}")
        
class DoEmail:
    
    def update(self, subject: Subject):
        print(f"Viewer: DoEmail has email of: {subject.email}")

c1 = Core("Core 1")

phoneViewer = DoPhone()
emailViewer = DoEmail()

c1.attach(phoneViewer)
c1.attach(emailViewer)

c1.phone = 4403304400
c1.phone = 911

c1.email = "hey@hey.com"
c1.email = "tryagain@hey.com"
