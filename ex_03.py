import re

while True:
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        email = input("Digite um e-mail válido: ")
        valid_email = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

        if not isinstance(nome, str):
            print("Você digitou algo errado como seu nome")
        elif not isinstance(idade, int):
            print("Você digitou algo errado como sua idade")
        elif not isinstance(email, str):
            print("Você digitou algo errado como seu e-mail")
        
        if idade < 18 or idade > 65:
            print("Idade deve estar entre 18 e 65 anos")
        if not valid_email:
            print("Este e-mail não é válido")
        else:
            print("Dados cadastrados com êxito!")

        break
    except:
        print("Dado(s) digitado(s) incorretamente")