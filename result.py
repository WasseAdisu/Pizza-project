from filee import *

def result():
    global price
    for p in price_list:
        price += p
    print(f"you bought pizza, the price is: {price}")