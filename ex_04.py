"""
palavras = ["carro", "hipopótamo", "escalafobético", "inconstitucionalicimamente"]

for p in palavras:
    print(f"A palavra {p} contém " + str(len(p)) + " letras")
"""

palavras = []
qtd = 4

while qtd > 0:
    palavra = input("Digite um palavra: ")
    palavras.append(palavra)
    qtd -= 1

for p in palavras:
    print(f"A palavra {p} contém " + str(len(p)) + " letras")