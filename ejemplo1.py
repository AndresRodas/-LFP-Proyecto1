import sys
import os

from io import open
  
os.system ("cls")
AFD = input("ingrese el nombre del AFD: ")
Estados = ["jaja","jeje","jiji"]
Alfabetos = ["jojo", "juju"]
Estado_Inicial = ""
Estado_Aceptacion = ""

#Ingresar Estados
estado = input("Ingrese estado: ")
if len(Estados) != 0:           
        contador = 0
        for k in range(0,len(Estados)):
                if estado == Estados[k]:
                        contador = contador + 1
        for i in range(0,len(Alfabetos)):
                if estado == Alfabetos[i]:
                        contador = contador + 1
        if contador > 0:
                print("El estado ya existe o es parte del alfabeto!")
        elif contador == 0:
                print("El estado se ha ingresado!")
                Estados.append(estado)
else:
        Estados.append(estado)                        
print(Estados)

#Ingresar alfabeto
alfabeto = input("Ingrese alfabeto: ")
if len(Alfabetos) != 0:           
        contador = 0
        for k in range(0,len(Estados)):
                if alfabeto == Estados[k]:
                        contador = contador + 1
        for i in range(0,len(Alfabetos)):
                if alfabeto == Alfabetos[i]:
                        contador = contador + 1
        if contador > 0:
                print("El alfabeto ya existe o es parte de los Estados!")
        elif contador == 0:
                print("El alfabeto se ha ingresado!")
                Alfabetos.append(alfabeto)
else:
        Alfabetos.append(alfabeto)                                
print(Alfabetos)

#Estado inicial
print("Estados: ")
print(Estados)
inicial = input("Ingrese estado inicial: ")
verificador = 0
for k in range(0,len(Estados)):
        if inicial == Estados[k]:
                verificador = verificador + 1
if verificador > 0:
        print("Estado inicial agregado")
        Estado_Inicial = inicial
else:
        print("El estado ingresado no existe!")
print(Estado_Inicial)

#Estado de aceptacion
print("Estados: ")
print(Estados)
aceptacion = input("Ingrese estado de aceptación: ")
verificador = 0
for k in range(0,len(Estados)):
        if aceptacion == Estados[k]:
                verificador = verificador + 1
if verificador > 0:
        print("Estado de aceptación agregado")
        Estado_Aceptacion = aceptacion
else:
        print("El estado ingresado no existe!")
print(Estado_Aceptacion)

