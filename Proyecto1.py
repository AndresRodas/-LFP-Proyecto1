import sys
import os
import glob

from graphviz import *
from io import open
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ListaAFD = []
ListaGramatica = []

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


    def inicio(self):
        os.system ("cls")
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

    def menu_afd(self):
        AFD().menu_afd()
    def menu_gramatica(self):
        MenuGramatica().menu_gramatica()
    def menu_cadenas(self):
        Cadenas().menu_cadenas()
    def menu_cargar(self):
        Cargar().menu_cargar()
    def menu_reportes(self):
        Reportes().menu_reportes()
    def Save(self):
        Guardar().save()

    def run(self):
        while True:
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

class Transicion:
    def __init__(self):
        self.simbolo = ''
        self.destino = ''
    def Simbolo(self, sim, dest):
        self.simbolo = sim
        self.destino = dest

    def ToString(self):
        print('\t Transicion: ')
        print('\t \t Simbolo: ', self.simbolo)
        print('\t \t Destino: ', self.destino)

class Estado:
    def __init__(self):
        self.nombre = ''
        self.transiciones = []
        self.inicial = False
        self.aceptacion = False
    def Nombre(self,nombre):
        self.nombre = nombre
    def Transiciones(self, simbolo, destino):
        trans = Transicion()
        trans.Simbolo(simbolo, destino)
        self.transiciones.append(trans)
    def Inicial(self, ini):
        self.inicial = ini
    def Aceptacion(self, acep):
        self.aceptacion = acep
    def ToString(self):
        print('Estado: ')
        print('\t Nombre: ', self.nombre)
        print('\t Estado inicial: ', self.inicial)
        print('\t Estado aceptacion: ', self.aceptacion)
        for j in range(0,len(self.transiciones)):
            self.transiciones[j].ToString()

class Automata:
    def __init__(self):
        self.nombre = ""
        self.estados = []
        self.alfabeto = []
        self.gram = []
        self.cadenav = []
        self.cadenai = []
    def CadenaV(self, cadena):
        self.cadenav.append(cadena)
    def CadenaI(self, cadena):
        self.cadenai.append(cadena)
    def Nombre(self, nombre):
        self.nombre = nombre
    def Alfabeto(self, alfabeto):
        self.alfabeto.append(alfabeto)
    def Estados(self, estados):
        est = Estado()
        est.Nombre(estados)
        self.estados.append(est)
    def Gramatica(self, gramatica):
        self.gram = gramatica.copy()
    def ToString(self):
        print('************************************')
        print('Nombre: '+self.nombre)
        print('Alfabeto: ',self.alfabeto)
        for k in self.estados:
            k.ToString()
        print('Conversion a gramática: ')
        for i in self.gram:
            print(i)

