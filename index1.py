value1 = input("Enter the 1st value")
value2 = input("Enter the 2nd value")
value3 = input("Enter the 3rd value")
value4 = input("Enter the 4th value")

pass1 = (value1[0])

pass2 = (value2[0:2])

pass3 = (value3[2:4])

pass4 = (value4[3:])
pass5 = pass4.upper()

password = pass1+pass2+pass3+pass5
print (password)
