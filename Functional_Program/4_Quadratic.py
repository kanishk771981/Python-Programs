import math

#function for finding roots
def roots(a, b, c):

    delta = b*b -4*a*c
    if delta > 0:
        Root_1 = (-b + math.sqrt(delta))/(2*a)
        Root_2 = (-b - math.sqrt(delta))/(2*a)
        print(f"Two roots are {Root_1} and {Root_2} ")

    elif delta == 0:
        Root = -b /(2*a)
        print(f" one Root is: {Root} ")
    
    else:
        print("Equation has no real roots")

   

    
#taking input from user
a = int(input("enter value of a"))
b = int(input("enter value of b"))
c = int(input("enter value of c"))

if a == 0:
    print("Invalid !! a cannot be 0 in quadratic equation")
else:
    roots(a,b,c)
