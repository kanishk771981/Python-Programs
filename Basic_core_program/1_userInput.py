#asking user for input
user_name =  input("Enter your name")

#using if condition and len function 
#to ensure lenfth > 3
if len(user_name) >=3 :
    print(f"Hello {user_name} ,How are you")
else :
    print("please enter minimum 3 char")    
