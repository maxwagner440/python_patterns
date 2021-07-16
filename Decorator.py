from functools import wraps


def make_blink_tag(function):
    
    @wraps(function)
    
    def decorator():
        
        ret = function()
        
        return f"<blink>{ret}<blink/>"
        
    return decorator
    
def make_blink_tag_with_param(function):
    
    @wraps(function)
    
    def decorator(num:int):
        
        ret = function(num)
        
        return f"<blink>{ret}<blink/>"
        
    return decorator
    
        
@make_blink_tag_with_param
def add_two_param(two:int):
    return str(2 + two)
    
@make_blink_tag
def add_two():
    return str(2)

print(add_two_param(2))
print(add_two()) 
