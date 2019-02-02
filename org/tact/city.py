import random as r

def get_friendship_meter(name1, name2):
    
    print('Your Name : ', name1)
    print("Your friend Name : ", name2)
    meter = r.randint(1, 100)   
    print("Your friendship meter : ", meter)
    
get_friendship_meter('sam', 'purnima')