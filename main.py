import random
import string
import pymongo
from pymongo import MongoClient
from colorama import Fore
import re

cluster = MongoClient(
    "mongodb+srv://pixel-bucks:6Z8hRowG2STzw0gM@pixel-bucks.1mjf2ug.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
)
db = cluster["pixel-bucks"]
c = db["pixel-bucks"]


def generate_id(digit):
    characters = string.ascii_lowercase + string.digits
    _id = ''.join(random.choice(characters) for _ in range(digit))
    return _id


login = input("Login or Register? (l/r): ")

# Log into your Account
if login == "l":
    user = input("Username: ")
    user_password = input("Password: ")

    if str(c.find_one({"username": user})) != "None" and str(c.find_one({"password": user_password})) != "None":
        print(Fore.CYAN + f"Welcome back {user}!")
    else:
        print(Fore.RED + "Wrong Username or Password! Be sure that you have an Account!")
        print(Fore.RED + "Please restart!")
        quit()

    
    def sendmoney():
        print("You Balance: " + str(c.find_one({"username": user}, {"_id": 0, "balance": 1})["balance"]))
        sendBalance = input(Fore.LIGHTYELLOW_EX + "How much do you want to send?: ")

        if sendBalance == "" or re.search('[a-zA-Z]', sendBalance):
            print(Fore.RED + "Invalid input!")
            sendmoney()

        reciever = input("To whom you want to send? (Username): ")
        verifyReciever = c.find_one({"username": reciever})

        if str(verifyReciever) == "None":
            print(Fore.RED + "User does not exist!")
            sendmoney()

        sendersBalance = c.find_one({"username": user, "password": user_password}, {"_id": 0, "balance": 1})
        recieversBalance = c.find_one({"username": reciever}, {"_id": 0, "balance": 1})
    
        if sendersBalance.get("balance", 0) - int(sendBalance) < 0:
            print(Fore.RED + "You don't have enough Money!")
            sendmoney()
    
        # Sending Money
        elif sendersBalance.get("balance", 0) - int(sendBalance) >= 0:
            sendersBalance["balance"] -= int(sendBalance)
            recieversBalance["balance"] += int(sendBalance)
            
            c.update_one({"username": user}, {"$set": sendersBalance})
            c.update_one({"username": reciever}, {"$set": recieversBalance})
    
            print(Fore.LIGHTGREEN_EX + f"You sent {sendBalance} to {reciever}!")
            sendmoney()

    sendmoney()

# Create Account
elif login == "r":
    username = input("Username: ")
    password = input("Password: ")

    if c.find_one({"username": username}) and str(c.find_one({"password": password})) == "None":
        print(Fore.RED + "This Username already exist!")
        print("Please restart!")
        quit()

    elif c.find_one({"username": username, "password": password}):
        print(Fore.RED + "Username and Password is already in use! Please login!")
        print("Please restart!")
        quit()

    else:
        c.insert_one({"_id": generate_id(16),
                      "username": username,
                      "password": password,
                      "balance": 100})

    print(Fore.CYAN + f"Welcome {username} to the Banksystem from Pixel-Bucks!")
    print(Fore.LIGHTYELLOW_EX + "Please restart the Program to get access!")

elif login != "l" or "r":
    print(Fore.RED + "Please enter " + Fore.LIGHTYELLOW_EX + "l" + Fore.RED + " for login or " + Fore.LIGHTYELLOW_EX + "r" + Fore.RED + " for register!")
    print(Fore.RED + "Please restart!")
