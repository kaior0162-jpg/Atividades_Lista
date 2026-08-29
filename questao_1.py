   #questao sobre substituição

fun = ["kaio", "matheus", "samuel", "ivo", "thiago"]

nfun = input("digite o nome do novo funcionario: ")
lgar = int(input("qual o numero do funcionario que sera substituido? "))


fun[lgar-1] = nfun

print(fun)
print("Escala atual!")

print(fun)