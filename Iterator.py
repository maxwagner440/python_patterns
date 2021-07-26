def count_to(count):
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]
    
    # zip does not order tuple
    iterator: tuple(int, str) = zip(range(count), numbers_in_german)
    
    for position, number in iterator:
        yield number
        
for num in count_to(4):
    print("{}".format(num))
