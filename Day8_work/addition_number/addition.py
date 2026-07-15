def add(a,b):
    return a+b
def sub(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def main():
    print("================Simpley Calculator===========")
    print("1. Addition.")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    choice =int(input("Enter your choice (1-4):"))

    num1= float(input("Enter the first number:"))
    num2=float(input("Enter Second number:"))

    if choice ==1:
        print(f"The result of addition is :{add(num1,num2)}")
    elif choice==2:
        print(f"The result of substraction is:{sub(num1,num2)}")
    elif choice==3:
        print(f"The result of Multiplication is:{multiply(num1,num2)}")
    elif choice ==4:
        if num2!=0:
            print(f"The result of Division is:{divide(num1,num2)}")
        else:
            print(f"Error: Division by zero is not allowed") 
    else:
        print("Division by Zero error")
 
main()

