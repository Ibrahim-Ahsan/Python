num1 = int(input("Enter the first number "))
print("You have entered the number ", num1)
num2 = int(input("Enter the second number "))
print("You have entered the number ", num2)

division = num1 / num2
rounded = round(division,0)

ans1 = num2 * rounded

ans2 = num1 - ans1

print (num2,"goes into",num1,",",rounded,"times","with",ans2,"left over")
