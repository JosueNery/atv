import pandas as pd

from models import Jogos


def listaDes(jogos):
    lista_desordenada = []
    tamanho = len(jogos)
    i = 0
    while i < tamanho:
        lista_desordenada.append(Jogos(
            jogos.loc[i, 'jogo'], jogos.loc[i, 'categoria'], jogos.loc[i, 'avaliacao']))
        i += 1
    return lista_desordenada


def selectionSort(lista, s):

    for step in range(len(lista)):
        min_idx = step

        for i in range(step + 1, len(lista)):
            if eval(s):
                min_idx = i

        (lista[step], lista[min_idx]) = (lista[min_idx], lista[step])


def printLista(lista):
    for i in range(len(lista)):
        print(lista[i])


if __name__ == "__main__":
    jogoDes = pd.read_csv("src/JogosDesordenados.csv",
                          header=None, names=['jogo', 'categoria', 'avaliacao'])

    lista = listaDes(jogoDes)
    selectionSort(lista, 'lista[i].categoria < lista[min_idx].categoria')
    selectionSort(
        lista, '(lista[i].avaliacao > lista[min_idx].avaliacao) and (lista[i].categoria == lista[min_idx].categoria)')
    selectionSort(
        lista, '(lista[i].avaliacao == lista[min_idx].avaliacao) and (lista[i].categoria == lista[min_idx].categoria) and (lista[i].jogo < lista[min_idx].jogo)')

    lista = pd.DataFrame(lista)
    lista.to_csv('src/JogosOrdenados.csv')
    print(lista)
