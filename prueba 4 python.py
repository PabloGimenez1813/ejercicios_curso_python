#aqui utilizamos en un bucle for la sentencia continue para evitar contar 
#el espacio en blanco la de la variable de la cual queremos contar la 
#cantidad de caracteres

nombre= "pildoras informaticas"
contador=0
for i in nombre:
    if i==" ":
        continue;
    contador+=1
print(contador)