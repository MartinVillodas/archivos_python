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
    cantidad_lineas = 0
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

    for linea in fi:
        cantidad_lineas_fo = 0
        fo.writelines(linea)
        cantidad_lineas_fo += contar_lineas(fo)

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

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    ej2()
    #ej3()
    #ej4()
    #ej5()
