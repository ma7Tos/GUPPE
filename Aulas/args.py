"""
Entendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo.

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde já lembre-se que
tuplas são imutáveis.

# Exemplos menos utilizado (Não otimizado)

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4,6,9))

print(soma_todos_numeros(4 ,6))

print(soma_todos_numeros(4, 6, 9, 5))

# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Jairo', 'JJoestar@gmail.com'))
print(soma_todos_numeros('Jairo', 'JJoestar@gmail.com', 1))
print(soma_todos_numeros('Jairo', 'JJoestar@gmail.com', 2, 3))
print(soma_todos_numeros('Jairo', 'JJoestar@gmail.com', 2, 3, 4))
print(soma_todos_numeros('Jairo', 'JJoestar@gmail.com', 3, 4, 5, 6))

print(soma_todos_numeros('Jairo', 'JJoestar@gmail.com', 23.4, 12.5))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza de quem você é...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(1, 'University', 3.145)
"""

def soma_todos_numeros(*args):
    return sum(args)

# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6,))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros))

#OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
#Desta forma, ele saberá que precisará antes desempacotar estes dados.


