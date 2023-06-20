"""
nota = 0
soma_notas = 0
num_notas = 0

nota = float(input("Insira a nota ou -1 para sair:"))

while nota != -1:
    soma_notas += nota
    num_notas += 1
    nota = float(input("Insira a nota ou -1 para sair:"))

if num_notas != 0:
    print("A média é: ", soma_notas/num_notas)
else:
    print("Nenhuma nota inserida.")

lista = [1, 2, 3]
tupla = (1, 2, 3)

print(type(lista))
print(type(tupla))

lista = []
lista2 = [1, 1.1, "EMAp", [1.2, 1.8, "FGV"], ["CD"]] # Lista aninhada

print(lista2)

lista = ["E", "M", "A", "p"]

# print(lista[0])

lista3 = ["E", "M", "A", "p", [2, 0, 0, 3]]

print(lista3[4][0]) # Indexando listas aninhadas

print(lista3[-2]) # Contagem de trás pra frente


lista = ["E", "M", "A", "p"]

print(lista[1:4])
print(lista[1:])
print(lista[:3])
print(lista[-3:])
print(lista[1:])]


lista = ["E", "M", "A", "p"]

# del lista[0] # Isso altera os índices da lista
# del lista[1:3]

# print(lista)

minha_lista = ["A", "N", "A", "J", "Ú", "L", "I", "A"]

minha_lista.remove("A")

print(minha_lista)

minha_lista.remove("A")

print(minha_lista)

minha_lista.clear()

print(minha_lista)


impares = [2, 4, 6, 8]
impares[0] = 1
impares[1:4] = [3, 5, 7]

print(impares)

impares.append(9)

print(impares)

impares.extend([11, 13, 15]) # Insere mais de um elemento

print(impares)

impares_extra = [17, 19, 21]

print(impares + impares_extra)
"""

minha_lista = ["A", "N", "A", "J", "Ú", "L", "I", "A"]

# print("A" in minha_lista)
# print("B" in minha_lista)
# print("B" not in minha_lista)

filosofos = ["Marco Aurélio", "Zenão de Cítio", "Sêneca", "Epiteto", "Dilma Roussef"]

"""
if "Sêneca" in filosofos:
    print(f"{filosofos[2]} é demais!")

if "Dilma Roussef" in filosofos:
    print(f"{filosofos[2]} é demais!")
"""

indice = 0

while indice < len(filosofos):
    print(filosofos[indice])
    indice += 1

for i in filosofos:
    print(i)


































