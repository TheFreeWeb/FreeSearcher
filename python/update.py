import requests
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
# Specific logic for updating 'freesearcher-python.py'
url = 'https://raw.githubusercontent.com/Martycat111/Freesearcher-Python_Files/main/freesearcher-python.py'
file_name = 'freesearcher-python.py'

# Use the script's directory for the file path
file_path = os.path.join(script_dir, file_name)

# Try to download the update
response = requests.get(url)
if response.status_code == 200:
    print("Update found, downloading...")
    try:
        # Save the update to the file path in the script's directory
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Updated {file_name} at {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")
elif response.status_code == 404:
    print(f"Error: The update file '{file_name}' was not found in the repository.")
else:
    print(f"An error occurred: {response.status_code}")
