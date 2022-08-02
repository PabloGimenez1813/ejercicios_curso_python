import math
print("programa de calculo de raiz cuadrada")
numero= int(input("introduce un numero: "))
intentos=0
while numero <0:
    print("no se puede hallar la raiz de un numero negativo")
    
    if intentos==2:
        print("has consumido demasiados intentos. el programa finalizo.")
        break;
    numero= int(input("introduce un numero: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print("la raiz cuadrada de "+ str(numero)+"es"+ str(solucion))