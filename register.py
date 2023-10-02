import os
import customtkinter
import random
import string
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://pixel-bucks:6Z8hRowG2STzw0gM@pixel-bucks.1mjf2ug.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
)
db = cluster["pixel-bucks"]
c = db["pixel-bucks"]


def generate_id(digit):
    characters = string.ascii_lowercase + string.digits
    _id = ''.join(random.choice(characters) for _ in range(digit))
    return _id


def register():
    # Create Account
    username = entry1.get()
    password = entry2.get()

    if c.find_one({"username": username}) and str(c.find_one({"password": password})) == "None":
        print("This Username already exist!")
        label2.configure(text="This Username already exist!")

    elif c.find_one({"username": username, "password": password}):
        print("Username and Password is already in use! Please login!")
        label2.configure(text="Username and Password is already in use! Please login!")

    else:
        dateiname = "userdata.txt"
        username = username
        password = password

        try:
            with open(dateiname, "x") as file:
                file.write(f"Benutzername: {username}\n")
                file.write(f"Passwort: {password}\n")
                print(f"Benutzerdaten wurden in die Datei '{dateiname}' geschrieben.")
        except FileExistsError:
            print(f"Die Datei '{dateiname}' existiert bereits und enthält Benutzerdaten.")

    print(f"Welcome {username} to the Banksystem from Pixel-Bucks!")
    label2.configure(text=f"Starting Login System...")
    os.startfile("loginexe.exe")

    c.insert_one({"_id": generate_id(16),
                  "username": username,
                  "password": password,
                  "balance": 100})

    


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Pixel-Bucks")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="Register System")
label1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Register", command=register)
button.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="")
label2.pack(pady=12, padx=10)

root.mainloop()