class AFD:

    def __init__(self):
        self.afdtemp = ''
        self.opcion_afd = {
            "1" : self.ingresar_estados,
            "2" : self.ingresar_alfabeto,
            "3" : self.estado_inicial,
            "4" : self.estado_aceptacion,
            "5" : self.transiciones,
            "6" : self.ayuda,
            "7" : self.back
        }

    def menu_afd(self):
        os.system ("cls")
        self.afdtemp = input("Ingrese el nombre del AFD: ")

        #Comprobar si ya existe para modificar o crear.
        estado = True
        for x in ListaAFD:
            if x.nombre == self.afdtemp:
                estado = False
                self.afd = x
        if estado:
            self.afd = Automata()
            self.afd.Nombre(self.afdtemp)
            ListaAFD.append(self.afd)

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
            else:
                print("{0} no es una opción".format(eleccion))

    def ingresar_estados(self):
        #Ingresar Estados
        estado = input("Ingrese estado: ")
        if len(self.afd.estados) != 0:
                contador = 0
                for k in range(0,len(self.afd.estados)):
                        if estado == self.afd.estados[k].nombre:
                                contador = contador + 1
                for i in range(0,len(self.afd.alfabeto)):
                        if estado == self.afd.alfabeto[i]:
                                contador = contador + 1
                if contador > 0:
                        print("El estado ya existe o es parte del alfabeto!")
                elif contador == 0:
                        print("El estado se ha ingresado!")
                        self.afd.Estados(estado)
        else:
            print("El estado se ha ingresado!")
            self.afd.Estados(estado)

    def ingresar_alfabeto(self):
        #Ingresar alfabeto
        alfabeto = input("Ingrese alfabeto: ")
        if len(self.afd.alfabeto) != 0:
                contador = 0
                for k in range(0,len(self.afd.estados)):
                        if alfabeto == self.afd.estados[k].nombre:
                                contador = contador + 1
                for i in range(0,len(self.afd.alfabeto)):
                        if alfabeto == self.afd.alfabeto[i]:
                                contador = contador + 1
                if contador > 0:
                        print("El alfabeto ya existe o es parte de los Estados!")
                elif contador == 0:
                        print("El alfabeto se ha ingresado!")
                        self.afd.alfabeto.append(alfabeto)
        else:
            print("El alfabeto se ha ingresado!")
            self.afd.alfabeto.append(alfabeto)

    def estado_inicial(self):
        #Estado inicial
        print("Estados: ")
        for x in self.afd.estados:
            print(x.nombre)
        inicial = input("Ingrese estado inicial: ")
        verificador = 0
        for k in range(0,len(self.afd.estados)):
            if inicial == self.afd.estados[k].nombre:
                self.afd.estados[k].inicial = True
                verificador = verificador + 1
                print("Estado inicial agregado")
            else:
                self.afd.estados[k].inicial = False
        if verificador == 0:
            print("El estado ingresado no existe, elija de nuevo!")
            self.estado_inicial()

    def estado_aceptacion(self):
        #Estado de aceptacion
        print("Estados: ")
        for x in self.afd.estados:
            print(x.nombre)
        inicial = input("Ingrese estado de aceptación: ")
        verificador = 0
        for k in range(0,len(self.afd.estados)):
            if inicial == self.afd.estados[k].nombre:
                self.afd.estados[k].aceptacion = True
                verificador = verificador + 1
                print("Estado de aceptación agregado")
        if verificador == 0:
            print("El estado ingresado no existe, elija de nuevo!")
            self.estado_aceptacion()

    def transiciones(self):
        os.system ("cls")
        print("""
                Modos de Transición:

                1) Modo 1
                2) Modo 2

            """)
        Modo = input("Seleccione una opción: ")
        if Modo == str(1):
            #Modo 1
            try:
                pos = 0
                transicion_temporal = input("Ingrese la transición de la forma A,B;0: ")
                trans = transicion_temporal.split(';')
                est = trans[0].split(',')
                contador = 0
                for k in range(0,len(self.afd.estados)):
                    if est[0] == self.afd.estados[k].nombre:
                        contador = contador + 1
                        pos = k
                    if est[1] == self.afd.estados[k].nombre:
                        contador = contador + 1
                for i in range(0,len(self.afd.alfabeto)):
                    if trans[1] == self.afd.alfabeto[i]:
                        contador = contador + 1

                for x in self.afd.estados:
                    for y in x.transiciones:
                        if (y.simbolo == trans[1] and y.destino == est[1] and x.nombre == est[0]) or trans[1] == 'epsilon':
                            contador = contador - 1
                            print('Esto solo es posible con un AFN')

                if contador == 3:
                    self.afd.estados[pos].Transiciones(trans[1],est[1])

                    print('La cadena es valida! los datos se han guardado')

                elif contador < 3:
                    print('La cadena es invalida!')
            except IndexError:
                print('La cadena es invalida!')

        elif Modo == str(2):
            #Modo 2
            columnas = input('Ingrese: [terminales]:  ')
            filas = input('Ingrese: [no terminales]:  ')
            simbolos = input('Ingrese: [simbolos destino]:  ')

            try:

                #recorrer filas (estados) para ingresar a ellos
                estados_temporales = filas.split('[')[1].split(']')[0].split(',')
                simbolo_temporal = columnas.split('[')[1].split(']')[0].split(',')
                destino_temporal = simbolos.split('[')[1].split(']')[0].split(';')
                for e in range(0,len(self.afd.estados)):
                    for t in range(0,len(estados_temporales)):
                        #se ingresa a un estado igual
                        if self.afd.estados[e].nombre == estados_temporales[t]:
                            for s in range(0,len(simbolo_temporal)):
                                estado = False
                                for c in self.afd.alfabeto:
                                    if c == simbolo_temporal[s]:
                                        estado = True
                                if estado:
                                    #se agregan las transiciones con destino y simbolo.
                                    dt = destino_temporal[t].split(',')[s]
                                    if dt != '-':
                                        self.afd.estados[e].Transiciones(simbolo_temporal[s], dt)
                                        print('Transicion ingresada correctamente')
                                else:
                                    print('Datos incorrectos!')
            except IndexError:
                print('Datos incorrectos!')

        else:
            print('Opcion invalida')

    def ModoUno():
        print('aqui va el modo 1')

    def ayuda(self):
        print('Lenguajes Formales y de Programacion A+')
        print('Aux: Elmer Real')
        print('0')
       

    def back(self):
        os.system ("cls")
        Menu().run()

class Gramatica:
    def __init__(self):
        self.nombre = ''
        self.no_terminales = []
        self.terminales = []
        self.nt_inicial = ''
        self.producciones = []
        self.prod_sin_rec = []
        self.afd = Automata()
        self.cadenav = []
        self.cadenai = []
    def CadenaV(self, cadena):
        self.cadenav.append(cadena)
    def CadenaI(self, cadena):
        self.cadenai.append(cadena)
    def Nombre(self,nombre):
        self.nombre = nombre
    def NoTerminales(self, nt):
        self.no_terminales.append(nt)
    def Terminales(self, te):
        self.terminales.append(te)
    def NtInicial(self, nt):
        self.nt_inicial = nt
    def Producciones(self, prod):
        self.producciones.append(prod)
    def Prod_sin_rec(self, p):
        self.prod_sin_rec.append(p)
    def Alfabeto(self, alfabeto):
        self.afd.Alfabeto(alfabeto)
    def Estados(self, estados):
        est = Estado()
        est.Nombre(estados)
        self.afd.estados.append(est)
    def ToString(self):
        print('Nombre: '+self.nombre)
        print('No terminales: ',self.no_terminales)
        print('Terminales: ',self.terminales)
        print('No terminal inicial: '+self.nt_inicial)
        print('Producciones: ')
        for prod in self.producciones:
            print(prod)
        print('Sin recursividad por izquierda: ')
        for psd in self.prod_sin_rec:
            print(psd)
        print('Conversion a autómata: ')
        self.afd.ToString()

