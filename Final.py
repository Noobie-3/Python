
from time import time, sleep


count = 1
amount = 1   
tax = float(1)
price = 10
def buy():
    global count
    global amount
    global tax
    global price
    global thingsBought
    count = count - (price * tax)
    amount = amount + 1
    
def doThing():
    global count
    global amount
    global price    
    global thingsBought
    thingsBought = amount
    count = count + (count * thingsBought)
    thingsBought
    


while True:
    sleep(1 - time() % 1)
    doThing()
    print(count)
    
    if count >= (price * tax):
        buy()
        print(round(tax))


