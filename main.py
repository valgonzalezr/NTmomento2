from Ciclista import Ciclista

def menu():
    return int(input(
"""
-------------- MENU ------------
1. ingresar ciclista
2. mostrar ciclista con mejor tiempo
3. salir
"""
    ))

def agg():
    ciclista={
        'name': input('nombre: '),  
        'age':int(input('edad: ')),
        'country':input('pais: '),
        'time':float(input('time: '))  
    }
    return ciclista

def mejor_ciclista(ciclistas):

    mejor=None
    posicion=0
    if len(ciclistas) != 0:
        for ciclista in ciclistas:
            if mejor==None:
                mejor=ciclista.time
                posicion=ciclistas.index(ciclista)
            elif ciclista.time < mejor:
                mejor=ciclista.time
                posicion=ciclistas.index(ciclista)
        return posicion
    return print("No hay ningun ciclista")

ciclistas=[]
salir=False

while not salir:
    opcion=menu()
    if opcion==1:
        ciclista=agg()
        ciclistas.append(Ciclista())
        ciclistas[-1].name=ciclista['name']
        ciclistas[-1].age=ciclista['age']
        ciclistas[-1].country=ciclista['country']
        ciclistas[-1].time=ciclista['time']
    elif opcion==2:
        posicion=mejor_ciclista(ciclistas)
        print(
f"""
nombre: {ciclistas[posicion].name}
edad: {ciclistas[posicion].age}
pais: {ciclistas[posicion].country}
time: {ciclistas[posicion].time}
"""
        )
    elif opcion==3:
        salir=1
    
    else:
        print("Opcion incorrecta") 
