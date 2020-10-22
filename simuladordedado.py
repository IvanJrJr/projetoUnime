from random import randint

while True:
    i = int(input("Digite 1 para gerar um número\nDigite 0 para sair\n"))
    if i == 1:
        print(randint(1, 6))
    elif i == 0:
        break
    else:
        print("Comando inválido!")

