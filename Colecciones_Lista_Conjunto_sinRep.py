#Con lista, eliminar elementos repetidos, luego mostrarlos
lista = [1,2,3,7,2,2,1,1,8,3]
conjunto = set(lista) #Metodo 'set() diferencia conjuntos; En conjuntos no pueden haber elementos repetidos
print("Esta es la lista original-> {}".format(lista))
print("Este es conjunto depurado-> {}\n".format(conjunto))
print("Conjunto no  respeta orden, por lo tanto \n convertimos conjunto depurado a lista\n con funcion 'list()'")
#listaa = list(conjunto)
listaa = list(set(lista))#podemos hacer en una sola linea: de lista depurar elementos repetidos con conjuntos, luego conjunto volverlo lista
print(listaa)
#Lista metodos
lista1 = [1,2,3,"Valecita","Chaparrita",[1,2,3],'x']
print("Iniciamos lista con {} elemetos-> {}".format(len(lista1),lista1))#Longitud de lista
lista1.append("Jorge")
print("Ahora tenemos {} elementos-> ".format(len(lista1),lista1))
lista1.insert(3,"Jorge")#2parametros, donde poner que->indice, que
lista1.insert(4,"monta")
lista1.insert(5,"a")
lista1.insert(7,"y a la")
lista1.extend(["batiendoles","asi","sus","ricos","culos"])
print(lista1)
print("Ahora tenemos {} elementos-> {}".format(len(lista1),lista1))
print("La lista inicial es de {}-> {}".format(len(listaa),listaa))
listaa.insert(3,4)
listaa.insert(4,5)
listaa.insert(5,6)
listaa.extend([9,10,11,12])
lista3 = [13,14,15,16,17,18,19,20]
lista2 = listaa+lista3
print("La lista1 es {} y la lista 2 es {} ".format(listaa,lista3))
print(f"Al juntarlas queda-> {lista2}")
print(10 in lista2)#busqueda? TRUE : FALSE
print(lista2.index(10))#indice de elemento buscado
print(lista.count(1))#Cuenta veces de aparicion de elemento en lista
print(lista2.count(7))
lista2.pop()#Elimina por defecto ultimo elemento de la lista, pudiendo pasar parametro de indice
lista2.pop(5)
lista2.remove(10)#En caso de no saber indice de elemento, se pasa valor
print(lista2)
lista2.reverse()
print(lista2)
lista2 *2
print(lista2)
lista2.append(-7)
lista2.extend([-1,22,33,70])
print(lista2)
lista2.sort()#Orden ascendentemente
print(lista2)
lista2.sort(reverse=True)
print(lista2)
lista2.clear()#vacia la lista
x = int(input("system paused"))
