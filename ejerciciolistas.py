hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

reemplazo= int (input("ingrese el numero a reemplazar: "))
while reemplazo == hat_list[2]:
    if True:reemplazo= int (input("ingrese otro numero: "))
else:
    hat_list[2]=reemplazo
    hat_list.pop(-1)
    print("longitud de la lista ahora: ", len(hat_list))
        

print(hat_list)
