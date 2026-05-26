import json
import os
from .repo import get_repo_path

def read_json (filename):
    path = os.path.join(get_repo_path(), filename)
    if not os.path.isfile(path):
        return None
    with open(path, 'r') as f:
        return json.load(f)
    
def write_json (filename, data):
    path = os.path.join(get_repo_path(), filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def read_head():
    path = os.path.join(get_repo_path(), "HEAD")
    with open(path, 'r') as f:
        return f.read().strip()
    
def write_head(commit_id):
    path = os.path.join(get_repo_path(), "HEAD")
    with open(path, "w") as f:
        f.write(commit_id)