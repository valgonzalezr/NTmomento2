#funcion lambda

mayor = lambda num1,num2 : 1 if (num1 > num2 ) else -1
imprimir= lambda valor :"El primer número es mayor" if (valor==1) else "el segundo número es mayor"

valor=(mayor(5,6))
print(imprimir(valor))