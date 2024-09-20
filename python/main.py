import os
import requests
import json

YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print(f"Welcome to V1.4 of the FreeSearcher CLI {YELLOW}Python Edition{RESET}{BLUE}.")

commands_url = "https://raw.githubusercontent.com/TheFreeWeb/FreeSearcher/refs/heads/main/python/commands.json"

def get_commands():
    response = requests.get(commands_url)
    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            return {}
    else:
        print(f"Failed to fetch commands. Status code: {response.status_code}")
        return {}

def download_file(command):
    commands = get_commands()
    if command in commands:
        url = commands[command]
        file_name = url.split('/')[-1]
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(os.getcwd(), file_name), 'wb') as file:
                file.write(response.content)
            print(f"{file_name} downloaded successfully.")
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")
    else:
        print(f"Command '{command}' not recognized.")

user_input = input(">>> ")
download_file(user_input)
