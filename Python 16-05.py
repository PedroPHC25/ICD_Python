"""
def maior_e_menor_valores(dicionario):
    valores = list(dicionario.values())
    maior_valor = valores[0]
    menor_valor = valores[0]
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
        elif valor < menor_valor:
            menor_valor = valor
    return maior_valor, menor_valor

num = {"a": -9, "b": 7, "c": 7, "d": 8, "e": 5}

print(maior_e_menor_valores(num))
"""
"""
def quadrados(n):
    dicionario = {}
    for i in range(1, n + 1):
        dicionario[i] = i**2
    return dicionario

print(quadrados(5))
"""
"""
def remove_duplicatas(dicionario):
    dicionario_novo = {}
    for chave, valor in dicionario.items():
        if valor not in dicionario_novo.values():
            dicionario_novo[chave] = valor
    return dicionario_novo

dicionario = {1:1, 2:2, 3:1, 4:2, 5:3}

print(remove_duplicatas(dicionario))
"""

def adicionar_pedido(numero_do_pedido, fila_de_pedidos):
    fila_de_pedidos.append(numero_do_pedido)
    print(f"Pedido {numero_do_pedido} adicionado")

def preparar_pedido(fila_de_pedidos):
    print(f"Pedido {fila_de_pedidos[0]} está pronto")
    fila_de_pedidos.remove(fila_de_pedidos[0])

def listar_pedidos_em_preparo(fila_de_pedidos):
    for pedido in fila_de_pedidos:
        print(f"Preparando {pedido}")

def verificar_pedido(numero_do_pedido, fila_de_pedidos):
    if fila_de_pedidos.count(numero_do_pedido) < 1:
        print("Pedido não existente")
    else:
        print("Seu pedido é o número", fila_de_pedidos.index(numero_do_pedido) + 1, "da fila.")


pedidos_em_preparo = []

print("Digite 1 para listar pedidos.")
print("Digite 2 para adicionar um pedido.")
print("Digite 3 para preparar um pedido.")
print("Digite 4 para verificar um pedido.")
print("Digite 5 para encerrar o programa.")

while True:
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        listar_pedidos_em_preparo(pedidos_em_preparo)
    elif opcao == 2:
        pedido = int(input("Digite o número do pedido: "))
        adicionar_pedido(pedido, pedidos_em_preparo)
    elif opcao == 3:
        preparar_pedido(pedidos_em_preparo)
    elif opcao == 4:
        pedido = int(input("Digite o número do pedido: "))
        verificar_pedido(pedido, pedidos_em_preparo)
    elif opcao == 5:
        break
    else:
        print("Opção incorreta. Digite outra vez.")

"""
adicionar_pedido(1, pedidos_em_preparo)
adicionar_pedido(2, pedidos_em_preparo)
adicionar_pedido(3, pedidos_em_preparo)

listar_pedidos_em_preparo(pedidos_em_preparo)

verificar_pedido(2, pedidos_em_preparo)
verificar_pedido(3, pedidos_em_preparo)

preparar_pedido(pedidos_em_preparo)
preparar_pedido(pedidos_em_preparo)

verificar_pedido(2, pedidos_em_preparo)
verificar_pedido(3, pedidos_em_preparo)

listar_pedidos_em_preparo(pedidos_em_preparo)
"""