class MenuGramatica:

    def __init__(self):
        self.nombre_gramatica = ""
        self.opcion_gramatica = {
            "1" : self.NT,
            "2" : self.T,
            "3" : self.NT_inicial,
            "4" : self.Producciones,
            "5" : self.Transformada,
            "6" : self.ayuda,
            "7" : self.back
        }

    def menu_gramatica(self):
        os.system ("cls")
        self.nombre_gramatica = input("Ingrese el nombre de la gramática: ")

        #Comprobar si ya existe para modificar o crear.
        estado = True
        for x in ListaGramatica:
            if x.nombre == self.nombre_gramatica:
                estado = False
                self.gram = x
        if estado:
            self.gram = Gramatica()
            self.gram.Nombre(self.nombre_gramatica)
            ListaGramatica.append(self.gram)

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
            else:
                print("{0} no es una opción".format(eleccion))

    def NT(self):
        #Ingresar NT
        nt = input("Ingrese no terminal: ")
        if len(self.gram.no_terminales) != 0:
                contador = 0
                for k in self.gram.no_terminales:
                        if nt == k:
                                contador = contador + 1
                for i in self.gram.terminales:
                        if nt == i:
                                contador = contador + 1
                if contador > 0:
                        print("El no terminal ya existe!")
                        self.NT()
                elif contador == 0 and nt.isupper():
                        print("El no terminal se ha ingresado!")
                        self.gram.NoTerminales(nt)
                else:
                    print("El no terminal debe estar en mayusculas")
                    self.NT()
        elif nt.isupper():
            print("El no terminal se ha ingresado!")
            self.gram.NoTerminales(nt)
        else:
            print("El no terminal debe estar en mayusculas")
            self.NT()

    def T(self):
        #Ingresar T
        t = input("Ingrese terminal: ")
        if len(self.gram.terminales) != 0:
                contador = 0
                for k in self.gram.terminales:
                        if t == k:
                                contador = contador + 1
                for i in self.gram.no_terminales:
                        if t == i:
                                contador = contador + 1
                if contador > 0:
                        print("El terminal ya existe!")
                        self.T()
                elif contador == 0 and (t.islower() or t.isnumeric()):
                        print("El terminal se ha ingresado!")
                        self.gram.Terminales(t)
                else:
                    print("El terminal debe estar en minusculas")
                    self.T()
        elif t.islower():
            print("El terminal se ha ingresado!")
            self.gram.Terminales(t)
        else:
            print("El terminal debe estar en minusculas")
            self.T()

    def NT_inicial(self):
        print('No terminales: ')
        for x in self.gram.no_terminales:
            print(x)
        nt_i = input('Ingrese no terminal inicial: ')
        contador = 0
        for x in self.gram.no_terminales:
            if nt_i == x:
                contador = contador + 1
        if contador > 0:
            self.gram.nt_inicial = nt_i
            print("El no terminal inicial se ha ingresado!")
        else:
            print('El termino no existe en los no terminales!')
            self.NT_inicial()

    def Producciones(self):
        gramatica_temporal = []
        gramatica_temporal.extend(self.gram.no_terminales)
        gramatica_temporal.extend(self.gram.terminales)
        produccion_temporal = input('Ingrese la producción: ')
        estado = 0
        for x in range(0,len(self.gram.producciones)):
            if produccion_temporal.split('>')[0] == self.gram.producciones[x].split('>')[0]:
                self.AgregarOr(gramatica_temporal, produccion_temporal, x)
                estado = estado + 1
        if estado == 0:
            self.AgregarProd(gramatica_temporal, produccion_temporal)

    def Transformada(self):
        # self.gram.prod_sin_rec = []
        # self.gram.prod_sin_rec.extend(self.gram.producciones)
        self.gram.prod_sin_rec = self.gram.producciones[:]
        
        estado = True
        #recorre las producciones de la gramatica
        for z in self.gram.producciones:
            prod_temp = z.split('>')[1].split(' | ')
            for n in prod_temp:
                #comprueba si tiene recursividad
                if n.split(' ')[0] == z.split('>')[0]:
                    self.Sustituir_Prod(z)
                    estado = False
                    break
        #si: no tiene recursividad por la izquierda...
        if estado:
            print('La gramática no tiene recursividad por la izquierda!')
            for x in self.gram.producciones:
                print(x)
        else:
            print('Gramática original: ')
            for z in self.gram.producciones:
                print(z)
            print('Gramática transformada: ')
            for y in self.gram.prod_sin_rec:
                print(y)

    def ayuda(self):
        print('Lenguajes Formales y de Programacion A+')
        print('Aux: Elmer Real')
        print('0')

    def back(self):
        os.system ("cls")
        Menu().run()

    def AgregarOr(self, gt, pt, num):
        try:
            lista_pt = pt.split('>')
            lista_d = lista_pt[1].split(' ')
            estado = 0
            for y in self.gram.no_terminales:
                if lista_pt[0] == y:
                    estado = estado + 1
            for k in lista_d:
                for x in gt:
                    if k == x:
                        estado = estado + 1
                if k == '|':
                        estado = estado + 1
                if k == 'epsilon':
                    estado = estado + 1
            for x in self.gram.producciones:
                if pt == x:
                    print('La producción ya ha sido ingresada!')
                    estado = estado - 1
            if estado == (len(lista_d)+1):
                self.gram.producciones[num] = self.gram.producciones[num] + ' | ' + pt.split('>')[1]
                print('Produccion agregada correctamente')
            else:
                print('Producción inválida, intente nuevamente...')
                self.Producciones()

        except IndexError:
            print('La entrada no es valida!!')

    def AgregarProd(self, gt, pt):
        try:
            lista_pt = pt.split('>')
            lista_d = lista_pt[1].split(' ')
            estado = 0
            if len(self.gram.producciones) == 0:
                if lista_pt[0] == self.gram.nt_inicial:
                    estado = estado + 1
                for k in lista_d:
                    for x in gt:
                        if k == x:
                            estado = estado + 1
                    if k == '|':
                        estado = estado + 1
                    if k == 'epsilon':
                        estado = estado + 1
                if estado == (len(lista_d)+1):
                    self.gram.Producciones(pt)
                    print('Produccion agregada correctamente')
                else:
                    print('Producción inválida, intente nuevamente...')
                    self.Producciones()
            else:
                for y in self.gram.no_terminales:
                    if lista_pt[0] == y:
                        estado = estado + 1
                for k in lista_d:
                    for x in gt:
                        if k == x:
                            estado = estado + 1
                    if k == '|':
                            estado = estado + 1
                    if k == 'epsilon':
                        estado = estado + 1
                for x in self.gram.producciones:
                    if pt == x:
                        print('La producción ya ha sido ingresada!')
                        estado = estado - 1
                if estado == (len(lista_d)+1):
                    self.gram.Producciones(pt)
                    print('Produccion agregada correctamente')
                else:
                    print('Producción inválida, intente nuevamente...')
                    self.Producciones()
        except IndexError:
            print('La entrada no es valida!!')

    def Sustituir_Prod(self, x):

        produc = x.split('>')[1].split(' | ')
        nt_comparador = x.split('>')[0]
        comp_prima = nt_comparador+"P"
        partes_no_rec = []
        partes_rec = []
        #ciclo que recorre las partes derechas de las producciones
        for n in produc:

            div_espacios = n.split(' ')
            if div_espacios[0] == nt_comparador:
                #agrega partes recursivas
                partes_rec.append(n.split(f'{nt_comparador} ')[1])
            else:
                #agrega partes no recursivas
                partes_no_rec.append(n)

        #produce la primera produccion sin recursividad por la izquierda
        first_cadena = nt_comparador+'>'
        for m in range(0,len(partes_no_rec)):
            if m == len(partes_no_rec)-1:
                first_cadena = first_cadena + partes_no_rec[m] + ' ' + comp_prima
            else:
                first_cadena = first_cadena + partes_no_rec[m] + ' ' + comp_prima + ' | '

        #produce la segunda produccion sin recursividad por la izquierda
        second_cadena = comp_prima+'>'
        for o in range(0,len(partes_rec)):
            if o == len(partes_rec)-1:
                second_cadena = second_cadena + partes_rec[o] + ' ' + comp_prima + ' | epsilon'
            else:
                second_cadena = second_cadena + partes_rec[o] + ' ' + comp_prima + ' | '

        #llenado la gramatica con las nuevas producciones
        for p in range(0,len(self.gram.prod_sin_rec)):

            if x == self.gram.prod_sin_rec[p]:
                self.gram.prod_sin_rec.pop(p)
                self.gram.prod_sin_rec.insert(p, second_cadena)
                self.gram.prod_sin_rec.insert(p, first_cadena)

    def ComprobarOr():
        for x in self.gram.producciones:
            v = x.split(' ')
            for y in v:
                if y == '|':
                    return True

