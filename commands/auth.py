import hashlib
from core.repo import require_repo
from core.storage import read_json, write_json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    require_repo()
    auth = read_json("auth.json")

    username = input("Usuario: ").strip()

    if any (u ["username"] == username for u in auth ["users"]):
        print (f"Erro: usuario {username} ja existe")
        return
    
    password = input("Senha: ").strip()
    confirm = input("Confirme a senha: ").strip()

    if password != confirm:
        print("Erro: as senhas nao coincidem")
        return
    
    auth ["users"].append(
        {
        "username" : username,
        "password" : hash_password(password)
        })
    write_json("auth.json", auth)
    print(f"Usuario {username} registrado com sucesso")

def login():
    require_repo()
    auth = read_json("auth.json")

    username = input("Usuario: ").strip()
    password = input("Senha: ").strip()

    user = next((u for u in auth ["users"] if u ["username"] == username), None)
    if not user or user ["password"] != hash_password(password):
        print("Erro: usuario ou senha invalidos")
        return
    
    auth ["logged_in"] = username
    write_json ("auth.json", auth)
    print(f"Usuario {username} logado com sucesso")

def logout():
    require_repo()
    auth = read_json("auth.json")

    if not auth ["logged_in"]:
        print("Erro: nenhum usuario esta logado")
        return
    
    usuario = auth ["logged_in"]
    auth ["logged_in"] = None
    write_json("auth.json", auth)
    print(f"Usuario {usuario} deslogado com sucesso")
