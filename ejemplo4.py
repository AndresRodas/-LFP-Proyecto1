class Gramatic():
    def __init__(self):
        self.nombre = ''
        self.no_terminales = []
        self.terminales = []
        self.nt_inicial = ''
        self.producciones = []
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
    def ToString(self):
        print('Nombre: '+self.nombre)
        print('No terminales: ',self.no_terminales)
        print('Terminales: ',self.terminales)
        print('No terminal inicial: '+self.nt_inicial)
        print('Producciones: ', self.producciones)

prod = ['S>a A | b B', 'A>A 0 | A 1 | 0', 'B>b s | m']

def Recursividad():
    estado = True
    #recorre las produccines de la gramatica
    for z in prod:
        prod_temp = z.split('>')[1].split(' | ')
        for n in prod_temp:
            #comprueba si tiene recursividad
            if n.split(' ')[0] == z.split('>')[0]:
                Sustituir_Prod(z)
                estado = False
                break
    #si: no tiene recursividad por la izquierda...
    if estado:
        print('La gramática no tiene recursividad por la izquierda!') 

def Sustituir_Prod(x):
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
            partes_rec.append(div_espacios[1])
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
    for p in range(0,len(prod)):
        if x == prod[p]:
            prod.pop(p)
            prod.insert(p, second_cadena)
            prod.insert(p, first_cadena)

print('Gramatica con rii: ')
for f in prod:
    print(f)
Recursividad()
print('Gramatica sin rii: ')
for f in prod:
    print(f)               
      
