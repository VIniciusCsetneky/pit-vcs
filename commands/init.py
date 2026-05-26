import os
import json
from core.repo import get_repo_path, repo_exists

def init():
    if repo_exists():
        print("Repositório já existe.")
        return

    repo = get_repo_path()
    os.makedirs(os.path.join(repo, "objects"))

    with open(os.path.join(repo, "HEAD"), "w") as f:
        f.write("")

    with open(os.path.join(repo, "index.json"), "w") as f:
        json.dump({}, f)

    with open(os.path.join(repo, "commits.json"), "w") as f:
        json.dump([], f)

    with open(os.path.join(repo, "auth.json"), "w") as f:
        json.dump({"users": [], "logged_in": None}, f)

    print("Repositório pit iniciado.")