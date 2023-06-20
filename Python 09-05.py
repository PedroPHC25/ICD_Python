from math import sqrt as raiz
# import sys

def saudacoes():
    print("Olá, aluno. Eu adoro a EMAp!")
    
def saudacoes_com_argumento(nome_do_usuario):
    print(f"Olá, {nome_do_usuario.title()}. Eu adoro a EMAp!")
    
def saudacoes_com_argumentos_posicionais(nome_do_usuario, escola_do_usuario):
    print(f"Olá, {nome_do_usuario.title()}. Eu adoro a {escola_do_usuario}!")
    
def saudacoes_com_argumento_padrao(nome_do_usuario = "amiguinho", escola_do_usuario = "EMAp"):
    print(f"Olá, {nome_do_usuario.title()}. Eu adoro a {escola_do_usuario}!")
    
def nome_formatado(nome_pessoal, nome_de_familia):
    nome_completo = f"{nome_pessoal} {nome_de_familia}".title()
    return nome_completo

def alunos_bons(escola, *alunos):
    print(escola)
    for cada_aluno in alunos:
        print(cada_aluno, end = "    ")
        
def alunos_bons2(escola, **alunos):
    print(escola)
    for cada_aluno in alunos:
        print(cada_aluno, end = "    ")
        
    
# Main ou driver code
    
'''
saudacoes()
saudacoes_com_argumento("frango")
saudacoes_com_argumento("floquinho de neve")
saudacoes_com_argumentos_posicionais("floquinho de neve", "EMAp")
saudacoes_com_argumentos_posicionais(escola_do_usuario = "EMAp", nome_do_usuario = "floquinho de neve")
saudacoes_com_argumento_padrao()

retorno = nome_formatado("pedro hENRique", "coterli")
print(retorno)

print(saudacoes())

saudacoes_com_argumentos_posicionais(nome_formatado("Pedro", "Coterli"), "EMAp")

alunos_bons("EMAp", "Mariana Rocha", "Matheus Carvalho", "Guilherme Buss")

saudacoes()

print(sys.path)
'''

print(raiz(9))