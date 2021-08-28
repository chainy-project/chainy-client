import time
import random
import requests
import os

print("Welcome to the Chainy client v1")
BASE_URL = "http://45.138.72.87"
print("1: Login")
print("2: Check balance")
print("3: Send")
print("4: Register")
func = int(input("Select function:"))
if func == 4:
    try:
        open(".chainy/wallet")
        print("You have already registered")
        raise SystemExit()
    except Exception:
        pass
    private_key = (
        str(int(time.time()))
        + str(random.randint(99999, 9999999999))
        + str(random.randint(99999, 9999999999))
        + str(random.randint(99999, 9999999999))
        + str(random.randint(99999, 9999999999))
    )
    print(f"Your private key: {private_key}")
    print("WARNING: IF YOU LOST YOUR PRIVATE KEY, YOU LOST ALL COINS")
    address = requests.post(f"{BASE_URL}/seeaddr?private_key={private_key}").json()
    address = address["address"]
    print(f"Your address: {address}")
    os.mkdir(".chainy")
    open(".chainy/wallet", "w").write(private_key)
if func == 1:
    print("You are changing a private key")
    private_key = str(input("Enter new private key:"))
    address = requests.post(f"{BASE_URL}/seeaddr?private_key={private_key}").json()
    address = address
    print(f"Your address: {address}")
    try:
        os.mkdir(".chainy")
    except Exception:
        pass
    open(".chainy/wallet", "w").write(private_key)
if func == 2:
    try:
        private_key = open(".chainy/wallet").read()
    except Exception:
        print("Register or login firstly!")
        raise SystemExit()
    address = requests.post(f"{BASE_URL}/seeaddr?private_key={private_key}").json()
    address = address["address"]
    balance = requests.post(f"{BASE_URL}/balance?address={address}").json()
    print(f"Your balance is {balance}")
if func == 3:
    try:
        private_key = open(".chainy/wallet").read()
    except Exception:
        print("Register or login firstly!")
        raise SystemExit()
    reciv = str(input("Reciver:"))
    amount = int(input("Amount:"))
    response = requests.post(
        f"{BASE_URL}/send?private_key={private_key}&amount={amount}&address={reciv}"
    ).json()
    print(response)

