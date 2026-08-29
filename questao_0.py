vetor = []

for i in range(5):
    n = int(input(f"igite o {i+1}° numero: "))
    vetor.append(n)

    print("os numeros digitados foram: ")
    
    for i in vetor:
        print(i)
