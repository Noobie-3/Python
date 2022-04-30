
from time import monotonic, time, sleep


count = 1
amount = 1   
tax = float(1)
price = 10
thingsBought = 1
MoneyMadePerSec = 1
total = 0
markup = 0
def buy():
    #changes the price to be higher and gives you more of the item if you have enough
    global count
    global amount
    global tax
    global price
    global thingsBought
    global MoneyMadePerSec
    global markup
    global total
    total = (total - price)
    thingsBought = thingsBought + 1
    markup = (.15 * thingsBought)
    MoneyMadePerSec = (thingsBought * markup)
    price = price + (price * .35)

    
    
def doThing():
    global count
    global amount
    global price    
    global thingsBought
    global MoneyMadePerSec
    global total
    total = (total + MoneyMadePerSec)
    


while True:
    sleep(1 - time() % 1)
    doThing()
    print(total)
    

while count >= 999:
    print("hello")
    

        

#testttt