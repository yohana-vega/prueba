"""01. Crear una lista que contenga nombres de provincias 
Argentinas, que contenga más de 5 elementos e imprimir por pantalla 
2. Imprimir por pantalla el tercer elemento de la lista 
3. Imprimir por pantalla del segundo al cuarto elemento 
4. Mostrar el tipo de dato de la lista 
5. Mostrar los primeros 4 elementos de la lista 
6. Agregar una provincia más a la lista que ya exista y otra que no. 
7. Agregar una provincia, pero en la cuarta posición."""

provincias = ["tdf", "santa cruz", "bueno aires", "cordoba", "jujuy"]
#print(provincias)

#print(provincias[3])

#print(provincias[2:5])

#print(type(provincias))

#print(provincias[0:4])

provincias.append("cordoba")
#print(provincias)

provincias.append("mendoza")
#print(provincias)

provincias.insert(4,"san juan")
#print(provincias)

provincias2 = ["chubut", "rio negro"]
provincias.extend(provincias2)
#print(provincias)

provincias.remove("tdf")
#print(provincias)

variable = provincias.pop()
#print(variable)