#GRUPO 1A
#Gurrola Alvarez Carlos Fernando



#Los de abajo es el jugador 1 osea la cordenada 00
EMPTY = "-"
TORRE = "T"
PEON  = "P"
REY = "R"
REINA = "Q"
ALFIL = "A"
CABALLO = "C"
#Creamos un tablero vacio
tablero = []
#aqui hie un tipo checkpoint para que entre al bucle
flag = True
#Aqui van a ser las coordenadas como de estado presente y estado final a y b
a = [0,0]
b = [0,0]
#Aqui las piezas
Pieza = [PEON, TORRE, CABALLO, ALFIL, REY, REINA]
T = ""
#Se hace el tablero
for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append(fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

tablero[0][2] = ALFIL
tablero[0][5] = ALFIL
tablero[7][2] = ALFIL
tablero[7][5] = ALFIL

tablero[0][1] = CABALLO
tablero[0][6] = CABALLO
tablero[7][1] = CABALLO
tablero[7][6] = CABALLO

tablero[7][4] = REY
tablero[0][4] = REY
tablero[7][3] = REINA
tablero[0][3] = REINA
#Aqui hice u bucle para generar todos los peones para no hacer el codigo tan largo
for i in range(8):
        tablero[1][i] = PEON

for i in range(8):
        tablero[6][i] = PEON
#Imprimimos el tablero
print(tablero[7])
print(tablero[6])
print(tablero[5])
print(tablero[4])
print(tablero[3])
print(tablero[2])
print(tablero[1])
print(tablero[0])

#Creamos un bucle para un jugador con nuestro checkpoint
while flag==True:
#Aqui pedimos las coordenadas
    print("Primer Jugador")
    a[0] = int(input("Ingresa la coordenada y: "))
    a[1] = int(input("Ingresa la coordenada x: "))
#Aqui hacia donde se va a mover      
    b[0] = int(input("Mover a y:"))
    b[1] = int(input("Mover a x:"))
#Aqui encontraremos la pieza la cual va a mover    
    for i in range(len(Pieza)):
#Si coincide con una    
        if tablero[a[0]][a[1]] == Pieza[i]:
#Aqui buscamos de cual pieza se trata        
            if i == 0:
#Peon  aqui esta si ingresa las cordenadas tanto del inicio como del final en x y y
                if b[0] == a[0]+1 and b[1] == a[1]:
#Aqui cree una variable para almacenar la pocision de la pieza y despues pasarla a la variable para posicionarla a otro lugar
                    T = tablero[a[0]][a[1]]                    
                    tablero[a[0]][a[1]] = tablero[b[0]][b[1]]                    
                    tablero[b[0]][b[1]] = T
#Al finalizar cada moviento se rompera el bucle y empezara con el otro jugador
                    break
            elif i == 1:
#Torre Todas las piezas tienen un codigo diferente puesto que estas se mueven diferente
                if b[0] == a[0] or b[1] == a[1]:
                    T = tablero[a[0]][a[1]]
                    tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                    tablero[b[0]][b[1]] = T
                    break

            elif i == 2:
#Caballo
                if b[0] == a[0]+1 or b[0] == a[0]-1 or b[0] == a[0]+2 or b[0] == a[0]-2:               
                    if b[1] == a[1]+2 or b[1] == a[1]-2 or b[1] == a[1]+1 or b[1] == a[1]-1:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
            elif i == 3:
#Alfil
                for i in range(8):                
                    if b[0] == a[0]+i and b[1] == a[1]+i or b[0] == a[0]-i and b[1] == a[1]-i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break                        
                    elif b[0] == b[0]+i and b[1] == a[1]-i or b[0] == a[0]-i and b[1] == a[1]+i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
            elif i == 4:
#Rey
                if b[0] == a[0] or b[0] == a[0]+1 or b[0] == a[0]-1:               
                    if b[1] == a[1] or b[1] == a[1]+1 or b[1] == a[1]-1:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
            else:
#Reina            
                for i in range(8):
                    if SET[0] == a[0] + i and b[1] == a[1] + i or b[0] == a[0] - i and b[1] == a[1] - i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
                    elif b[0] == a[0] + i and a[1] == a[1] - i or b[0] == a[0] - i and b[1] == a[1] + i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
                    elif b[0] == a[0] or b[1] == a[1]:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
#Imprimimos el tablero para saber que pieza se movio y para que elotro jugador avanze

    print(tablero[7])
    print(tablero[6])
    print(tablero[5])
    print(tablero[4])
    print(tablero[3])
    print(tablero[2])
    print(tablero[1])
    print(tablero[0])

#Aqui cambiamos de jugador, el codigo de las pezas es el mismo menos el del peon ya que estara en otra pocision
    #aqui tenemos nuestro checkpoint
    flag = False
#El codigo es el mismo solo que con diferentes parametros 

    print("Segundo Jugador")
    a[0] = int(input("Ingresa la coordenada y: "))
    a[1] = int(input("Ingresa la coordenada x: "))
      
    b[0] = int(input("Mover a y: "))
    b[1] = int(input("Mover a x: "))
    
    for i in range(len(Pieza)):
   
        if tablero[a[0]][a[1]] == Pieza[i]:
            if i == 0:
                if b[0] == a[0]-1 and b[1] == a[1]:   
                    T = tablero[a[0]][a[1]]
                    tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                    tablero[b[0]][b[1]] = T
                    break
            elif i == 1:
                if b[0] == a[0] or b[1] == a[1]:
                    T = tablero[a[0]][a[1]]
                    tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                    tablero[b[0]][b[1]] = T
                    break
            elif i == 2:
                if b[0] == a[0]+1 or b[0] == a[0]-1 or b[0] == a[0]+2 or b[0] == a[0]-2:      
                    if b[1] == a[1]+2 or b[1] == a[1]-2 or b[1] == a[1]+1 or b[1] == a[1]-1:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
            elif i == 3:
                for i in range(8):            
                    if b[0] == a[0]+ i and b[1] == a[1]+ i or b[0] == a[0]- i and b[1] == a[1]- i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break             
                    elif b[0] == b[0]+ i and b[1] == a[1]- i or b[0] == a[0]- i and b[1] == a[1]+ i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
            elif i == 4:
                if b[0] == a[0] or b[0] == a[0]+1 or b[0] == a[0]-1:
                    if b[1] == a[1] or b[1] == a[1]+1 or b[1] == a[1]-1:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
            else:   
                for i in range(8):
                    if b[0] == a[0] + i and b[1] == a[1] + i or b[0] == a[0] - i and b[1] == a[1] - i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
                    elif b[0] == a[0] + i and a[1] == a[1] - i or b[0] == a[0] - i and b[1] == a[1] + i:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break
                    elif b[0] == a[0] or b[1] == a[1]:
                        T = tablero[a[0]][a[1]]
                        tablero[a[0]][a[1]] = tablero[b[0]][b[1]]
                        tablero[b[0]][b[1]] = T
                        break

    print(tablero[7])
    print(tablero[6])
    print(tablero[5])
    print(tablero[4])
    print(tablero[3])
    print(tablero[2])
    print(tablero[1])
    print(tablero[0])
    
    
    print("Siguiente")
    flag=True
