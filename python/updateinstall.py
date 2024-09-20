import requests, os
r = requests.get('https://raw.githubusercontent.com/Martycat111/Freesearcher-python-download/refs/heads/main/freesearcher-python.py')
if r.status_code == 200:
    try: open(os.path.join(os.path.dirname(__file__), 'freesearcher-python.py'), 'wb').write(r.content)
    except Exception as a: print(a)
else: print(r.status_code)
