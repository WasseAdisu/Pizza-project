from filee import *

def delivery():
    global price
    deliver = input("Do you live in beerSheba? y/n: ")
    if deliver == "y":
         price = price + 20

    else:
        price = price + 60
    price_list.append(price)