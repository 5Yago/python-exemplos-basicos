#importação de biblioteca getpass
import getpass as gtp

usuario = input("Nome do usuário: ")
senha = gtp.getpass("Digite sua senha: ")

#verificação 

if len(senha) >= 6:
    print(f"Usuario cadastrado com sucesso")
else:
    print("Senha deve ter pelo menos 6 caracteres!!")