class Cadenas:

    def __init__(self):
        self.tipo = ''
        self.nombre_eleccion = ''
        self.posicion = 0
        self.opcion_cadenas = {
            "1" : self.validar,
            "2" : self.ruta,
            "3" : self.expandir,
            "4" : self.ayuda,
            "5" : self.back
        }

    def menu_cadenas(self):
        self.nombre_eleccion = input("Ingrese el nombre del AFD o Gramática a evaluar: ")
        estado = False
        for x in range(0,len(ListaAFD)):
            if self.nombre_eleccion == ListaAFD[x].nombre:
                estado = True
                self.tipo = 'automata'
                self.posicion = x
        for y in range(0,len(ListaGramatica)):
            if self.nombre_eleccion == ListaGramatica[y].nombre:
                estado = True
                self.tipo = 'gramatica'
                self.posicion = y

        if estado:
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
                else:
                    print("{0} no es una opción".format(eleccion))
        else:
            print('El Afd o Gramatica ingresada no existe, intente nuevamente...')
            Menu().run()

    def validar(self):
        cadena = input('Ingrese la cadena a evaluar: ')
        if self.tipo == 'automata':
            #valida la cadena si es automata
            self.ValidarAutomata(ListaAFD[self.posicion], cadena, False)
        elif self.tipo == 'gramatica':
            if ListaGramatica[self.posicion].prod_sin_rec == []:
                ListaGramatica[self.posicion].prod_sin_rec.append(ListaGramatica[self.posicion].producciones)
            self.ValidarGramatica(ListaGramatica[self.posicion].prod_sin_rec, cadena, False)

    def ruta(self):
        cadena = input('Ingrese la cadena a expandir: ')
        if self.tipo == 'automata':
            print('Ruta en AFD: ')
            self.ValidarAutomata(ListaAFD[self.posicion], cadena, True)
        elif self.tipo == 'gramatica':
            self.ValidarAutomata(self.TransformarGramatica(self.posicion), cadena, True)

    def expandir(self):
        cadena = input('Ingrese la cadena a expandir: ')
        if self.tipo == 'automata':
            self.ValidarGramatica(self.TransformarAutomata(self.posicion), cadena, True)
        elif self.tipo == 'gramatica':
            if ListaGramatica[self.posicion].prod_sin_rec == []:
                ListaGramatica[self.posicion].prod_sin_rec.append(ListaGramatica[self.posicion].producciones)
            self.ValidarGramatica(ListaGramatica[self.posicion].prod_sin_rec, cadena, True)

    def TransformarAutomata(self, pos):
        #vector temporal
        gramatica = []

        #se recorren los estados
        for x in ListaAFD[pos].estados:
            temp = x.nombre+'>'
            #se recorren las transiciones
            for y in range(0,len(x.transiciones)):
                #si es el ultimo
                if y == (len(x.transiciones)-1):
                    temp = temp + x.transiciones[y].simbolo + ' ' + x.transiciones[y].destino
                else:
                    temp = temp + x.transiciones[y].simbolo + ' ' + x.transiciones[y].destino + ' | '
            #si es estado de aceptacion se le agrega epsilon
            if x.aceptacion:
                temp = temp + ' | epsilon'
            gramatica.append(temp)

        print('AFD transformado a gramática: ')
        for g in gramatica:
            print(g)
        ListaAFD[pos].Gramatica(gramatica)
        return gramatica

    def TransformarGramatica(self, pos):
        ListaGramatica[pos].afd.estados = []
        ListaGramatica[pos].afd.alfabeto = []
        #recorre la gramatica sin recursividad
        for n in ListaGramatica[pos].prod_sin_rec:
            #crea el nuevo estado
            ListaGramatica[pos].Estados(n.split('>')[0])
            transiciones = n.split('>')[1].split(' | ')
            #recorre las posibles transiciones del nuevo estado
            for t in transiciones:
                #si es de aceptacion
                if t == 'epsilon':
                    for acep in ListaGramatica[pos].afd.estados:
                        if acep.nombre == n.split('>')[0]:
                            acep.aceptacion = True
                #si no es de aceptacion
                else:
                    #recorre los estados y encuentra el estado recien creado
                    for tr in ListaGramatica[pos].afd.estados:
                        if tr.nombre == n.split('>')[0]:
                            #le agrega las transiciones al estado recien creado
                            tr.Transiciones(t.split(' ')[0], t.split(' ')[1])
                    #se verifica si el alfabeto esta vacio
                    if ListaGramatica[pos].afd.alfabeto == []:
                        #se agrega la letra nueva
                        ListaGramatica[pos].afd.alfabeto.append(t.split(' ')[0])
                    else:
                        #sino se recorre el alfabeto
                        no_existe = True
                        for a in ListaGramatica[pos].afd.alfabeto:
                            #se compara si existe la letra
                            if a == t.split(' ')[0]:
                                no_existe = False
                        if no_existe:
                            #si no eciste entonces agrega nueva letra al alfabeto
                            ListaGramatica[pos].afd.alfabeto.append(t.split(' ')[0])
        #asigna el estado inicial
        for ini in ListaGramatica[pos].afd.estados:
            if ini.nombre == ListaGramatica[pos].prod_sin_rec[0].split('>')[0]:
                ini.inicial = True
        #muestra automata generado
        return ListaGramatica[pos].afd

    def ValidarAutomata(self, afd, cad, ruta):
        estado = ''
        #recorre los estados del afd seleccionado
        for e in afd.estados:
            if e.inicial == True:
                #declara estado inicial
                estado = e.nombre
        #recorre la cadena
        for x in cad:
            #entra a ciclo para verificar que exista en alfabeto
            comprobador_alfabeto = False
            for a in afd.alfabeto:
                if x == a:
                    comprobador_alfabeto = True
            if comprobador_alfabeto:
                #recorre los estados
                for l in afd.estados:
                    #estado actual igual al estado del afd
                    if estado == l.nombre:
                        #recorre las transiciones del estado
                        for t in l.transiciones:
                            if x == t.simbolo:
                                #imprime si hay que mostrar ruta
                                if ruta:
                                    print(f'{estado},{t.destino};{x}')
                                #asigna nuevo estado
                                estado = t.destino
                                break
                        break
            else:
                estado = ''
                break
        #verifica estado de confirmacion
        comp = False
        for k in afd.estados:
            if k.nombre == estado and k.aceptacion == True:
                comp = True
        if comp:
            print('La cadena es valida!')
            ListaAFD[self.posicion].CadenaV(cad)

        else:
            print('La cadena es incorrecta!')
            ListaAFD[self.posicion].CadenaI(cad)

    def ValidarGramatica(self, trans, cad, exp):
        print('Expansión en gramática: ')
        alfabeto_temporal = []
        for m in trans:
            
            for n in m.split('>')[1].split(' '):
                alfabeto_temporal.append(n)

        estado = trans[0].split('>')[0]
        # print(estado + ' --> ')
        letra = ''
        #recorre letra de cadena
        for c in cad:
            #comprueba que el valor exista
            status = False
            for a in alfabeto_temporal:
                if c == a:
                    status = True
            if status == True:
                #recorre prod de trans
                for t in trans:
                    #si estado es de prod
                    if estado == t.split('>')[0]:
                        for n in t.split('>')[1].split(' | '):
                            if n.split(' ')[0] == c:
                                z = n.split(' ')[1]
                                letra = letra + c
                                if exp:
                                    print(f'{letra} {z}')
                                #asigna nuevo estado
                                estado = z
                                break
                        break
            else:
                estado = ''
                break

        value = False
        for m in trans:
            if m.split('>')[0] == estado:
                for i in m.split('>')[1].split(' | '):
                    if i == 'epsilon':
                        value = True
        if value:
            print(letra + ' epsilon --> '+ letra)
            print('Cadena valida!')
            ListaGramatica[self.posicion].CadenaV(cad)
        else:
            print('Cadena invalida!')
            ListaGramatica[self.posicion].CadenaI(cad)

    def ayuda(self):
        print('Lenguajes Formales y de Programacion A+')
        print('Aux: Elmer Real')
        print('0')

    def back(self):
        os.system ("cls")
        Menu().run()

