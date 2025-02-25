#asking user for the value of rows and columns
rows = int(input("enter the value for row"))
cols = int(input("enter the value for columns"))

# crweating a empty list[] 
array =[]

print( "enter values of rows and column")

for i in range(rows):
    while True:
      row = list(map(int ,input().split()))
      if len(row) == cols:
         array.append(row)
         break
      else:
         print("invalid entery")
    

#printing the array
print("your 2D Array is")
for row in array:
    print(" ".join(map(str,row)))


