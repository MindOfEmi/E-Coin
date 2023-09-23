import random
import string
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://pixel-bucks:6Z8hRowG2STzw0gM@pixel-bucks.1mjf2ug.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
db = cluster["pixel-bucks"]
c = db["pixel-bucks"]


def generate_id(digit):
    characters = string.ascii_lowercase + string.digits
    _id = ''.join(random.choice(characters) for _ in range(digit))
    return _id


login = input("Login or Register? (l/r): ")
if login == "l":
    l_username = input("Username:")
    l_password = input("Password: ")
    login = c.find_one({"username": l_username, "password": l_password}, {"_id": 0, "balance": 1})
    balance = input("How much do you want to send?")
    print(balance)
    login["balance"] -= int(balance)
    c.update_one({"username": "MindOfEmi"}, {"$set": login})

elif login == "r":
    username = input("Username: ")
    password = input("Password: ")

    c.insert_one({"_id": generate_id(16),
                  "username": username,
                  "password": password,
                  "balance": 100})
