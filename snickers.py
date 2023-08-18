price = 0.75
amount = int(input("Enter the amount of snickers you want to buy"))

price2 = price*amount
print("The total cost will be £",price2)

recieved = int(input("Enter the amount you would like to pay"))
print ("Thank you, I have received £",recieved)

change = recieved - price2
print("You will now receive £",change, "in change")
