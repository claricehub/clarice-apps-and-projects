from random import choice 

def generate_name():
    names = ["Alice", "Frank"]
    
    return choice(names)
def generate_age():
    for i in range(1,101):
        ages = list(range(1,101))
    
    return choice(ages)