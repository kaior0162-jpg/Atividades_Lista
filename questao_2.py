lista = []

for i in range(10):
    n = int(input(f"Digite o {i+1}° numero: "))
    lista.append(n)

print("Lista atual: ", lista)
lista.reverse()
print("Nova lista: ", lista)