class Cargar:

    def __init__(self):
        self.opcion_cargar = {
            "1" : self.cargarAFD,
            "2" : self.cargarGra,
            "3" : self.back
        }

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

    def cargarAFD(self):
        try:
            targetPattern = r"*.afd"
            x = glob.glob(targetPattern)[0].split('.')[0]

            archivo = open(f'{x}.afd','r')
            automatas_linea = archivo.readlines()
            archivo.close()

            new_afd = Automata()
            new_afd.Nombre(x)

            for a in automatas_linea:
                estados_izq = a.split('\n')[0].split(';')[0].split(',')
                estados_der = a.split('\n')[0].split(';')[1].split(',')
                #agregar estados
                comprobador = True
                for n in new_afd.estados:
                    if n.nombre == estados_izq[0]:
                        comprobador = False
                if comprobador:
                    new_afd.Estados(estados_izq[0])

                comprobador = True
                for n in new_afd.estados:
                    if n.nombre == estados_izq[1]:
                        comprobador = False
                if comprobador:
                    new_afd.Estados(estados_izq[1])

                #inicial
                for n in new_afd.estados:
                    if n.nombre == automatas_linea[0].split(',')[0]:
                        n.inicial = True

                #aceptacion
                if estados_der[0] == 'true':
                    for n in new_afd.estados:
                        if n.nombre == estados_izq[0]:
                            n.aceptacion = True

                if estados_der[1] == 'true':
                    for n in new_afd.estados:
                        if n.nombre == estados_izq[1]:
                            n.aceptacion = True
                #alfabeto
                if new_afd.alfabeto == []:
                    new_afd.Alfabeto(estados_izq[2])
                else:
                    cont = True
                    for alfa in new_afd.alfabeto:
                        if alfa == estados_izq[2]:
                            cont = False
                    if cont:
                        new_afd.Alfabeto(estados_izq[2])

                #transicion:
                try:
                    pos = 0
                    transicion_temporal = a.split('\n')[0].split(';')[0]
                    trans = transicion_temporal.split(',')[2]
                    est1 = transicion_temporal.split(',')[0]
                    est2 = transicion_temporal.split(',')[1]
                    contador = 0
                    for k in range(0,len(new_afd.estados)):
                        if est1 == new_afd.estados[k].nombre:
                            contador = contador + 1
                            pos = k
                        if est2 == new_afd.estados[k].nombre:
                            contador = contador + 1
                    for i in range(0,len(new_afd.alfabeto)):
                        if trans == new_afd.alfabeto[i]:
                            contador = contador + 1

                    for x in new_afd.estados:
                        for y in x.transiciones:
                            if (y.simbolo == trans and y.destino == est2 and x.nombre == est1) or trans == 'epsilon':
                                contador = contador - 1
                                print('Esto solo es posible con un AFN')
                    if contador == 3:
                        new_afd.estados[pos].Transiciones(trans,est2)

                    elif contador < 3:
                        print('La cadena es invalida!')
                except IndexError:
                    print('La cadena es invalida!')

            ListaAFD.append(new_afd)
            print('El archivo se ha cargado!')

        except IndexError:
            print('el archivo tiene comandos invalidos!')

    def cargarGra(self):
        try:
            targetPattern = r"*.grm"
            x = glob.glob(targetPattern)[0].split('.')[0]

            archivo = open(f'{x}.grm','r')
            gramaticas_linea = archivo.readlines()
            archivo.close()

            new_gram = Gramatica()
            new_gram.Nombre(x)

            for g in gramaticas_linea:
                nt = g.split('\n')[0].split('>')[0]
                izq = g.split('\n')[0].split('>')[1].split(' ')

                #agregar no terminales
                flag = True
                if new_gram.no_terminales == [] and nt.isupper:
                    new_gram.NoTerminales(nt)
                    new_gram.NtInicial(nt)
                else:
                    for t in new_gram.no_terminales:
                        if t == nt:
                            flag = False
                    if flag and nt.isupper():
                        new_gram.NoTerminales(nt)

                #agregar valores lado izquierdo
                for i in izq:
                    if i.islower():
                        term = True
                        for t in new_gram.terminales:
                            if t == i:
                                term = False
                        if term:
                            new_gram.Terminales(i)
                    elif i.isnumeric():
                        term = True
                        for t in new_gram.terminales:
                            if t == i:
                                term = False
                        if term:
                            new_gram.Terminales(i)
                    elif i.isupper():
                        term = True
                        for t in new_gram.no_terminales:
                            if t == i:
                                term = False
                        if term:
                            new_gram.NoTerminales(i)

                pas = True
                if new_gram.producciones == []:
                    new_gram.Producciones(g.split('\n')[0])
                    pas = False
                else:
                    for n in range(0,len(new_gram.producciones)):
                        if new_gram.producciones[n].split('>')[0] == nt:
                            new_gram.producciones[n] = new_gram.producciones[n] + ' | ' + g.split('\n')[0].split('>')[1]
                            #self.gram.producciones[num] = self.gram.producciones[num] + ' | ' + pt.split('>')[1]
                            pas = False
                if pas:
                    new_gram.Producciones(g.split('\n')[0])
            ListaGramatica.append(new_gram)
            new_gram.ToString()
            print('El archivo se ha cargado!')
