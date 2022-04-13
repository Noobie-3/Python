#Starting Numbers/ input from user
from types import TracebackType


HourlyPayRate = float(input("Enter Your Hourly Pay: "))
HoursWorked = float(input("Enter Your Hours Worked: "))
taxRate = float(input("Enter Your Current Rate Of Tax as a Decimal: "))
Tax = int(0)
#the Calulations for the Calulator

TaxPercentage = taxRate / 100
GrossPay = HoursWorked * HourlyPayRate

Tax = GrossPay * TaxPercentage 
TakeHomePay = GrossPay - Tax


#Prints the data from before
print("Pay Check calculator")
print("The Hours Your Have Worked Are: ",round(HoursWorked, 2))
print("The Hourly PayRate That You Provided Was: ",round(HourlyPayRate,2))
print("\nYour Gross Pay is: ",round(GrossPay, 2),("$"))
print("Your Tax rate Is : ",round(TaxPercentage, 2),("%"))
print("Your Tax Amount Is: ",round(Tax, 2),("$"))
print("Your Get To take Home: ",round(TakeHomePay, 2),("$"))


