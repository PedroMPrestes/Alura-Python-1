print(" Python na Escola de Programação da Alura.")

nome = "jorge"
idade = "15"
print(f" Meu nome é {nome} e tenho {idade} anos")

print("""
      A
      L 
      U
      R
      A""")

# print('A','L','U','R','A',sep='\n')


pi_arredondado = 3.14159

print(F"O valor arredondado de pi é: {pi_arredondado}")

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))


#Listas e Tuplas
# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)


# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])


#Loops
#For
numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)


#While
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)

#Try/Except
encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")

#dicinarios
restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False}, {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False}]
