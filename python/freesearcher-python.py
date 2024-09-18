import requests
import os

# Function to list all files in the 'Freesearcher-Python_Files' repository
def list_github_repo_files():
    repo_owner = "Martycat111"
    repo_name = "Freesearcher-Python_Files"

    # GitHub API URL to get the repository contents
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        # Parse the response and check if it's a directory
        contents = response.json()
        if isinstance(contents, list):
            print(f"Files in the repository '{repo_name}':")
            for content in contents:
                if content['type'] == 'file':
                    print(f"- {content['path']}")
                elif content['type'] == 'dir':
                    print(f"[Directory] {content['path']}")
        else:
            print(f"Failed to list files: Unexpected response format.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while listing files: {e}")

# Main loop for user input and handling download, list, or update
e = "e"
while e == "e":
    user = input(">>> ").strip().lower()

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if user == "list":
        # List all files in the 'Freesearcher-Python_Files' repository
        list_github_repo_files()
    else:
        # Construct the URL using the user's input to download a specific file
        url = f'https://raw.githubusercontent.com/Martycat111/Freesearcher-Python_Files/main/{user}'
        file_name = user

        # Use the script's directory for the file path
        file_path = os.path.join(script_dir, file_name)

        # Try to download the file
        response = requests.get(url)
        if response.status_code == 200:
            print("File found, downloading...")
            try:
                # Save the content to the specified file path in the script's directory
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {file_name} at {file_path}")
            except Exception as e:
                print(f"Error writing to file: {e}")
        elif response.status_code == 404:
            print(f"Error: The file '{file_name}' was not found in the repository.")
        else:
            print(f"An error occurred: {response.status_code}")
