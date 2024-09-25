import os
import requests
import json
from tqdm import tqdm
import time

YELLOW = "\033[33m"
BLUE = "\033[34m"
WHITE = "\033[37m"
RESET = "\033[0m"

print(f"Welcome to V1.4 of the FreeSearcher CLI {YELLOW}Python {BLUE}Edition{RESET}.")

commands_url = "https://raw.githubusercontent.com/TheFreeWeb/FreeSearcher/refs/heads/main/python/commands.json"


def get_commands():
    try:
        response = requests.get(commands_url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Failed to fetch commands: {response.status_code}")
            return {}
    except Exception as e:
        print(f"An error occurred while fetching commands: {e}")
        return {}


def download_file(command):
    try:
        commands = get_commands()
        if command in commands:
            url = commands[command]
            file_name = url.split('/')[-1]

            retries = 5
            success = False  # Track if download was successful

            for attempt in range(retries):
                try:
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
                            for data in response.iter_content(65536):
                                file.write(data)
                                bar.update(len(data))
                        print(f"{file_name} downloaded successfully.")
                        success = True
                        break
                    else:
                        wait_time = 2 ** attempt
                        print(f"Attempt {attempt + 1} failed: {response.status_code}. Retrying in {wait_time} seconds...")
                        time.sleep(wait_time)
                except Exception as e:
                    print(f"Error occurred during attempt {attempt + 1}: {e}")
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)

            if not success:  # After retries fail, trigger error message
                print("Failed to download the file after multiple attempts.")
        else:
            print(f"{YELLOW}File '{command}' not found.{RESET}")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")


def list_available_files():
    commands = get_commands()
    if commands:
        print(f"{YELLOW}Available Files to Download:{RESET}")
        for command in commands:
            print(f"- {BLUE}{command}{RESET}")
    else:
        print("No files available or an error occurred.")


while True:
    user_input = input(">>> ").strip()
    if not user_input:
        print("Please enter a valid file name.")
    elif user_input == "search-list":
        list_available_files()
    elif user_input == goob or Goob:
        print(f"{RED}goob.exe{BLUE} installed succsessfully. {YELLOW}WATCH OUT!{RESET}")
    else:
        download_file(user_input)
