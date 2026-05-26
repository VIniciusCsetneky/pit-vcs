import os

MYVCS_DIR = ".myvcs"

def get_repo_path():
    return os.path.join(os.getcwd(), MYVCS_DIR)

def repo_exists():
    return os.path.isdir(get_repo_path())

def require_repo():
    if not repo_exists():
        print("Erro, repositorio nao encontrado, rode 'pit init'para criar um novo repositorio")
        exit(1)
        