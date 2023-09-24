import customtkinter
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://pixel-bucks:6Z8hRowG2STzw0gM@pixel-bucks.1mjf2ug.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
)
db = cluster["pixel-bucks"]
c = db["pixel-bucks"]

balance = 100

def sendmoney():
    dateiname = "userdata.txt"

    try:
        with open(dateiname, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Benutzername: "):
                    saved_username = line.split(": ")[1].strip()
                elif line.startswith("Passwort: "):
                    saved_passwort = line.split(": ")[1].strip()

        print(f"Benutzername aus der Datei: {saved_username}"" saved_username")
        print(f"Passwort aus der Datei: {saved_passwort}")

    except FileNotFoundError:
        print("Du bist ein schlechter coder!")

    balance = c.find_one({"username": saved_username, "password": saved_passwort}, {"_id": 0, "balance": 1})
    recieversbalance = c.find_one({"username": entry2.get()}, {"_id": 0, "balance": 1})

    label1.configure(text=f"Your Balanace: {balance['balance']}")

    print(f"You Balance: {balance}")
    sendBalance = entry1.get()
    print(sendBalance)

    reciever = entry2.get()
    print(reciever)

    if sendBalance == "":
        print("Invalid input!")
        label2.configure(text="Invalid input!")

    elif str(c.find_one({"username": reciever})) == "None":
        print("Invalid input!")
        label2.configure(text="Invalid input!")

    else:
        amount = int(entry1.get())
        if balance["balance"] - amount < 0:
            amount = 0

        balance["balance"] -= int(amount)
        recieversbalance["balance"] += int(amount)

        if amount == 0:
            label2.configure(text="You don't have enough Money!")

        elif saved_username == reciever:
            label2.configure(text="You can not send Money to your self!")
        else:
            label2.configure(text=f"You sent {entry1.get()}$ to {entry2.get()}!")
            label1.configure(text=f"Your Balanace: {balance['balance']}")

            c.update_one({"username": saved_username}, {"$set": balance})
            c.update_one({"username": reciever}, {"$set": recieversbalance})



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Pixel-Bucks")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text=f"Your Balance: {balance}")
label1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Amount")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Person")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Send", command=sendmoney)
button.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="")
label2.pack(pady=12, padx=10)

root.mainloop()

sendmoney()
