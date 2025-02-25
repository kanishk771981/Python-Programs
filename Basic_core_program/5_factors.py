#asking user for input
num = int(input("enter a number to find the prime factors"))

#checking for factors of 2
while num % 2 == 0:
    print(2)
    num = num/2

#checking for odd factors
i=3
while i*i <= num:
    while num % i == 0:
        print(i)
        num = num/i
#incrementing by 2 for odd num
i =i+2      

if num > 2 :
    print(num)


