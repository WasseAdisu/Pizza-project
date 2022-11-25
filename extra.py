from filee import *

def extra():
    global price
    extra = input("Do you want extras? y/n")
    if extra == "y":
        price = price + 2
    else:
        pass
    price_list.append(price)