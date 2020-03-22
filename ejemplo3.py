
Automatas = []
class Transiciones:
    def __init__(self):
        self.simbolo = ''
        self.destino = ''
    def Simbolo(self, sim):
        self.simbolo = sim
    def Destino(self, dest):
        self.destino = dest
    def ToString(self):
        print('\t Transicion: ')
        print('\t \t Simbolo: ', self.simbolo)
        print('\t \t Destino: ', self.destino)

class Estados:
    def __init__(self):
        self.nombre = ''
        self.transiciones = []
        self.inicial = False
        self.aceptacion = False
    def Nombre(self,nombre):
        self.nombre = nombre
    def Transiciones(self, simbolo):
        trans = Transiciones()
        trans.Simbolo(simbolo)
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
    def Nombre(self, nombre):
        self.nombre = nombre
    def Alfabeto(self, alfabeto):
        self.alfabeto.append(alfabeto)
    def Estados(self, estados):
        est = Estados()
        est.Nombre(estados)
        self.estados.append(est)
    def ToString(self):
        print('************************************')
        print('Nombre: '+self.nombre)
        print('Alfabeto: ',self.alfabeto)
        for k in range(0,len(self.estados)):
            self.estados[k].ToString()

asd = Automata()
asd.ToString()
objeto.Alfabeto('parametros')
objeto.Nombre('parametros')
objeto.Estados('parametros')
objeto.estados[posicion].Inicial('parametros')
objeto.estados[posicion].Aceptacion('parametros')
objeto.estados[posicion].Transiciones('parametros')
objeto.estados[posicion].transiciones[posicion].Simbolo('parametros')
objeto.estados[posicion].transiciones[posicion].Destino('parametros')






