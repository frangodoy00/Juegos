import random    

def ElegirTemaYPalabra(palabras):
    tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
    pal =palabras[tema][random.randrange(len(palabras[tema]))]
    return pal

def Jugar(pal,pal_separada,ahorcado):
    LetrasAdivinadas=0
    PartesDelCuerpo=0
    sigue=True
    while sigue:
        letra=input('Ingrese una letra').lower()
        if letra in pal:
            for pos in range(len(pal)):
                if pal[pos]==letra:
                    pal_separada[pos]=letra
                    LetrasAdivinadas= LetrasAdivinadas + 1
            pal_imprime=''
            for y in pal_separada:
                pal_imprime=pal_imprime + y[0]
            print(pal_imprime)
            if LetrasAdivinadas== len(pal):
                print('Ganaste')
                sigue=False
        else:
            PartesDelCuerpo = PartesDelCuerpo + 1
            for x in range(PartesDelCuerpo):
                print(ahorcado[x])
            if PartesDelCuerpo ==3:
                print('Perdiste,la palabra era ',pal)
                sigue=False
palabras = {1:['gato', 'perro','leon','loro'], 2:['rojo','azul','verde','amarillo'], 3:['ensalada','arroz','pasta','hamburguesa']}
ahorcado = [' O ', '/|\\','/ \\']
pal_separada=[]
pal = ElegirTemaYPalabra(palabras)
for i in pal:
    pal_separada.append(['_ '])
print('- '*len(pal))
Jugar(pal,pal_separada,ahorcado)