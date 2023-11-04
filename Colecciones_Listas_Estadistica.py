#Programa con 2 listas y crear las suguientes listas
#Elementos de ambas lista; Solo elementos de primera; De segunda, no en primera; Elementos en comun de ambas listas, repetidos
lista1 = [1,2,3,4,5,4,3,2,1]
lista2 = [4,5,1,2,9,6,9,8,7]
a = set(lista1)#Eliminamos elementos repetidos voliviendo lista conjunto
b = set(lista2)
union = list(a | b) #Simbolo '|' es union, como en estadistica, une elementos de estructuras
soloA = list(a-b)
soloB = list(b-a)
intersection  = list(a & b)
print("Lista A ->  {}".format(a))
print("Lista B ->  {}\n\n".format(b))
print(f"Elementos de ambas listas -> {union}")
print(f"Elemento de primera lista, Solo A ->{soloA}")
print(f"Elemento de segunda lista, Solo B ->{soloB}")
print(f"Elemento de amabs listas, Interseccion ->{intersection}")
#Conjuntos
#a = set() -> Conjunto vacio, posteriormente agregar elemetnos con funcion add(#) {comas entre elementos vuelve cinjunto}; no importa orden solo elemetos
#a = {} Diccionario; 
a = frozenset({1,2,3,4})#inputable, no se puede modificar
b = {3,4,5,6,7,8}
c = {2,4,1,3,4,5,8}
d = a | b
print("Conjunto A tiene {} elemetos -> {}".format(len(a),a))
print("Conjunto B tiene {} elementos-> {}".format(len(b),b))
print("Conjunto C tiene {} elementos-> {}".format(len(c),c))
print("a=b?-> {}".format(a == b))#iguladad entre conjuntos
print("a=c?-> {}".format(a == c))
print("A union B-> {}".format(d))
d = a & b
print("A interseccion B-> {}".format(d))
d = b - a
print("Elementos solo de B, que no tiene A-> {}".format(d))
d = a - b
print("Elementos solo de A, que no tiene B-> {}".format(d))
print("Es A subconjunto de C?-> {}".format(a.issubset(c)))#Es A subconjunto de B?
print("Es B subconjunto de C?-> {}".format(b.issubset(c)))#Deben estar todos los elementos
print("Es C suoer conjunto de A?-> {}".format(c.issuperset(a)))#SuperConjunto contiene todos los elementos
print("Es A y B completamente diferentes, no comparten algun elemento->".format(a.isdisjoint(b)))#Disconexos: No comparten algun elemento, completamente diferentes
print("A es inmutable por funcion 'frozenst()',pero a B se le pueden agragar elementos, [2,9,1]'")
b.add(2)
b.add(9)
b.add(1)
print(f"B quedo asi-> {b}\n\n")
#Diccionarios; Elemetos desordenados, como en listas; 2 elementos por posicion(Clave:Valor), donde clave no puede ser repetida
diccionario = {"azul":"blue","rojo":"red","verde":"green"}#diccionario vacio; Elemento1, Elemento2,... ElementoN
print(diccionario)
print(diccionario["azul"])
print(diccionario["rojo"])
diccionario["amarillo"] = "yellow"#Agregamos, primero clave, luego valor
print(diccionario)#Son desordenados
diccionario["azul"] = "BLUE"#Modificamos valor de azul
print(diccionario)
del(diccionario["azul"])
print(diccionario)
#puede haber diccionarios complejos con listas, tuplas, incluso otros diccionarios
dicc = {"Jorge":[22,1.80],"Leo":[23,1.85],"Natalia":[16,1.55]}#Clave:Valor es lista
dicc1 = {"Jor":{"edad":21,"estatura":1.80,"carrera":"infomatica"},"Nat":{"edad":16,"estatura":1.55,"carrera":"Estudiante"}}
print(dicc["Natalia"])
print(dicc1["Jor"])

#Practica de diccionario con Personajes
print("\n\nEjemplo de diccionario con personajes")
personajes = []#Creacion lista vacia
dias = ["lunes","martes","miercoles","jueves","viernes"]
p = {"Nombre":"Tony Montana","Clase":"Empresario","Raza":"Caribenio"}
personajes.append(p)#Agregamos a lista el personaje creado
p = {"Nombre":"Cochiloco","Clase":"Traficante","Raza":"Latina"}
personajes.append(p)
p = {"Nombre":"Shindler","Clase":"Fabricante","Raza":"Aria"}
personajes.append(p)#Metodo append agrega al fila, Pila
print("Personajes: {}".format(personajes))
#Repaso listas 
print("personajes, el segundo",personajes[1])
print(dias)
print("dia mnos uno",dias[-1])
print("dias, de el primero al tercero",dias[0:3])
print("dia 4",dias[3])
x = int(input("System Paused"))