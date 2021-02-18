def prime_first(n):
   
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
    
def prime_second(n):
    
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
    
for x in range(1001):
    if x <= 500:
        if prime_first(x):
            print('{} is prime number prime_first'.format(x))
    else:
        if prime_second(x):
            print('{} is prime number prime_second'.format(x))