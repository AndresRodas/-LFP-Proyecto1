
estados = ['s1','s2','s3','s4']

# #Modo 2
# columnas = input('Ingrese: [terminales separados por comas]')
# filas = input('Ingrese: [no terminales separados por comas]')
# simbolos = input('Ingrese: [interior de matriz por comas y columnas por punto y coma]')

# #recorrer filas (estados) para ingresar a ellos
# estados_temporales = filas.split('[')[1].split(']')[0].split(',')
# for e in estados:
#     for t in estados_temporales:
#         if e == t:
#             pass
trans = ['A>1 A | 0 B', 'B>1 B | 0 C', 'C>0 C | 1 C | epsilon']
cad = '11001'
print('Expansión en gramática: ')
estado = trans[0].split('>')[0]
print(estado + ' --> ')
letra = ''
#recorre letra de cadena
for c in cad:
    #comprueba que el valor exista
    status = False
    for m in trans:
        for o in m.split('>')[1].split(' | '):
            if c == o.split(' ')[0]:
                status = True
    if status:
        #recorre prod de trans
        for t in trans:
            #si estado es de prod
            if estado == t.split('>')[0]:
                for n in t.split('>')[1].split(' | '):
                    if n.split(' ')[0] == c:
                        z = n.split(' ')[1]
                        #print()
                        letra = letra + c
                        print(f'{letra} {z}')
                        #asigna nuevo estado
                        estado = z
                        break
                break
    else:
        print('Cadena invalida!')
        estado = ''

value = False
for m in trans:
    if m.split('>')[0] == estado:
        for i in m.split('>')[1].split(' | '):
            if i == 'epsilon':
                value = True
if value:
    print(letra + ' epsilon --> '+ letra)
    print('Cadena valida!')
else:
    print('Cadena invalida!')
        
        
    
    

