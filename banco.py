from Cliente import Cliente
from Cuenta import Cuenta

print("Banco de hierro de la isla de Braavos")

nombre=input("Nombre: ")
apellido=input("Apellido: ")
cedula=input("Cedula: ")
ciudad=input("Ciudad: ")
numero_cuenta=input("Numero de cuenta: ")
saldo=float(input("Saldo: "))
cliente=Cliente(nombre, apellido, cedula, ciudad)
cuenta=Cuenta(numero_cuenta,saldo)

print("1. consultar saldo")
print("2. retirar dinero")
print("3. ingresar dinero")
print("4. Salir")

def menu():
    return int(input("Digite la opcion: "))
def retirar(retirar):
    total=cuenta.get_saldo()-retirar
    cuenta.set_saldo(total)

def ingresar(ingresar):
    total=cuenta.get_saldo()+ingresar
    cuenta.set_saldo(total)


salir=False
while not salir:
    opcion=menu()
    if opcion==1:
        print(f"Su saldo es de  {cuenta.get_saldo()}")
    elif opcion==2:
        valorRetiro=float(input("Cantidad de dinero a retirar: "))
        if (valorRetiro > cuenta.get_saldo() ):
            print("Sorry el banco no le va a prestar se quebro")
        else:
           retirar(valorRetiro)
           
    elif opcion==3:
        i=float(input("Cantidad de dinero a ingresar: "))
        ingresar(i)
    elif opcion==4:
        salir=1
    else:
        print("Esta no es una opcion correcta")
    
