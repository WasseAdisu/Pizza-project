from filee import *

def size():
    global price
    size = input("what size pizza do you want please?: ")
    if size in pizaa_dict:
        price = pizaa_dict[size]
        price_list.append(price)