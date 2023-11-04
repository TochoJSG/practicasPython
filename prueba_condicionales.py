#Condicionales combinados
edad = int(input("Digite su edad->  "))
if 0<edad<100#if edad>0 and edad<100
    print("La edad {} es valida".format(edad))
    if(edad>17)
        print("Es muy grande")
        else
            print("Edad incorrecta")
#Condicionales: Ejercicio 1: Programa que pida 2 numeros y se de cuenta cual es par o si ambos lo son
n1 = int(input("De numero 1:  "))
n2 = int(input("De numero 2:  "))
if n1%2==0 and n2%2==0:
print("Ambos numeros son pares")
    elif n1%2==0 and n2!=0:
    print("El numero 1 es par, el otro no")
        elif n1%2!=0 and n2%2==0:
        print("El primero es impar, el seguundo es par")
            else:
            print("Ninguno es par")
#Condicionales: Ejercicio 2: Programa que pida 3 numeros y determine cual es el mayor
cont = 0
num1 = int(input("De numero:  "))
num2 = int(input("De numero 2:  "))
num3 = int(input("De numero 3:  "))
#if num1>=num2 and num1>=num3:
#if num2>=num1 and num2>=num3:
if num2<num1>num3:
    print(f"El numero 1 '{num1}' es el mayor")
    elif num1<num2>num3:
        print("El numero 2 '{}' es el mayor".format(num2))
        elif num1==num2 and num2==num3:
            print("Todos son iguales")
            elif num1==num2 and num1>num3:
                print("Numero 1 y 2 son iguales y mayores'{}'".format(num1))
                elif num1==num3 and num1<num2:
                    print(f"Numero 1 y 3 son iguales '{}', y menores al segundo '{num3}'")
                    elif num2==num3 and num2<num1:
                        print("Numero 2 y 3 son iguales '{}' y el primero es mayor '{}'".format(num2,n3))
                        elif num1==num2 and num1<num3:
                            print("Numero 3 '{}' es mayor, los otros son iguales '{}'".format(num3,num1))
                                elif num1==num3 and num1<num2:
                                    print(f"Numero 1 y 3 son iguales '{}', y menores al segundo '{num3}'")
                                    elif num2==num3 and num2<num1:
                                        print("Numero 2 y 3 son iguales '{}' y el primero es mayor '{}'".format(num2,n3))
            else:
            print("El numero 3'{}' es el mayor".format(num3))
z = float(input("system pause "))
