import os
import requests
import json
from tqdm import tqdm  # Progress bar library
import time
from playsound import playsound  # Import the playsound library

# ANSI escape codes for colors
YELLOW = "\033[33m"
BLUE = "\033[34m"
WHITE = "\033[37m"  # Added white color
RESET = "\033[0m"

# Welcome message
print(f"Welcome to V1.4 of the FreeSearcher CLI {YELLOW}Python {BLUE}Edition{RESET}.")

commands_url = "https://raw.githubusercontent.com/TheFreeWeb/FreeSearcher/refs/heads/main/python/commands.json"

def play_error_sound():
    try:
        playsound('errorXP.mp3')  # Assumes the file is in the current directory
    except Exception:
        pass  # Silently handle any errors related to playing the sound

def get_commands():
    try:
        response = requests.get(commands_url)
        if response.status_code == 200:
            try:
                return json.loads(response.text)
            except json.JSONDecodeError:
                play_error_sound()  # Play error sound
                return {}
        else:
            play_error_sound()  # Play error sound
            return {}
    except Exception:
        play_error_sound()  # Play error sound
        return {}

def download_file(command):
    try:
        commands = get_commands()
        if command in commands:
            url = commands[command]
            file_name = url.split('/')[-1]

            retries = 5  # Number of retries for download
            for attempt in range(retries):
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    with open(os.path.join(os.getcwd(), file_name), 'wb') as file, tqdm(
                        desc=file_name,
                        total=total_size,
                        unit='B',
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for data in response.iter_content(65536):  # 64 KB chunks
                            size = file.write(data)
                            bar.update(len(data))
                    print(f"{file_name} downloaded successfully.")
                    break
                else:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"Attempt {attempt + 1} failed: {response.status_code}. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
            else:
                play_error_sound()  # Play error sound
        else:
            play_error_sound()  # Play error sound
    except Exception:
        play_error_sound()  # Play error sound

while True:
    user_input = input(">>> ").strip()  # Strip spaces/newlines
    if not user_input:  # Check if input is empty
        print("Please enter a valid command.")
    else:
        download_file(user_input)
