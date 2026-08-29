notas = []
soma = 0

nome = input("Digite o nome do aluno: ")

for i in range(4):
    n = float(input(f"Digite a {i+1}° nota: "))

    notas.append(n)

soma = soma + n

media = soma / 4

print("\n boletin da(o) ", nome)
print("---------------------------")
for i in notas:
    print(i)

print("------------------------------------------")
print(f"  A soma das Notas do {nome} é : {soma:.1f}")
print(f"Essa é a media do(a) {nome}: {media:.1f}")