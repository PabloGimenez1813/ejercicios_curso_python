def suma(opc1,opc2):
    return opc1+opc2

def resta(opc1,opc2):
    return opc1-opc2

def multiplicacion(opc1,opc2):
    return opc1*opc2

def division(opc1,opc2):
    return opc1/opc2

opc1= (int(input('ingrese el primer numero:')))
opc2= (int(input('ingrese el segundo numero:')))

operacion=input('ingrese operacion que desea realizar--- (suma,resta,multiplicar,dividir):  ')

if operacion=='suma':
    print(suma(opc1,opc2))
    
elif operacion=='resta':
    print(resta(opc1,opc2))
    
elif operacion =='multiplicar':
    print(multiplicacion(opc1,opc2))

elif operacion== 'dividir':
    print(division(opc1,opc2))
    
else: print('operacion no contemplada')

print('operacion exitosa.continua el programa.')    