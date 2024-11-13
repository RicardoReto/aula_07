
while True:
    try:
        x = int(input("Por favor, digite um número inteiro: "))
        if x < 0:
            x = 0
            print("O número é menor que zero")
        elif x == 0:
            print("O valor é igual a zero")
        elif x == 1:
            print("O valor é igual a 1")
        else:
            print("O valor é maior que 1")
        break
    except:
        print("Você digitou um valor inválido!")