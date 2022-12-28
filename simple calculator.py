#to make a simple calculator

#addition
def add(a,b):
    return a+b
#subtraction
def sub(a,b):
    return a-b
#multiplication
def mul(a,b):
    return a*b
#division
def div(a,b):
    return a/b
#for getting the remainder of division
def rem(a,b):
    return a%b
    
print("select the operation to be executed:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.remainder")

while True:
    
    choice=input("Enter the option 1/2/3/4/5:")
    
    if choice in ("1","2","3","4","5"):
        
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        
        if choice== "1":
            print("the Addition of",num1,"+",num2,"=",add(num1,num2))
        
        elif choice== "2":
            print("the Subtraction of",num1,"-",num2,"=",sub(num1,num2))
            
        elif choice== "3":
            print("the Multiplication of",num1,"*",num2,"=",mul(num1,num2))    

        elif choice== "4":
            print("the Division of",num1,"/",num2,"=",div(num1,num2))
            
        elif choice== "5":
            print("the Remainder of",num1,"%",num2,"=",rem(num1,num2))    

        next=input("can we another calculation (yes/no): ")
        if next== "no":
            break
        
    else:
        print("invalid input")





