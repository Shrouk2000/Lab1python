#Q1
#  bill_amount = 47.28
# tip_percentage = 0.15
# tip_amount = bill_amount * tip_percentage
# total_amount = bill_amount + tip_amount
# each_person_share = total_amount / 2
# print(f"Each person needs to pay: ${each_person_share:.2f}")


## Q2

# num1 = float(input("Enter the first number: "))

# num2 = float(input("Enter the second number: "))


# if num2 != 0:
#     result = num1 / num2
#     print(f"The result of dividing {num1} by {num2} is: {result:.2f}")
# else:
#     print("Error: Division by zero is not allowed.")


# Q3
# Define the variables

# word1 = "How"
# word2 = "do"
# word3 = "you"
# word4 = "like"
# word5 = "{}"
# word6 = "so"
# word7 = "far?"
# sentence = f"{word1} {word2} {word3} {word4}{word5} {word6} {word7}"

# print(sentence)


# Q4
# Define the variables
# word1 = "How"
# word2 = "do"
# word3 = "you"
# word4 = "like"
# word5 = " {}"
# word6 = "so"
# word7 = "far?"

# word7 = word7.replace('?', '!')
# sentence = f"{word1} {word2} {word3} {word4}{word5} {word6} {word7}"
# print(sentence)


#q5

# input = input("Please enter a statement: ")

# length_of_input = len(input)

# print(f"The length of your statement is: {length_of_input} characters")


# Q6

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):

    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")


    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input. Please select a valid operation.")


calculator()

