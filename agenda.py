# import modules
from easygui import *
from peewee import *
import sys


# GUI
# crear menu
def menu():
    msg = 'Select an option.'
    title = 'Menu'
    choices = ["Search","Modify"]
    choice = choicebox(msg,title,choices)
# ventana busqueda
def search():
    msg = "Enter the information"
    title = "Search"
    fieldNames = ["Name","Telephone","E-mail"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)
# ventana registro
def registry():
    msg = "Enter the information"
    title = "Registry"
    fieldNames = ["Name","Telephone","E-mail"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)
# ventana borrado
# ventana modificar
def modify():
    msg = "Modify the information"
    title = "modify"
    fieldNames = ["Name","Telephone","E-mail"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)
# ventana confirmación
def confirmation():
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        alert_confirm()  # user chose Continue
    else:  # user chose Cancel
        sys.exit(0)
# ventana aviso de no datos
def no_data():
    msg = "Sorry, but I can not found any information."
    title="Alert no data"
    msgbox(msg,title)
    
# ventana de aviso de confirmación
def alert_confirm():
    msg = "Step is done."
    title="Comfirm"
    msgbox(msg,title)
# ventana informacion programa
def info():
    msg = "Information of the program."
    body = """
            Author: Marco Baturan.
            Program: Tool under EasyGui and
            Peewe for store information
            of contactcs.
          """
    title="Info"
    textbox(msg,title,body)
    
    
# FUNCIONES
# crear registro
# crear modificacion
# crear borrado
# crear excepcion de error


# INICIO
menu()

