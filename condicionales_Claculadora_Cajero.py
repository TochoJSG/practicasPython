#Simulador calculadora chafaldrana
num1 = float(input("Digite numero 1->  "))
num2 = float(input("Digite numero 2->  "))
operacion = input("Digite la letra de la operacion deseada  ").upper()#funcion a Mayuscula  != lower
if 's'==operacion=='S':
    print("\nSuma es->  {:.2f}".format(n1+n2))
    elif 'r'==operacion=='R':
        #suma = num1+num2
        print("\nResta es->  {:.2f}".format(n1-n2))
        elif 'm'==operacion=='M':
            #resta = n1-n2
            print("\nMultiplicacion es->  {:.2f}".format(n1*n2))
            elif 'd'==operacion=='D':
                div = n1/n2
                print(f"\nDivision es->  {div:.2f}")
                    #elif 'p'==operacion=='P':
                      #  print("Potencia es->  {:.2f}".format(n1**n2))
                      else: 
                        print("\nError")
#Switch no existe en Python; Simulacion de cajero
saldo = 1000
print("\t.:Cajero:.")
print("1.Ingresar dinero a la cuenta")
print("2.Retirar dinero")
print("3.Mostrar saldo")
print("4.Salir")
opcion = int(input("Ingrese opcion->  "))
print()
if opcion==1:
    deposito = int(input("Digite monto de deposito->  "))
    saldo += deposito
    elif opcion==2:
        retiro = int(input("Digite monto a retirar->  "))
        if retiro>saldo:
            print("El monto excede el saldo")
            else:
                saldo -= retiro
        elif opcion==3:
            print("Su saldo es de {}"format(saldo))
            elif opcion==4:
                print("Gracias por confiar en nosotros, good bya perro")
                else:
                    print("Error, opcion inexistente")
get = char(input("System pause"))