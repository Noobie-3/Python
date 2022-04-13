print("Tip Calculator\n")

cost = round(float(input("Input the cost of your meal please: ")),2)

#cost of the meal
print("Cost of meal:",round(cost,2),"$\n")

#15% tip
print("15%")
fifteen = cost * .15
print("Tip Amount:", round(fifteen,2), "$")
print("Total Amount Due", round(cost + fifteen,2),"$\n")

#20% tip
print("20%")
twenty = cost * .20
print("Tip Amount:", round(twenty,2), "$")
print("Total Amount Due", round(cost + twenty, 2),"$\n")

#25% tip 
print("25%")
twen5 = cost * .25
print("Tip Amount:", round(twen5,2), "$")
print("Total Amount Due", round(cost + twen5,2),"$\n")

