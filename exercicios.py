# print(" Python na Escola de Programação da Alura.")

# nome = "jorge"
# idade = "15"
# print(f" Meu nome é {nome} e tenho {idade} anos")

# print("""
#       A
#       L 
#       U
#       R
#       A""")

# # print('A','L','U','R','A',sep='\n')


# pi_arredondado = 3.14159

# print(F"O valor arredondado de pi é: {pi_arredondado}")

# pi = 3.14159

# # Abordagem de f-string
# print(f'O valor arredondado de pi é: {pi:.2f}')

# # Abordagem de .format()
# print('O valor arredondado de pi é: {:.2f}'.format(pi))

# # Utilizando a função round()
# print('O valor arredondado de pi é:', round(pi, 2))


# #Listas e Tuplas
# # Criando uma lista de compras
# lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# # Adicionando um item à lista
# lista_de_compras.append("Ovos")

# # Removendo um item da lista
# lista_de_compras.remove("Banana")

# # Exibindo a lista
# print("Lista de Compras:")
# for item in lista_de_compras:
#     print("- " + item)


# # Definindo uma tupla de coordenadas geográficas
# coordenadas_gps = (40.7128, -74.0060)

# # Exibindo as coordenadas
# print("Coordenadas GPS:")
# print("Latitude:", coordenadas_gps[0])
# print("Longitude:", coordenadas_gps[1])


# #Loops
# #For
# numero = -1
# for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
#     numero = int(input("Digite um número positivo: "))
#     if numero > 0:
#         break

# print("Você digitou:", numero)


# #While
# numero = -1
# while numero <= 0:
#     numero = int(input("Digite um número positivo: "))

# print("Você digitou:", numero)

# #Try/Except
# encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
# try:
#     for encomenda in encomendas:
#         print(int(encomenda))
# except ValueError:
#     print("Uma das entradas não é um número válido.")

# #dicinarios
# restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False}, {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False}]


# livro = {
#     'titulo': 'Aprendendo Python',
#     'autor': 'Fabrício Silva',
#     'ISBN': '12345',
#     'preco': 59.90,
#     'em_estoque': True
# }
# livro['preco'] = 69.90
# #Esta é a maneira correta de atualizar o valor associado à chave 'preco' em um dicionário em Python.


# credenciais_clientes = {
#     'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
#     'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
#     'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
# }


# alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] == 'inactive' else 'Sem alerta'
#Este código verifica corretamente o status do usuário 'bob456' utilizando um operador ternário, onde se o status for 'inactive', a variável alerta recebe 'Enviar alerta!', caso contrário, recebe 'Sem alerta'.

# Exercícios

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = [{'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'},
           {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}]


# 2 - Utilizando o dicionário criado no item 1:

#     Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

pessoas[0]['idade'] = 31
print(pessoas[0]['idade'])  # Isso irá imprimir 31, que é a nova idade de João.

#     Adicione um campo de profissão para essa pessoa;
pessoas[0]['profissao'] = 'Engenheiro'
print(pessoas[0]['profissao'])  # Isso irá imprimir 'Engenheiro',s
#     Remova um item do dicionário.
del pessoas[0]['cidade']
print(pessoas[0])  # Isso irá imprimir o dicionário atualizado de João,

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = [{1: 1}, {2: 4}, {3: 9}, {4: 16}, {5: 25}]
print(quadrados)  # Isso irá imprimir a lista de dicionários com os números e seus quadrados.
# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
if 'nome' in pessoas[0]:
    print("A chave 'nome' existe no dicionário de João.")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "Python é uma linguagem de programação. Python é fácil de aprender."
frequencia_palavras = {}
for palavra in frase.split():
    palavra = palavra.strip('.,').lower()  # Remove pontuação e converte para minúsculas
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1
print(frequencia_palavras)  # Isso irá imprimir o dicionário com a frequência de cada palavra.