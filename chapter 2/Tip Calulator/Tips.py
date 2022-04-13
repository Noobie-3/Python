#The Infomation gave by the user
Cost = float(input("Input the cost of your meal please: "))
TipPercent = float(input("What percent would you like to tip?: "))
#the math for the tip and total
TipAmount = TipPercent / 100 * Cost
TotalAmount = Cost + TipAmount
print("Tip Calculator")
print("The cost of your meal was:            ",round(Cost, 2),"$")
print("The percent that you are tipping is:  ",round(TipPercent, 2),"%")
print("The amount that is owed is:           ",round(TipAmount, 2),"$")
print("Your total after tips is:             ",round(TotalAmount, 2),"$")