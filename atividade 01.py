
#As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
#estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
#a) len(), que recebe uma lista e retorna número de itens;
#b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
#c) min(),que recebe uma lista e retorna o menor valor
#d) max(), que recebe uma lista retorna o maior valor
#e) sum(), que recebe uma lista retorna a soma dos valores
#Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a
#leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o
#resultado encontrado.
#Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(),
#minimo(), maximo(), soma().


def cria_lista():
    lista = []
    while True:
        numeros = int(input())
        if numeros == 0:
            break
        lista.append(numeros)

    return lista


def comprimento(lista):
    comprimento = 0

    for _ in lista:
        comprimento += 1
    return comprimento


def inverter(lista, comprimento):
    lista_invertida = []
    incremento = comprimento
    
    for i in range(comprimento):
        lista_invertida.append(lista[incremento - 1])
        incremento -= 1
    return lista_invertida


def minimo(lista):
    menor = 0
    for i in lista:
        if i < menor:
            menor = i
        if menor == 0:
            menor = i
    return menor


def maximo(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior


def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


def main():
    lista = cria_lista()
    tamanho = comprimento(lista)
    lista_invertida = inverter(lista, tamanho)
    min = minimo(lista)
    max = maximo(lista)
    somadas = soma(lista)

    print(f'{lista}\n{tamanho}\n{lista_invertida}\n{min}\n{max}\n{somadas}')


if __name__ == "__main__":
    main()