lista = []
par = []
impar = []

for n in range(101):
    lista.append(n)

for n in lista:
    if n % 2 == 0:
        par.append(lista[n])
    else:
        impar.append(lista[n])

print(par)
print(impar)

# Retirar os números 33, 61 e 82
impar.pop(impar.index(33))
impar.pop(impar.index(61))
par.pop(par.index(82))

print(impar)
print(par)