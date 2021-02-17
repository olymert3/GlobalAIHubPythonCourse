import random

mylist=[2,3,5,7,11,13,17,19,23]
for i in mylist:
    a=random.sample(mylist,3)
    b=random.sample(mylist,3)
    c=random.sample(mylist,3)
print(a)
print(b)
print(c)
