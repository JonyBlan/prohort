def error(code):
    print("ERROR CODE " + str(code))
    exit()

def final(msg):
    print(msg)
    print("continue para borrar los datos")
    exit()

# Variables que vendrian del programa
# El orden de estos objetos es [[disponibilidadBloque1, disponibilidadBloque2, disponibilidadBloque3][same]]. Cada uno es un curso
curso  = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
profesor  = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
aula  = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# el orden de los bloques es [[(numBloque, (id)curso, (id)profesor, (id)aula][same]]. Cada uno es un bloque

# Variables que deberian estar ingresadas por el usuario
maxBloquesDia = [[5, 5, 5, 5, 5, -1, -1], [5, 5, 5, 5, 5, -1, -1], [5, 5, 5, 5, 5, -1, -1]] # falta automatizar por cantidad de cursos
minBloquesDia = [[3, 3, 3, 3, 3, -1, -1], [3, 3, 3, 3, 3, -1, -1], [3, 3, 3, 3, 3, -1, -1]] # falta automatizar por cantidad de cursos
bloquesDiaReal = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] # falta automatizar por cantidad de cursos
faltanBloques = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]] # falta automatizar por cantidad de cursos
cantBloquesReal = [20, 20, 20]  # falta automatizar por cantidad de cursos
cantBloquesOcupados = [0, 0, 0]  # falta automatizar por cantidad de cursos
# horarioEntrada va del -2 a maxBloquesDia, hay 14 valores y representan el bloque de entrada minimo y maximo por dia. -1 indica que ese dia no hay clase, -2 que es cualquier horario (siempre que de resultados), y x>=0 los bloquesAux
horarioEntrada = [[[2, 2], [0, 0], [0, 0], [0, 0], [0, 0], [-1, -1], [-1, -1]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1, -1], [-1, -1]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1, -1], [-1, -1]]]  # falta automatizar por cantidad de cursos y dias

# Variables que se llenan acorde al usuario
# bloquesxDia va del -3 al 7 inclusive: -3 significa que ya fue asignado, -2 significa que no hay clase en todo el dia, -1 significa que en ese bloque no hay clase, 0 que todavia no fue asignado (no deberia quedar ninguno cuando finaliza la ejecucion), y del 1 al 7 la prioridad de llenar el bloque
bloquesxDia = []
bloquesAux = []
diasSemana = len(maxBloquesDia[0])
cantCursos = len(curso)

# Aca empieza la logica
maxBloques = 0
maxCantBloques = 0
diasSemanaEscuela = 0
for numCurso in range(cantCursos):
    for i in range(diasSemana):
        if maxBloquesDia[numCurso][i] != -1:
            diasSemanaEscuela = diasSemanaEscuela + 1
            if(maxBloquesDia[numCurso][i] > maxCantBloques):
                maxCantBloques = maxBloquesDia[numCurso][i]

cantBloques = maxCantBloques*diasSemanaEscuela

for b in range(cantCursos):
    bloquesxDia.append([])
    for i in range(diasSemana):
        for a in range(maxCantBloques):
            bloquesxDia[b].append(0)

for cursooo in range(cantCursos):
    for i in range(diasSemana):
        if(maxBloquesDia[cursooo][i] == -1):
            faltanBloques[cursooo][i] = -1

for idCurso in range(cantCursos):
    for diaSemana in range(diasSemana):
        if(maxBloquesDia[idCurso][diaSemana] - minBloquesDia[idCurso][diaSemana] < 0):
            error(10)
        elif((maxBloquesDia[idCurso] == -1 and minBloquesDia[idCurso] != -1) or (maxBloquesDia[idCurso] != -1 and minBloquesDia[idCurso] == -1)):
            error(11)
        elif(horarioEntrada[idCurso][diaSemana][1] - horarioEntrada[idCurso][diaSemana][0] < 0):
            error(12)
        elif(maxBloquesDia[idCurso][diaSemana] - minBloquesDia[idCurso][diaSemana]) < horarioEntrada[idCurso][diaSemana][0]:
            error(9)
        elif(horarioEntrada[idCurso][diaSemana][0] >= 0 and maxBloquesDia[idCurso][diaSemana] >= 0):
            #for numCurso in range(cantCursos):
                if(maxBloquesDia[idCurso][diaSemana] != -1):
                    for hora in range(horarioEntrada[idCurso][diaSemana][0]):
                        bloquesxDia[idCurso][diaSemana*5+hora] = -1
                if(maxBloquesDia[idCurso][diaSemana] - horarioEntrada[idCurso][diaSemana][0] == minBloquesDia[idCurso][diaSemana]):
                    for hora in range(horarioEntrada[idCurso][diaSemana][0], maxCantBloques):
                        bloquesxDia[idCurso][hora+5*diaSemana] = 7
        elif(maxBloquesDia[idCurso][diaSemana] == -1):
            #for numCurso in range(cantCursos):
                for bloque in range(maxCantBloques):
                    bloquesxDia[idCurso][bloque+5*diaSemana] = -2
        else:
            error(13)