#prod_sin_rec
        except:
            print('la cadena contiene valores erroneos..')

    def ayuda(self):
        print('Lenguajes Formales y de Programacion A+')
        print('Aux: Elmer Real')
        print('0')

    def back(self):
        os.system ("cls")
        Menu().run()

class Guardar:
    def __init__(self):

        os.system ("cls")
        self.nombre = input('Ingrese el nombre del AFD o Gramatica a guardar: ')
        self.destino = input('Ingrese el nombre con el que desea guardarlo: ')

        self.save()

    def save(self):
        for a in ListaAFD:
            if a.nombre == self.nombre:
                archivo2 = open(f'{self.destino}.afd','w')
                for e in a.estados:
                    for t in e.transiciones:
                         archivo2.write(f'{e.nombre},{t.destino},{t.simbolo};{e.inicial},{e.aceptacion}'+'\n')
                archivo2.close()
                input('El archivo se ha Guardado, presione enter para continuar..')

        for g in ListaGramatica:
            if g.nombre == self.nombre:
                archivo2 = open(f'{self.destino}.grm','w')
                for s in g.producciones:
                    archivo2.write(s+'\n')
                archivo2.close()
                input('El archivo se ha Guardado, presione enter para continuar..')
        os.system ("cls")
        Menu().run()



    def ayuda(self):
        print('Lenguajes Formales y de Programacion A+')
        print('Aux: Elmer Real')
        print('0')

    def back(self):
        os.system ("cls")
        Menu().run()

