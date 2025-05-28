import os
import datetime
import subprocess

# === SET THESE ===
GIT_NAME = "workspacereddy"
GIT_EMAIL = "workspacereddy@gmail.com"
REPO_DIR = "/home/your_pythonanywhere_username/daily-logger"
BRANCH = "main"  # Or "master" if that's your default branch

def make_commit():
    os.chdir(REPO_DIR)

    # Set user config so GitHub recognizes you
    subprocess.run(["git", "config", "user.name", GIT_NAME])
    subprocess.run(["git", "config", "user.email", GIT_EMAIL])

    # Create/update log file
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - Daily log\n")

    # Commit and push
    subprocess.run(["git", "add", "log.txt"])
    subprocess.run(["git", "commit", "-m", "Daily update"])
    subprocess.run(["git", "push", "origin", BRANCH])

if __name__ == "__main__":
    make_commit()
