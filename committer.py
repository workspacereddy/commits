import os
import time
from datetime import datetime

# Path where your repo is cloned inside Render
REPO_DIR = "/app/repo"  # Render mounts your project root at /app

def make_dummy_commit():
    os.chdir(REPO_DIR)
    
    # Make a dummy change
    with open("dummy.txt", "a") as f:
        f.write(f"Commit At {datetime.now()}\n")
    
    # Git commands
    os.system("git add .")
    os.system(f'git commit -m "Auto commit at {datetime.now()}"')
    os.system("git push origin main")  # Change to your branch if not 'main'

# Run forever
while True:
    make_dummy_commit()
    time.sleep(3600)  # Wait 1 hour (3600 seconds)
