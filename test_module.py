import agenda
import peewee
import easygui
import sys


def test_import_easygui():
    # Assert the existence of Easy GUI.
    assert easygui
    
def test_import_peewee():
    # Sssert the existence of Peewee
    assert peewee
    
def test_import_sys():
    # Assert the existence of Sy.
    assert sys
    
def test_import_agenda():
    # Assert the existence of agenda.
    assert agenda

def test_window_menu():
    agenda.menu()
    
def test_window_confirm():
    agenda.confirmation()
    
def test_window_no_data():
    agenda.no_data()

def test_window_search():
    agenda.search()

def test_window_registry():
    agenda.registry()
    
def test_window_alert_confirm():
    agenda.alert_confirm()

def test_window_modify():
    agenda.modify()

# ventana informacion programa
def test_info():
    agenda.info()
# FUNCIONES
# crear registro
# crear modificacion
# crear borrado
# crear excepcion de error


# INICIO
    