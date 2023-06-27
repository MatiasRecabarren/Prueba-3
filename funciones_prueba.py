import os
import time

#Funciones Para Prueba
contador = 0
import os
import time
import numpy 
lista_rut = []
lista_contador =[]
valor_dia = 15000

guarderia = numpy.zeros((2,5),int)

def validar_menu():
    os.system('cls')
    print("""MENÚ GUARDERÍA MASCOTA SEGURA
    1.Grabar
    2.Buscar
    3.Retirarse
    4.Salir
      """)

def validar_opcion():
    while True:
        try:
            opcion = int(input("Escoga una opción del Menú (1 al 4): "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! ESCOGA UNA OPCIÓN CORRECTA")
        except:
            print("ERROR! LA OPCIÓN DEBE SER UN NÚMERO ENTERO")

def validar_rut():
    os.system('cls')
    while True:
        try:
            rut = int(input("Ingrese su rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                lista_rut.append(rut)
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000  y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre del dueño: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validador_unico():#asi se me ocurre que puede haber sido pero no funciono
    #while True:
    #   if rut in (lista_rut)
    #       contador += contador
    #       print (f"Su digito verificador es {contador}")
    pass

def validar_nombre_mascota():
    while True:
        nombre = input("Ingrese nombre de la mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_dias():
    while True:
        try:
            dias = int(input("Ingrese de días que ingresara a su mascota: "))
            if dias >= 1 :
                return dias
            else:
                print("ERROR! LOS DÍAS INGRESADOS DEBEN SE MAYOR A 1")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def guardar_mascota():
    print ("        ____________")
    print ("                    ")
    print ("         GUARDERIA  ")
    print ("          MASCOTA   ")
    print ("        ____________")

    for x in range (2):
        print(f"Fila {x+1}:")
    for y in range (5):
        print (guarderia[x][y], end=" ") #Nose porque no quedo alineada con las filas
        print (" ")
    print("Columna: 1 2 3 4 5")
    while True:

        fila = input ("Eliga la columna donde estara su mascota:")
        columna = input("Eliga la columna donde estara su mascota: ")
        lugar_m = ([fila] [columna])
        if columna == 0:
            print("Su Mascota ya quedo registrada")
            return lugar_m
        else:
            print("Esa area ya esta ocupada con otra mascota")

def buscar():
    lugar_m = guardar_mascota()
    while True:
        try:
            rut=("Ingrese su rut para buscar a su mascota")
            if rut in lista_rut():
                print (f"Su mascota esta en: {lugar_m}")
            else:
                print("ERROR! EL RUT NO SE HA ENCONTRADO")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
    #Lo que se me ocurre que puede ir aqui es que gracias al validador unico
    #Se encuentre a la mascota

def retirarse():
    dias = validar_dias()
    while True:
        try:
            rut=("Ingrese su rut para retirarse")
            if rut in lista_rut():
                print (f"Su total a pagar es: {dias * valor_dia}")
                lista_rut.pop(rut)
                lista_contador.pop(contador)
                return rut
            else:
                print("ERROR! EL RUT NO SE HA ENCONTRADO")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
   