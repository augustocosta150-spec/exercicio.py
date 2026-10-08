senha = "Senha123"

while True:
    entrada = input("Digite a senha: ")
    if entrada == senha:
        print("Acesso permitido!!")
        break
    else:
        print("Senha incorreta! Tente novamente.")