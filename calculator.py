num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

choice = int(input("To use addition, enter the number 1. To use subtraction, enter the number 2. To use multiplication, enter the number 3. To use division, enter the number 4."))

if choice == 1:
    ans1 = num1 + num2
    print (num1, "+", num2, "=", ans1)

elif choice == 2:
    ans2 = num1 - num2
    print (num1, "-", num2, "=", ans2)

elif choice == 3:
    ans3 = num1 * num2
    print (num1, "*", num2, "=", ans3)

elif choice == 4:
    ans4 = num1 / num2
    print (num1, "/", num2, "=", ans4)

else:
    print("An invalid input was entered. Please try again")
