
    
class Handler:
    # abstract
    def __init__(self, successor):
        self._successor = successor
        
    def handle(self, request):
        handled = self._handle(request)
        
        if not handled:
            self._successor.handle(request)
        
    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")
    
    
class StringHandler(Handler):

    def _handle(self, request):
        if type(request) == str:
            print(f"Request {request} handled in StringHandler")
            return True

    
class IntegerHandler(Handler):

    def _handle(self, request):
        if type(request) == int:
            print(f"Request {request} handled in IntegerHandler")
            return True         
            
            
class DefaultHandler(Handler):

    def _handle(self, request):
        print(f"End of the chain, no type handler for: {request}")
        return True
        
class Client:

    def __init__(self):
        self.handler = StringHandler(IntegerHandler(DefaultHandler(None)))
    
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)
            
            

client = Client()

requests = ["hey, I be a string", 5, [],40]

client.delegate(requests)
