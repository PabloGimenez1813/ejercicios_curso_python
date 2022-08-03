# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) 
# que se puede describir de la siguiente manera:

# Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
# Si es par, evalúa un nuevo c0 como c0 Ã· 2.
# De lo contrario, si es impar, evalúe un nuevo  c0  como 3 Ã c0 + 1.
# Si c0 â  1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.


c0 = int (input("ingresa un numero entero: "))
contador=0
while c0 >=1:
    
    if c0 ==1:
        break;
    if c0 % 2==0:
        c0=c0 //2
    else:
        c0=(c0 * 3) +1
    contador+=1    
    print("Resultado: ", c0) 
else:
    print("no arroja resultados con ", c0)
    
print("numero de paso: ", contador)
