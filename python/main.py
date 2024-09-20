import os
import requests
import json

commands_url = "https://raw.githubusercontent.com/username/repo/branch/commands.json"

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

user_input = input("Enter command: ")
download_file(user_input)
