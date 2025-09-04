# Question 1 :Basic Caculator
#defining the functions

def add(num1,num2):
    return(num1 + num2)

def subtract(num1,num2):
    return(num1 - num2)

def multiply(num1,num2):
    return (num1 * num2)
def divide(num1, num2):
    if num2!=0:
        return(num1/num2)

print("Basic Caculator Opretaion")
try:
    choice= input("Choose operation(+, -, *, /)" "or" "exist to quit: ")
    while True: 
        num1= input("Enter first number:")
        num2= input("Enter the second number:")
        if choice == "+":
            print(f"Result: {num1 + num2}")
        elif choice == "-":
            print(f"Result: {num1 - num2}")
        elif choice == "*":
            print(f"Result: {num1 * num2}")
        elif choice == "/":
            print(f"Result: {num1 /num2}")
        elif choice == "exist":
            print("Existing the program")
        else:
            break
except Exception as e:
    print("error")



# Question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")



#Question 3

while True:
      try:
          age = int(input("Enter your age (or type exit to quit): "))
          if age >= 18:
              print("You can vote")
          elif age == "exit":
              print("Goodbye!")
          else:
            print("You cannot vote")
            break
      except Exception as e:
        print("Invalid input")
