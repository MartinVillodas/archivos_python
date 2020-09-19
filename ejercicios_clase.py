#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Martin Villodas"
__email__ = "martinvillodas@gmail.com"
__version__ = "1.2"

import csv
import re

def contar_lineas(nombre):
    cantidad_lineas = 0
    for linea in nombre:
        cantidad_lineas += 1
    return cantidad_lineas


def ej1():
    # Ejercicios con archivos txt

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    with open("notas.txt","r") as fi:
        print(contar_lineas(fi))


def ej2():
    # Ejercicios con archivos txt
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''
    fi = open("notas.txt","r")
    fo = open("copia_nota.txt","w")

    cantidad_lineas_fo = 0

    for linea in fi:
        fo.writelines(linea)
        cantidad_lineas_fo += 1
    print("Se copiaron {} lineas al archivo copia_nota".format(cantidad_lineas_fo))

    fi.close()
    fo.close()

    # Recuerde cerrar los archivos al final ;)


def ej3():
    # Ejercicios con archivos CSV
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    archivo = 'propiedades.csv'
    with open(archivo,"r") as propiedades:
        data = list(csv.DictReader(propiedades))

        cantidad_filas = len(data)
        cantidad_2_ambiente = 0
        cantidad_3_ambiente = 0

        for i in range(cantidad_filas):
            valor = data[i]["ambientes"]
            if valor == "2":
                cantidad_2_ambiente += 1
            elif valor == "3":
                cantidad_3_ambiente += 1
        print("La cantidad de departamentos 2 ambientes es {}".format(cantidad_2_ambiente))
        print("La cantidad de departamentos 3 ambientes es {}".format(cantidad_3_ambiente))


def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}
    fruta_verdura = 'manzanas'
    stock = 0

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"
    '''

    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    while True:
        print("El inventario de frutas/verduras actualmeten es:", inventario)
        fruta = str(input("Ingrese el nombre de una fruta/verdura o la palabra fin para salir:\n"))

        if fruta == "fin":
            break
        else:
            cantidad = int(input("Ingrese la cantidad, de la fruta que eligio, que desea agregar:\n"))
            inventario[fruta] = cantidad

def ej5():
    # Ejercicios con archivos CSV
    inventario = {'Fruta Verdura': 'manzana', 'Cantidad': 10}
    gondola = {}
    nombre_archivo = 'inventario.csv'
    header = ['Fruta Verdura', 'Cantidad']
    fruta_verdura = ''

    '''
    Parecido al ejercicio anterior: genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'
    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:
    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})
    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.
    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"
    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    with open(nombre_archivo, "w", newline="") as fo:
        writer = csv.DictWriter(fo, fieldnames=header)
        writer.writeheader()

        while True:
            print("El inventario de frutas/verduras actualmeten es:", inventario)
            fruta = str(input("Ingrese el nombre de una fruta/verdura o la palabra fin para salir:\n"))
            
            if fruta == "fin":
                break
            else:
                cantidad = int(input("Ingrese la cantidad, de la fruta que eligio, que desea agregar:\n"))
                inventario[fruta] = cantidad
                writer.writerow({"Fruta Verdura":fruta, "Cantidad":cantidad})

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
