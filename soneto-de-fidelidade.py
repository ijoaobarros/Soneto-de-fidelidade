import time
from os import system

def imprimir_texto(verso, tempo_intervalo):
    for caracter in verso:
        print(caracter, end='', flush=True)
        time.sleep(tempo_intervalo)
    print('')

soneto = [
    ['De tudo ao meu amor serei atento', 0.08],
    ['Antes, e com tal zelo, e sempre, e tanto,', 0.06],
    ['Que mesmo em face do maior encanto,', 0.05],
    ['Dele se encante mais meu pensamento.', 0.08],
    [' ', 0.5],
    ['Quero vivê-lo em cada vão momento', 0.05],
    ['E em seu louvor hei de espalhar meu canto', 0.06],
    ['E rir meu riso e derramar meu pranto', 0.05],
    ['Ao seu pesar ou seu contentamento.', 0.08],
    [' ', 0.3],
    ['E assim, quando mais tarde me procure,', 0.04],
    ['Quem sabe a morte, angústia de quem vive,', 0.04],
    ['Quem sabe a solidão, fim de quem ama,', 0.05],
    [' ', 0.8],
    ['Eu possa me dizer do amor (que tive):,', 0.07],
    ['Que não seja imortal, posto que é chama,', 0.07],
    ['Mas que seja infinito enquanto dure.', 0.06]
]

system('cls')
for verso in soneto:
    imprimir_texto(*verso)
    time.sleep(0.4)
time.sleep(6)