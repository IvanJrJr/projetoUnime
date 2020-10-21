import random
import string

while True:
    n = int(input('Quantidade de caracteres: '))
    if n < 3 or n > 30:
        continue
        print('O número deve ser maior que 3 e nem maior que 30')
    else:
        break


def switch():
    print('Digite 1 para númerico;\nDigite 2 para alfanumérica;\nDigite 3 para senha forte;')
    # Seletor de opções.

    opcao = int(input(''))

    def numerico():
        # função para senhas com apenas números
        print('Sua senha é:')
        for i in range(n):
            print(random.randint(0, 9), end='')

    def alfanumerico():
        print('Sua senha é:')
        letras_numeros = string.ascii_letters + string.digits
        for i in range(n):
            print(random.choice(letras_numeros), end='')  # Letras e números

    def senha_forte():
        inteiro = n
        inteiro = int(inteiro)
        print('Sua senha é:')
        for i in range(int(inteiro/inteiro)):
            print(random.choice(string.punctuation), end='')  # caracteres especiais
        for i in range(inteiro-1):
            print(random.choice(string.ascii_letters + string.digits), end='') # Letras e números

    def erro():
        print('Opção invalida. Tente novamente!')  # Caso o usuário selecione um número diferente de 1, 2, 3.

    # Mapa para o switch()
    mapa = {
        1: numerico,
        2: alfanumerico,
        3: senha_forte,
    }
    mapa.get(opcao, erro)()


switch()  # chamando o método.
