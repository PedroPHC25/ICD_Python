"""
#print('Eu', 'adoro', 'a', 'EMAp', sep = 'p', end = 'p')
#print('Eu', 'adoro', 'a', 'EMAp', sep = 'p')


altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilogramas: '))

# Teste

#print(altura)
#print(peso)

imc = peso/altura**2

print("Seu IMC é: ", imc, ".", sep = "")

if imc < 18.5:
    print("Abaixo do peso normal.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Excesso de peso.")
elif imc < 35:
    print("Obesidade classe 1.")
elif imc < 40:
    print("Obesidade classe 2.")
else:
    print("Obesidade classe 3.")
    

#print(altura>1.9)


if altura > 1.9:
    print('Caramba! Você é muito alto(a)!')
else:
    print("Você não é alto(a)...")
    
print('Fim do programa.')
"""
"""
número = 1

while número <= 10:
    print(número)
    número += 1
    
mensagem = ""

while mensagem != "Sair":
    mensagem = input("Digite Sair para sair: ")
    print("Você não saiu...")
"""

soma_notas = 0
total_notas = 0
nota = 0

nota = float(input("Digite a nota ou -1 para sair: "))

while nota != -1:
    soma_notas += nota
    total_notas += 1
    nota = float(input("Digite a nota ou -1 para sair: "))
    
if total_notas > 0:
    print("A média da turma é: ", soma_notas/total_notas)
else:
    print("Nenhuma nota foi inserida.")