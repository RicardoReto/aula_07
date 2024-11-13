while True:
    try:
        x = float(input("Por favor, digite uma temperatura: "))
        if x < 15.0:
            print("Está frio")
        elif x > 15.0 and x < 21.0:
            print("Está fresco")
        elif x > 21.0 and x < 27.0:
            print("Está agradável")
        
        elif x > 27.0 and x < 33.0:
            print("Está quente")
        else:
            print("Está muuito quente")
        break
    except:
        print("Você digitou algo errado!")