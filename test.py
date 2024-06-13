import random
ket = 360/37
highway = [0,32,15,19,4,
           21,2,25,17,34,
           6,27,13,36,11,
           30,8,23,10,5,
           24,16,33,1,20,
           14,31,9,22,18,
           29,7,28,12,35,
           3,26]
plunk = []
for i in range(37):
    plunk.append(0)
def punk(num):
    for i in range(37):
        if (ket) * i < num < (ket) * (i + 1):
            return highway[i]


for i in range(20000):
    punk(random.uniform(0.01,360))
gump = 0
print(punk(360))
for i in range(360):
    print(punk(i))