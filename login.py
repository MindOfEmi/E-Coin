import customtkinter
import os
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://pixel-bucks:6Z8hRowG2STzw0gM@pixel-bucks.1mjf2ug.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
)
db = cluster["pixel-bucks"]
c = db["pixel-bucks"]


# Log into your Account
def login():
    user = entry1.get()
    user_password = entry2.get()

    if str(c.find_one({"username": user})) != "None" and str(c.find_one({"password": user_password})) != "None":
        print(f"Starting the Bank System!")
        os.startfile("bank.py")
        quit()
    else:
        print("Wrong Username or Password! Be sure that you have an Account!")
        print("Please restart!")
        quit()


def startregister():
    label2.configure(text="Starting register program...")
    os.startfile("register.py")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Pixel-Bucks")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="Login System")
label1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Login", command=login)
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Register", command=startregister)
button2.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="")
label2.pack(pady=12, padx=10)

root.mainloop()
