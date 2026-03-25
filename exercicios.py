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
