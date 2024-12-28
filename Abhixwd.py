import os
import sys
import datetime
from time import sleep
import requests
from colorama import Fore, init

# Function to clear the terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Logo function
def logo():
    print(Fore.YELLOW + "==================== FACEBOOK TOOL ====================")

def send_message(access_token, convo_id, message):
    """
    Sends a message to the specified conversation ID using the provided access token.
    """
    url = f"https://graph.facebook.com/v15.0/t_{convo_id}/"
    parameters = {'access_token': access_token, 'message': message}
    try:
        response = requests.post(url, json=parameters)
        if response.status_code == 200:
            print(Fore.GREEN + f"[✔] Message Sent successfully: {message}")
        else:
            print(Fore.RED + f"[x] Failed to Send: {message} - {response.json()}")
    except Exception as e:
        print(Fore.RED + f"[x] Error: {str(e)}")

# Initialize colorama
init(autoreset=True)

# Clear screen and print logo
cls()
logo()
print(Fore.YELLOW + "---------------------------------------------------------------------")

# Display script details
print(Fore.MAGENTA + "-=[ Facebook Tool Created by L3g3nD Darshit ]=-")
print(Fore.YELLOW + "-=[ Contact Us ::https://www.facebook.com/profile.php?id=100064189448340 ]=-\n")
now = datetime.datetime.now()
print(Fore.GREEN + f"Start Time ==> {now.strftime('%Y-%m-%d %I:%M:%S %p')}")
print(Fore.GREEN + "# Tool Fucker == > [ DarshīīT YadaV]\n")

# User inputs for token, conversation ID, message file, and delay
mo = input(Fore.CYAN + "[+] Mobile Number :: ")
token_file = input(Fore.CYAN + "[+] Input Token File Name :: ")
print()

# Read access token from file and validate
try:
    with open(token_file, 'r') as f2:
        access_token = f2.read().strip()
except FileNotFoundError:
    print(Fore.RED + "[x] Token file not found!")
    sys.exit()

# Fetch sender's profile information
url = 'https://graph.facebook.com/v15.0/me'
payload = {'access_token': access_token}
response = requests.get(url, params=payload)

if response.status_code != 200:
    print(Fore.RED + "[x] Token Invalid..!!")
    print(Fore.RED + f"[x] Response: {response.json()}")
    sys.exit()

data = response.json()
sender_name = data.get('name', 'Unknown User')
print(Fore.GREEN + f"Your Profile Name: {sender_name}\n")

# Input for conversation ID and message file
convo_id = input(Fore.CYAN + "[+] Enter Conversation ID (t_{UID}) :: ")
ms = input(Fore.CYAN + "[+] Enter the Message File Name :: ")
delay = int(input(Fore.CYAN + "[+] Enter Delay Between Messages (in seconds) :: "))

# Validate the message file
try:
    with open(ms, 'r') as mf:
        messages = mf.readlines()  # Read all lines from the file
except FileNotFoundError:
    print(Fore.RED + "[x] Message file not found!")
    sys.exit()

# Send messages
while True:
    print(Fore.GREEN + f"\n[✔] Sending Messages as {sender_name}...\n")
    for message in messages:
        message = message.strip()  # Clean up any extra spaces or newline characters
        if message:
            send_message(access_token, convo_id, message)
            sleep(delay)  # Delay between messages
    print(Fore.CYAN + "\n[✔] All messages sent! Restarting...\n")