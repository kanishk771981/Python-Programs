#asking user for input
year = input("Enter a 4 digit year")

#using if condition for ensuring 4-digit year
if len((year)) == 4:
    year = int(year)
    
#using if condition for checking leap year
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a Leap Year")

    else:
        print(f"{year} is not a leap year")    

else:
    print("enter a 4 digit year")        

   



