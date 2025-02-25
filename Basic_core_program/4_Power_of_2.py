#asking user for input
N = int(input("Enter a value of N ,0<=N<31"))

#using if condition to ensure the input is between 0 to 31
if 0 <= N < 31:
    
# for loop for calculating power of 2
    for i in range(N + 1):
        print(f"2^{i} = {2**i}")
else:
    print("enter a number between 0 and 31")