import os
import time
from datetime import datetime

GITHUB_USERNAME = "workspacereddy"
REPO_NAME = "commits"
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']  # Store this in Replit Secrets
REMOTE = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

def setup_git():
    os.system("git init")
    os.system(f"git remote add origin {REMOTE}")
    os.system("git config user.name 'workspacereddy'")
    os.system("git config user.email 'workspacereddy@gmail.com'")

def make_commit():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"Logged at {now}\n")
    
    os.system("git add .")
    os.system(f"git commit -m 'Update: {now}'")
    os.system("git push origin master")

if not os.path.isdir(".git"):
    setup_git()

while True:
    make_commit()
    print("Committed successfully, sleeping for 1 hour...")
    time.sleep(3600)
