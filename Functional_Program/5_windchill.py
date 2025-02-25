import math
#function for  calculating wind_chill
def wind_chill(t,v):
    if(t > 50 or 3 > v > 120):
        print("invalid input ,please ensur t < 50 or 3 < t < 120")
    else:
        w = 35.74 + 0.6215*t + (0.4275 * t - 35.75) * math.pow(v, 0.16)

    return w

#asking input from user
t = float(input("enter temperature in Fahrenheit "))
v = float(input("enter wind speed  in M/H "))

result = wind_chill(t,v)
print(f"wind chill is {result}")

    