def checkearDisponibilidad(disponibilidad, numBloque, numArray, idLlamador):
    if(disponibilidad[numBloque] == 1 or disponibilidad[numBloque] == "1"):
        return True
    elif(disponibilidad[numBloque] == 0 or disponibilidad[numBloque] == "0"):
        return False

def forzarBloque(numBloque, idCurso, idProfesor, idAula):
    if(curso[idCurso][numBloque] == 0 or profesor[idProfesor][numBloque] == 0 or aula[idAula][numBloque] == 0):
        error(8)
    else:
        bloquesAux.append([numBloque, idCurso, idProfesor, idAula])
        curso[idCurso][numBloque] = 0
        profesor[idProfesor][numBloque] = 0
        aula[idAula][numBloque] = 0

#bloquesOcupados = 0

#               for dia in range(diasSemana):
#                    if(minBloquesDia[numCurso][dia] != -1):
#                        minBloques = minBloques + minBloquesDia[numCurso][dia]
#                    if(faltanBloques[numCurso][dia] == 1):
#                        diaFalta = dia
#                        libre = False
#                if(libre == False):
#                    for bloques in range(maxCantBloques):
#                        if(bloquesDiaReal[numCurso][bloques] == 0):
#                            numBloque = bloques+diaFalta*maxCantBloques
#                            break
#                else:


def llenarBloque(vuelta):
    for numCurso in range(cantCursos):
        if(cantBloquesOcupados[numCurso] < cantBloquesReal[numCurso]):
            numBloque = 0
            minBloques = 0
            bloqueFalta = -1
            diaFalta = -1
            libre = True
            for preNumBloque in range(cantBloques):
                numBloque = preNumBloque
                if(bloquesxDia[numCurso][numBloque] >= 0):
                    idCurso = 0
                    for idCurso in range(len(curso)):
                        #if(bloquesxDia[numBloque] > 0):
                            if(checkearDisponibilidad(curso[idCurso], numBloque, idCurso, 0)):
                                idProfesor = 0
                                for idProfesor in range(len(profesor)):
                                    if(checkearDisponibilidad(profesor[idProfesor], numBloque, idProfesor, 1)):
                                        idAula = 0
                                        for idAula in range(len(aula)):
                                            if(checkearDisponibilidad(aula[idAula], numBloque, idAula, 2)):
                                                curso[idCurso][numBloque] = 0
                                                profesor[idProfesor][numBloque] = 0
                                                aula[idAula][numBloque] = 0
                                                bloquesAux.append([numBloque, idCurso, idProfesor, idAula])
                                                bloquesxDia[numCurso][numBloque] = -3
                                                cantBloquesOcupados[numCurso] = cantBloquesOcupados[numCurso] + 1
                                                bloquesDiaReal[numCurso][int(numBloque/maxCantBloques)] = bloquesDiaReal[numCurso][int(numBloque/maxCantBloques)] + 1
                                                #bloquesOcupados = bloquesOcupados + 1
                                                #if bloquesOcupados == cantBloques:
                                                    #print("Se llenaron todos los bloques correctamente")
                                                    #exit()
                                                print("Bloque completo: " + str(bloquesAux[vuelta]))
                                                return 1
        else:
            todosContados = True
            for i in range(cantCursos):
                if(cantBloquesOcupados[i] != 20):
                    todosContados = False
            if(todosContados == True):
                for numCurso in range(cantCursos):
                    for numBloque in range(len(bloquesxDia[numCurso])):
                        if(bloquesxDia[numCurso][numBloque] == 0):
                            bloquesxDia[numCurso][numBloque] = -4
                print(bloquesxDia)
                print(bloquesDiaReal)
                final("se llenaron todos los bloques")
    print(bloquesxDia)
    error(4)

def llenarBloques():
    vueltas = -1
    if vueltas != -1:
        for i in range(vueltas):
            llenarBloque(i)
    else:
        i = 0
        while True:
            llenarBloque(i)
            i = i + 1
    print("Llego al final. Continuar para borrar datos")
    print("")

llenarBloques()