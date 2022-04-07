notaTotal=0
numeroDeNotas=int(input("Numero de Notas = "))
for i in range(numeroDeNotas):
    entradaNotas=float(input("Nota = "))
    notaTotal+=entradaNotas

print("Média final = ", notaTotal/numeroDeNotas)