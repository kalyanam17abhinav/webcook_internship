import math

def add():
    a,b=map(float,input("Enter first and second value: ").split())
    return (a+b)

def subtract():    
    a,b=map(float,input("Enter first and second value: ").split())    
    return(a-b)

def multiply():
    a,b=map(float,input("Enter first and second value: ").split())
    return (a*b)

def divide():
    a,b=map(float,input("Enter first and second value: ").split())
    try:
        return (a/b)
    except ZeroDivisionError:
        return "can't divide by zero"
    
def expo():
    a=float(input("Enter the value: "))
    return math.exp(a)

def trigo():
    a=float(input("Enter the value: "))
    print(f"sine ({a}) value is: ",math.sin(math.radians(a)))
    print(f"cosine ({a}) value is: ",math.cos(math.radians(a)))
    print(f"tangent ({a}) value is: ",math.tan(math.radians(a)))

def eval_expr():
    a=input("Enter the expression to solve: ")
    try:
        return eval(a)
    except Exception as e:
        return f"Error occured: {e}"


user_choice=0

while(user_choice==0):
    try:
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponential\n6. Trigonometric\n7. Parentheses")
        user_input=int(input("Enter your choice: "))
        if user_input==1:
            print(add())
        elif user_input==2:
            print(subtract())
        elif user_input==3:
            print(multiply())
        elif user_input==4:
            print(divide())
        elif user_input==5:
            print(expo())
        elif user_input==6:
            trigo()
        elif user_input==7:
            print(eval_expr())
        else:
            print("Enter valid choice")
        user_choice=int(input("Enter 0 to continue calculation, -1 to stop: "))
    except Exception as e:
        print(e)