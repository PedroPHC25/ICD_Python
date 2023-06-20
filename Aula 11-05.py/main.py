# Divisão do programa em módulos
# A2: Plotly ou Bokeh

dicionario = {1: "EMAp", 2: "CDD", 3: "MAp"}
# print(dicionario)

dicionario_muito_louco = {"Escola": "EMAp", 1: [1, 2, 3, 4, 5]}
# print(dicionario_muito_louco)

dicionario_vazio = {}
# print(dicionario_vazio)

dicionario_aninhado = {"Universidade": "FGV", "Escolas": {1: "EMAp", 2: "EBAPE", 3: "DIREITO RIO"}}
# print(dicionario_aninhado)

dicionario_criado_por_funcao = dict([(1, "EMAp"), (2, "EBAPE")])
# print(dicionario_criado_por_funcao)

# print(dicionario_aninhado["Escolas"][3])

dicionario[2] = "CdD"
dicionario[4] = "CM"
# print(dicionario)

# print(1 in dicionario)
# print("EMAp" in dicionario)

dados_para_atualizacao = {"nacionalidade": "brasileiro", "religião": "paganismo nórdico"}
dicionario_vazio.update(dados_para_atualizacao)
# print(dicionario_vazio)

mais_dados_para_atualizacao = {"nacionalidade": "português", "escolaridade": "pequeno medíocre"}
dicionario_vazio.update(mais_dados_para_atualizacao)
# print(dicionario_vazio)

# print(dicionario.get(5))

dicionario.clear()
# print(dicionario)

chaves = dicionario_vazio.keys()
chaves = list(chaves)
# print(chaves)
# print(type(chaves))

valores = dicionario_vazio.values()
# valores = list(valores)
# print(valores)
# print(type(valores))

# for cada_valor in valores:
#     print(cada_valor)

# for cada_valor in dicionario_vazio.values():
#     print(cada_valor)

# for cada_valor in dicionario_vazio.keys():
#     print(cada_valor)

dicionario_novo = {1: 7, 2: 42, 3: 666}
# print(max(dicionario_novo.values()))
# print(min(dicionario_novo.values()))

for cada_valor in dicionario_novo.values():
    maior_valor = cada_valor
    if cada_valor > maior_valor:
        maior_valor = cada_valor

print(maior_valor)