import os
import time
from datetime import datetime

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = "workspacereddy/commmits"
REPO_DIR = "./repo"

def clone_repo():
    if not os.path.exists(REPO_DIR):
        os.system(f"git clone https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git {REPO_DIR}")

def setup_git_user():
    os.chdir(REPO_DIR)
    os.system('git config user.email "workspacereddy@gmail.com"')
    os.system('git config user.name "workspacereddy"')

def make_dummy_commit():
    os.chdir(REPO_DIR)
    with open("dummy.txt", "a") as f:
        f.write(f"Auto commit at {datetime.now()}\n")
    os.system("git add dummy.txt")
    os.system(f'git commit -m "Auto commit at {datetime.now()}"')
    os.system("git push origin main")

clone_repo()
setup_git_user()

while True:
    make_dummy_commit()
    time.sleep(3600)
