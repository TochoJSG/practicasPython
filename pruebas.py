#Operadores Relacionales
resultado1 = 10 < 20
resultado2 = 10 > 11
a = 15
b = 20
c = 40
d = 35
e = a+b
print(resultado1)
print(resultado2)
print(e == c)
print(a+b == e)

#Salidas
nombre1 = "Jorge"
edad1 = 21
nombre2 = "Valeria"
edad2 = 16
print("Hola",nombre1,"tienes",edad1)
print("Hola {} tienes {} edad".format(nombre2,edad2))
print(f"Hola {nombre1} tienes {edad2} anios")#Ultima version

#Resolver expresion algebraica " (a3 * (b2 - 2*ac))/2*b "
print("Resolucion de la expresion (a3 * (b2 - 2*ac))/2*b ")
a = float(input("a-> "))
b = float(input("b-> "))
c = float(input("c-> "))
x = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"Resultado:  {x}")
#Leer Radio y calcular Area y Circunferencia
import math
radio = float(input("Radio->  "))
pii = 3.14159
areaC = pii * (radio*radio)
areaCC = math.pi * radio**2
peri = 2 *pii * radio
periCC = 2 * math.pi *radio
print(f"Area es de:  {areaC}")
print("Area con el modulo 'math': {:.8f} perimetro con modulo 'math': {:.5f}".format(areaCC,periCC))
print("Resultado es de area :{} y el perimetro: {}".format(areaC,peri))
#Descuento en tienda de 15% sobre total de coompra, saber monto final a pagar
base = float(input("Cual es el precio del producto:  "))
descuento = base * 0.15
precio = base / 1.15
print("Al producto de {base} luego de un descuento de {descuento}...".format(base,descuento))
print(f"El precio luego de descuento es de:  {precio}")
p = int(input("system pause "))