
def seed(seed = None, a=0, b=10,  N=10**12, integer=True):
   
    if seed:
        global rand_num_generator 
        if integer: 
            hash_plus = lambda j: int(a + (b-a)*(abs(hash(str(hash(str(seed) + str(j+1))))) % 10**13)/ 10**13)
        else:
            hash_plus = lambda j: a + (b-a)*(abs(hash(str(hash(str(seed) + str(j+1))))) % 10**13)/ 10**13
        rand_num_generator =  (hash_plus(j) for j in range(N))
  
    return next(rand_num_generator)
    
    