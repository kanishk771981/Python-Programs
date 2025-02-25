import math

#function for Euclidean distance
def distance(x : int , y : int):
    return math.sqrt(x**2 + y**2)

#taking user input
x = int(input("Enter x- coordinate"))
y = int(input("Enter y- coordinate"))

#storing the return value in result
result = distance(x,y)

print(f"distance between({x},{y}) and (0,0) is :{result} ")