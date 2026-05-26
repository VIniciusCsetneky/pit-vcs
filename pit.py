import sys
from commands.init import init
from commands.auth import register, login, logout

def main():
    if len(sys.argv) < 2:
        print("Uso: pit <comando>")
        print("Comandos disponíveis: init, register, login, logout")
        return

    comando = sys.argv[1]

    if comando == "init":
        init()
    elif comando == "register":
        register()
    elif comando == "login":
        login()
    elif comando == "logout":
        logout()
    else:
        print(f"Comando '{comando}' não reconhecido.")

if __name__ == "__main__":
    main()