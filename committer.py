import os
import time
from datetime import datetime

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Replace this with your real GitHub token
GITHUB_REPO = "workspacereddy/commits"
REPO_DIR = "/app/repo"

def clone_repo():
    if not os.path.exists(REPO_DIR):
        os.system(f"git clone https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git {REPO_DIR}")

def make_dummy_commit():
    os.chdir(REPO_DIR)
    with open("dummy.txt", "a") as f:
        f.write(f"Auto commit at {datetime.now()}\n")
    os.system("git add .")
    os.system(f'git commit -m "Auto commit at {datetime.now()}"')
    os.system("git push origin main")

# Run
clone_repo()

while True:
    make_dummy_commit()
    time.sleep(3600)