class Reportes:
    def __init__(self):
        self.nombre = ''
        self.tipo = ''
        self.posicion = ''
        self.opcion_reportes = {
            "1" : self.detalle,
            "2" : self.generarPDF,
            "3" : self.ayuda,
            "4" : self.back
        }

    def menu_reportes(self):

        self.nombre = input("Ingrese el nombre del AFD o Gramática a reportar: ")
        estado = False
        for x in range(0,len(ListaAFD)):
            if self.nombre == ListaAFD[x].nombre:
                estado = True
                self.tipo = 'automata'
                self.posicion = x
        for y in range(0,len(ListaGramatica)):
            if self.nombre == ListaGramatica[y].nombre:
                estado = True
                self.tipo = 'gramatica'
                self.posicion = y

        if estado:
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
        else:
            print('El archivo no existe!')
            Menu().run()

    def detalle(self):

        if self.tipo == 'automata':
            for d in ListaAFD:
                if d.nombre == self.nombre:
                    self.TransformarAutomata(self.posicion)
                    d.ToString()

        elif self.tipo == 'gramatica':
            for d in ListaGramatica:
                if d.nombre == self.nombre:
                    self.Transformada(d)
                    self.TransformarGramatica(self.posicion)
                    d.ToString()

    def generarPDF(self):
        #se crea el grafo
        dot = Digraph()
        #se busca el automata
        if self.tipo == 'automata':
            for d in ListaAFD:
                if d.nombre == self.nombre:
                    for e in d.estados:
                        #se crean los estados
                        dot.node(e.nombre, e.nombre)
                        for t in e.transiciones:
                            #se crean las transiciones
                            dot.edge(e.nombre, t.destino, label=t.simbolo)
                    dot.node('text',d.nombre)
                    print('El grafo se ha creado!')
                    #se crea el pdf
                    dot.render(d.nombre)

                    #imprime gramaticas
                    k = 790
                    c = canvas.Canvas(f"{d.nombre}-Gramaticas.pdf", pagesize=A4)
                    c.drawString(50,k, 'Gramatica')
                    
                    for j in range(0,len(d.gram)):
                        c.drawString(50, k - (j+1)*15, d.gram[j])

                    i = 650
                    c.drawString(50,i, 'Cadenas validas:')
                    for j in range(0,len(d.cadenav)):
                        c.drawString(50, i - (j+1)*15, d.cadenav[j])
                    
                    l = 520
                    c.drawString(50,l, 'Cadenas invalidas:')
                    for j in range(0,len(d.cadenai)):
                        c.drawString(50, l - (j+1)*15, d.cadenai[j])

                    c.showPage()
                    c.save()


        

        if self.tipo == 'gramatica':
            for d in ListaGramatica:
                if d.nombre == self.nombre:
                    for e in d.afd.estados:
                        #se crean los estados
                        dot.node(e.nombre, e.nombre)
                        for t in e.transiciones:
                            #se crean las transiciones
                            dot.edge(e.nombre, t.destino, label=t.simbolo)
                    print('El grafo se ha creado!')
                    #se crea el pdf
                    dot.render(d.nombre)

                    #imprime gramaticas
                    k = 790
                    c = canvas.Canvas(f"{d.nombre}-Gramaticas.pdf", pagesize=A4)
                    c.drawString(50,k, 'Gramática:')
                    for j in range(0,len(d.producciones)):
                        c.drawString(50, k - (j+1)*15, d.producciones[j])
                    
                    h = 650
                    c.drawString(50,h, 'Gramática sin recursividad a la izquierda:')
                    for j in range(0,len(d.prod_sin_rec)):
                        c.drawString(50, h - (j+1)*15, d.prod_sin_rec[j])
                    
                    i = 520
                    c.drawString(50,i, 'Cadenas validas:')
                    for j in range(0,len(d.cadenav)):
                        c.drawString(50, i - (j+1)*15, d.cadenav[j])
                    
                    l = 350
                    c.drawString(50,l, 'Cadenas invalidas:')
                    for j in range(0,len(d.cadenai)):
                        c.drawString(50, l - (j+1)*15, d.cadenai[j])
                        
                
                    c.showPage()
                    c.save()

    def TransformarAutomata(self, pos):
            #vector temporal
            gramatica = []

            #se recorren los estados
            for x in ListaAFD[pos].estados:
                temp = x.nombre+'>'
                #se recorren las transiciones
                for y in range(0,len(x.transiciones)):
                    #si es el ultimo
                    if y == (len(x.transiciones)-1):
                        temp = temp + x.transiciones[y].simbolo + ' ' + x.transiciones[y].destino
                    else:
                        temp = temp + x.transiciones[y].simbolo + ' ' + x.transiciones[y].destino + ' | '
                #si es estado de aceptacion se le agrega epsilon
                if x.aceptacion:
                    temp = temp + ' | epsilon'
                gramatica.append(temp)

            ListaAFD[pos].Gramatica(gramatica)
            return gramatica

    def TransformarGramatica(self, pos):
        ListaGramatica[pos].afd.estados = []
        ListaGramatica[pos].afd.alfabeto = []
        #recorre la gramatica sin recursividad
        for n in ListaGramatica[pos].prod_sin_rec:
            #crea el nuevo estado
            ListaGramatica[pos].Estados(n.split('>')[0])
            transiciones = n.split('>')[1].split(' | ')
            #recorre las posibles transiciones del nuevo estado
            for t in transiciones:
                #si es de aceptacion
                if t == 'epsilon':
                    for acep in ListaGramatica[pos].afd.estados:
                        if acep.nombre == n.split('>')[0]:
                            acep.aceptacion = True
                #si no es de aceptacion
                else:
                    #recorre los estados y encuentra el estado recien creado
                    for tr in ListaGramatica[pos].afd.estados:
                        if tr.nombre == n.split('>')[0]:
                            #le agrega las transiciones al estado recien creado
                            tr.Transiciones(t.split(' ')[0], t.split(' ')[1])
                    #se verifica si el alfabeto esta vacio
                    if ListaGramatica[pos].afd.alfabeto == []:
                        #se agrega la letra nueva
                        ListaGramatica[pos].afd.alfabeto.append(t.split(' ')[0])
                    else:
                        #sino se recorre el alfabeto
                        no_existe = True
                        for a in ListaGramatica[pos].afd.alfabeto:
                            #se compara si existe la letra
                            if a == t.split(' ')[0]:
                                no_existe = False
                        if no_existe:
                            #si no eciste entonces agrega nueva letra al alfabeto
                            ListaGramatica[pos].afd.alfabeto.append(t.split(' ')[0])
        #asigna el estado inicial
        for ini in ListaGramatica[pos].afd.estados:
            if ini.nombre == ListaGramatica[pos].prod_sin_rec[0].split('>')[0]:
                ini.inicial = True
        #muestra automata generado
        return ListaGramatica[pos].afd

    def Transformada(self, gram):
        gram.prod_sin_rec = gram.producciones.copy()
        #self.gram.prod_sin_rec = self.gram.producciones[:]
        estado = True
        #recorre las producciones de la gramatica
        for z in gram.producciones:
            prod_temp = z.split('>')[1].split(' | ')
            for n in prod_temp:
                #comprueba si tiene recursividad
                if n.split(' ')[0] == z.split('>')[0]:
                    self.Sustituir_Prod(z , gram)
                    estado = False
                    break
        #si: no tiene recursividad por la izquierda...
        if estado:
            print('La gramática no tiene recursividad por la izquierda!')

    def Sustituir_Prod(self, x, gram):

        produc = x.split('>')[1].split(' | ')
        nt_comparador = x.split('>')[0]
        comp_prima = nt_comparador+"P"
        partes_no_rec = []
        partes_rec = []
        #ciclo que recorre las partes derechas de las producciones
        for n in produc:

            div_espacios = n.split(' ')
            if div_espacios[0] == nt_comparador:
                #agrega partes recursivas
                partes_rec.append(n.split(f'{nt_comparador} ')[1])
            else:
                #agrega partes no recursivas
                partes_no_rec.append(n)

        #produce la primera produccion sin recursividad por la izquierda
        first_cadena = nt_comparador+'>'
        for m in range(0,len(partes_no_rec)):
            if m == len(partes_no_rec)-1:
                first_cadena = first_cadena + partes_no_rec[m] + ' ' + comp_prima
            else:
                first_cadena = first_cadena + partes_no_rec[m] + ' ' + comp_prima + ' | '

        #produce la segunda produccion sin recursividad por la izquierda
        second_cadena = comp_prima+'>'
        for o in range(0,len(partes_rec)):
            if o == len(partes_rec)-1:
                second_cadena = second_cadena + partes_rec[o] + ' ' + comp_prima + ' | epsilon'
            else:
                second_cadena = second_cadena + partes_rec[o] + ' ' + comp_prima + ' | '

        #llenado la gramatica con las nuevas producciones
        for p in range(0,len(gram.prod_sin_rec)):

            if x == gram.prod_sin_rec[p]:
                gram.prod_sin_rec.pop(p)
                gram.prod_sin_rec.insert(p, second_cadena)
                gram.prod_sin_rec.insert(p, first_cadena)

    def ayuda(self):
        print('Lenguajes Formales y de Programacion A+')
        print('Aux: Elmer Real')
        print('0')

    def back(self):
        os.system ("cls")
        Menu().run()

if __name__ == "__main__":
    Menu().inicio()