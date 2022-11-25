from delivery import delivery
from size import size
from extra import  extra
from filee import *

def runner():
    while True:
        age = int(input("Enter your age? "))
        if age < 18:
            break
        size()
        extra()
        delivery()
        con = input("Do you wanna continue? y/n: ")
        if con == "n":
            break

