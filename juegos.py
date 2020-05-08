import json
import PySimpleGUI as sg

archivo=open('Jugadores.txt','a')

sg.theme('Topanga')

layout = [
    [sg.Text('Ingrese su nombre')],
    [sg.Text('Nombre', size=(15, 1)), sg.InputText()],
    [sg.Text('A que juego desea jugar?')],
    [sg.Button('AHORCADO'), sg.Button('TATETI'), sg.Button('ADIVINADOR')]
]

window = sg.Window('MENU', layout)
event, values = window.read()
window.close()
print(event, values[0])
datos=[{'Nombre': values[0], 'Juego': event}]
json.dump(datos, archivo)

if event=='AHORCADO':
    import Ahorcado
if event=='TATETI':
    import TaTeTi
if event=='ADIVINADOR':
    import AdivinaNum   

archivo.close()     

# Utilizo un archivo para almacenar la informacion de los jugadores, ya que
# los archivos se guardan en el disco duro y no se pierde la informacion del mismo.
# El formato que utilice es el json, porque es una manera mas sencilla de almacenar
# los datos, antes que hacerlo con una cadena.