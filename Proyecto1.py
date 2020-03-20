import sys
import os

from io import open
from datetime import datetime

class Menu:
    def __init__(self):
       
        self.opcion_menu = {
                "1" : self.menu_afd,
                "2" : self.menu_gramatica,
                "3" : self.menu_cadenas,
                "4" : self.menu_reportes,
                "5" : self.menu_cargar,
                "6" : self.Save,
                "7" : self.Quit
        }
        self.opcion_afd = {
            "1" : self.ingresar_estados,
            "2" : self.ingresar_alfabeto,
            "3" : self.estado_inicial,
            "4" : self.estado_aceptacion,
            "5" : self.transiciones,
            "6" : self.ayuda,
            "7" : self.back
        }      
        self.opcion_gramatica = {
            "1" : self.NT,
            "2" : self.T,
            "3" : self.NT_inicial,
            "4" : self.producciones,
            "5" : self.transformada,
            "6" : self.ayuda,
            "7" : self.back           
        }
        self.opcion_cadenas = {
            "1" : self.validar,
            "2" : self.ruta,
            "3" : self.expandir,
            "4" : self.ayuda,
            "5" : self.back           
        }     
        self.opcion_cargar = {
            "1" : self.cargarAFD,
            "2" : self.cargarGra,
            "3" : self.back           
        }  
        self.opcion_reportes = {
            "1" : self.detalle,
            "2" : self.generar,
            "3" : self.ayuda,
            "4" : self.back           
        }  
    def inicio(self):
        print("""
        Universidad de San Carlos de Guatemala
        Lenguajes Formales y de Programación
        Sección A+
        José Andres Rodas Arrecis
        201504220
        \n""")
        input("Presione enter para continuar: ") 
        os.system ("cls")
        self.run() 

    def menu_principal(self):
        print("""
                *************** Menu Principal ***************

                1 Crear AFD
                2 Crear Gramática
                3 Evaluar Cadenas
                4 Reportes
                5 Cargar Archivo de Entrada
                6 Guardar Archivos
                7 Salir
                """)
    def menu_afd(self):
        os.system ("cls") 
        while True:

            print("""
                *************** Menu de AFD ***************

                1 Ingresar Estados
                2 Ingresar Alfabeto
                3 Estado Inicial
                4 Estado de Aceptación
                5 Transiciones
                6 Ayuda

                7 Volver
                """)
            eleccion = input("Escribe una opción: ")
            accion = self.opcion_afd.get(eleccion)
            if accion:
                accion()
                #break}
            else:
                print("{0} no es una opción".format(eleccion))
    def menu_gramatica(self):
        os.system ("cls") 
        while True:
            print("""
                *************** Menu Gramática ***************

                1 Ingresar NT
                2 Ingresar T
                3 NT Inicial
                4 Producciones
                5 Mostrar Gramática Transformada
                6 Ayuda

                7 Volver

                """)
            eleccion = input("Escribe una opción: ")
            accion = self.opcion_gramatica.get(eleccion)
            if accion:
                accion()
                #break
            else:
                print("{0} no es una opción".format(eleccion))
    def menu_cadenas(self):
        os.system ("cls") 
        while True:
            print("""
                *************** Menu Evaluar Cadenas ***************

                1 Solo Validar
                2 Ruta AFD
                3 Expandir con Gramática
                4 Ayuda

                5 Volver

                """)
            eleccion = input("Escribe una opción: ")
            accion = self.opcion_cadenas.get(eleccion)
            if accion:
                accion()
                #break
            else:
                print("{0} no es una opción".format(eleccion))
    def menu_cargar(self):
        os.system ("cls") 
        while True:
            print("""
                *************** Menu Cargar Archivos ***************

                1 AFD
                2 Gramática

                3 Volver

                """)
            eleccion = input("Escribe una opción: ")
            accion = self.opcion_cargar.get(eleccion)
            if accion:
                accion()
                #break
            else:
                print("{0} no es una opción".format(eleccion))  
    def menu_reportes(self):
        os.system ("cls") 
        while True:
            print("""
                *************** Menu Reportes ***************

                1 Ver Detalle
                2 Generar Reporte
                3 Ayuda

                4 Volver

                """)
            eleccion = input("Escribe una opción: ")
            accion = self.opcion_reportes.get(eleccion)
            if accion:
                accion()
                #break
            else:
                print("{0} no es una opción".format(eleccion))
    def ayuda(self):
        print("ayuda")
    def back(self):
        os.system ("cls")
        self.run()

    def ingresar_estados(self):
        AFD().ingresar_estados()
    def ingresar_alfabeto(self):
        AFD().ingresar_alfabeto()
    def estado_inicial(self):
        AFD().estado_inicial()
    def estado_aceptacion(self):
        AFD().estado_aceptacion()
    def transiciones(self):
        AFD().transiciones() 

    def NT(self):
        Gramatica().NT()
    def T(self):
        Gramatica().T()
    def NT_inicial(self):
        Gramatica().NT_inicial()
    def producciones(self):
        Gramatica().producciones()
    def transformada(self):
        Gramatica().transformada() 

    def validar(self):
        Cadenas().validar()
    def ruta(self):
        Cadenas().ruta()
    def expandir(self):
        Cadenas().expandir()

    def cargarAFD(self):
        Cargar().cargarAFD()
    def cargarGra(self):
        Cargar().cargarGra()

    def detalle(self):
        Reportes().detalle()
    def generar(self):
        Reportes().generar() 

    def Save(self):
        Guardar().save()

    def run(self): 
        while True:
            self.menu_principal()
            eleccion = input("Escribe una opción: ")
            accion = self.opcion_menu.get(eleccion)
            if accion:
                accion()
                break
            else:
                print("{0} no es una opción".format(eleccion))

    def Quit(self):
        print("Hasta la próxima")
        sys.exit(0)


class AFD:
    def __init__(self):
        print("Clase AFD")
    def ingresar_estados(self):
        print("ingresar estados")
    def ingresar_alfabeto(self):
        print("ingresar alfabeto")
    def estado_inicial(self):
        print("estado inicial")
    def estado_aceptacion(self):
        print("estado aceptacion")
    def transiciones(self):
        print("transiciones")
    
class Gramatica:
    def __init__(self):
        print("Clase Gramatica")
    def NT(self):
        print("NT")
    def T(self):
        print("T")
    def NT_inicial(self):
        print("NT inicial")
    def producciones(self):
        print("Producciones")
    def transformada(self):
        print("transformada")

class Cadenas:
    def __init__(self):
        print("Clase cadenas")
    def validar(self):
        print("validar")
    def ruta(self):
        print("ruta")
    def expandir(self):
        print("expandir")
    
class Cargar:
    def __init__(self):
        print("Clase cargar")
    def cargarAFD(self):
        print("cargar AFD")
    def cargarGra(self):
        print("Cargar Gramatica")

class Guardar:
    def __init__(self):
        print("Clase guardar")
    def save(self):
        print("guardar")

class Reportes:
    def __init__(self):
        print("Clase reportes") 
    def detalle(self):
        print("detalle")
    def generar(self):
        print("generar")


if __name__ == "__main__":
    Menu().inicio()