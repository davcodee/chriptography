
def cleanKey( cadena):
    """
        Método que límpia nuestra cadena quitando los elementos repetidos
    """
    print(cadena)
    c = cadena.upper()
    cadenaLimpia = []
    for i in c:
        if i == 'J' and  i not in cadenaLimpia:
            cadenaLimpia.append('I')
        if i not in cadenaLimpia and i != 'J':
            cadenaLimpia.append(i)
        
    return cadenaLimpia


def cleanText(text):
    """
        Método que regresa nuestro mensaje con x
    """
    clean_text = []

    for i in text:
        if i in clean_text:
            clean_text.append('x')
            clean_text.append(i)
        else:
            clean_text.append(i)

    return clean_text


def creaMatriz(arreglo):
    """
        Método que nos regresa todos los elementos de nuestra matriz
        en forma de lista.
    """
    abecedario = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    # agregamos de 5 en 5 elementos a nuestra matriz
    aux = arreglo
    print(aux)
    for i in abecedario:
        if i not in aux:
            aux.append(i)

    print(aux)
    return aux

def mismaColumna(a, b, lista):
    """
        Función que nos dice si estan en la misma columna
    """
    aux =[]
    for i in range(5):
        piso = 0
        techo = 5
        lista = rango(piso,techo, lista)
        if a in lista and b in lista:
            if lista.index(b) == 5:
                aux.append(lista[lista.index(a) + 1])    
                aux.append(lista[0])
                
            else:
                aux.append(lista[lista.index(a) + 1])
                aux.append(lista[lista.index(b) + 1])
            break
        else:
            piso  += 5
            techo += 5
            lista.clear()
    
    return aux
        
def mismaFila(a,b, matriz):
    """
        Función que nos dice si dos elementos están en en la misma columna
    """
    
    # indice de a y b
    indexA = 0
    indexB = 0
    #Columna a la que pertenecen a y b
    columnA = 0
    columnB = 0 

    # lista donde guardaremos los elementos encriptados
    aux = []

   
   
    # Iteraaciones y busqueda por culmna
    for i in range(5):
        #Piso y techo a buscar
        techo = i * 5  
        piso  = techo - 5
        #rango en el cual buscaremos
        lista = rango(piso, techo, matriz)
        print(lista)
        if a  in lista:
            indexA = lista.index(a)
            columnA = i

        if b in lista:
            indexB = lista.index(b)
            columnB = i
        else:
            lista.clear()

    if indexA == indexB:
        if columnA == 5 :
            #agregamos el elemento A
            techo = 5
            piso = 0
            lista = rango(piso, techo, matriz)
            aux.append(lista[indexA])
            
        if columnB == 5 :
            # Agregamos el elemento B
            techo = 5
            piso = 0
            lista = rango(piso, techo, matriz)
            aux.append(lista[indexB])
            
        else:
            #Para el caracter A
            techo = (columnA + 1) * 5
            piso  = techo - 5
            lista =  rango(piso, techo, matriz)
            aux.append(lista[indexA])

            #Para el caracter B
            techo = (columnB +  1 ) * 5
            piso = techo - 5
            lista = rango(piso, techo, matriz)
            aux.append(lista[indexB])

    return aux
        

        

def rango(a, b,lista):
    elements = []
    for i in lista[a:b]:
        elements.append(i)
    return elements
    
def main(): 
    """
        Función principal
    """
    key = input('Ingresa la cadena la llave:')
    #text = input('Ingresa la cadena a encriptar:')
    # llave ya limpia
    keyClean       = cleanKey(key)

    #texto con el formato establecido
   # textClean      = cleanText(text)



    #matriz en el orde correcto
    matriz = creaMatriz(keyClean)

    #print(mismaColumna('A','B', matriz))
    print(mismaFila('A','F', matriz))
 

main()




