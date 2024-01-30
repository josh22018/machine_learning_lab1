#Euclidian distance.

import math
def euclidian_distance(a,b):
    dist=0 
    if len(a) == len(b):
        for i in range(len(a)):
            dist+= (a[i]-b[i])**2
        return math.sqrt(dist)
    else:
        print("Points must be having the same no of co-ordinates")
x=[1,9,9]
y=[1,2,3]
print("The distance between the two points is ",euclidian_distance(x,y))
