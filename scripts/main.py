import time



#Importa los modulos a utilizar, uno por cada programa del proyecto final.

#bloque A
from Collatz import collatz
from tiro_parabolico import main as tiro_parabolico
from data_base import data_base
#bloque B
from curp import main as curp
from cuadratic_formula import main as cuadratic_formula
#bloque C
from matrices import matrixinv, matrixmult



#Define funciones para usar cada uno de los modulos importados siguiendo una estructura similar

#funciones del bloque A
def numero_1():
    """Tiro parabolico.
    Programa para calcular tiros parabolicos
    """
    print("bienvendio al programa de tiro parabolicos")
    
    while True:
        tiro_parabolico()
        salir = input("pulsa n para salir, y para repetir \n")
        match salir:
            case "y":
                pass
            case "n":
                break

def numero_2():
    """Sucesion de Collatz.
    A partir de esta funcion se puede calcular la sucesion de collatz de un numero hasta llegar al 1.
    """
    print("Calcula la sucesion de collatz de un numero natural.")
    
    while True:
        salir = input("ingresa un numero natural o pulsa x para salir\n")
        match salir:
            case "x":
                break
            case _:
                result = collatz(salir)
                #imprime la sucesion en forma de funcion f(i) = a_i con sleeps para que haya tiempo de leer
                for i in range (0,len(result)):
                    print(f"a_{i} = {result[i]}")
                    time.sleep(0.09)
                time.sleep(1)
                
        
def numero_3():
    """Base de datos.
    crea una base de datos para los alumnos
    """
    print("Base de datos horario de alumnos")
    
    while True:
        data_base()
        salir = input("pulsa n para salir, y para repetir \n")
        match salir:
            case "y":
                pass
            case "n":
                break

#funciones del bloque B
def numero_4():
    """CURP.
    funcion para sacar el curp de cualquier ciudadano
    """
    print("Generador de curp")
    
    while True:
        curp()
        salir = input("pulsa n para salir, y para repetir \n")
        match salir:
            case "y":
                pass
            case "n":
                break

def numero_5():
    """Formula cuadratica.
    funcion para sacar las raices de una ecuacion de segundo grado:
    """
    print("Formula cuadratica")

    while True:
        cuadratic_formula()
        salir = input("pulsa n para salir, y para repetir \n")
        match salir:
            case "y":
                pass
            case "n":
                break


#funciones del bloque C
def numero_6():
    """Multiplicacion de matrices 3x3.
    funcion para multiplicar matrices a partir de inputs del usuario:
    """
    print("Multiplicacion de matrices 3x3")

    while True:
        matrixmult()
        salir = input("pulsa n para salir, y para repetir \n")
        match salir:
            case "y":
                pass
            case "n":
                break

def numero_7():
    """Inversa de matriz 3x3.
    funcion para sacar la inversa de una matriz a partir de inputs del usuario:
    """
    print("Inversa de matriz 3x3")

    while True:
        matrixinv()
        salir = input("pulsa n para salir, y para repetir \n")
        match salir:
            case "y":
                pass
            case "n":
                break


#inicia el codigo principal
def main():
    
    #Carga instrucciones, el readme y la secuencia de inicio de la carpeta de recursos usando la funcion open
    with open('sources/inicio.txt', 'r', encoding='utf-8') as archivo:
        secuencia_inicio = archivo.read()
    with open('sources/instrucciones.txt', 'r', encoding='utf-8') as archivo:
        instrucciones = archivo.read()
    with open('readme.txt', 'r', encoding='utf-8') as archivo:
        readme = archivo.read()

    
    
    #inicia un diccionario con las funciones definidas anteriormente para poder ser seleccionadas en el menu de inicio
    dic = {1:numero_1, 2:numero_2,3:numero_3,4:numero_4,5:numero_5,6:numero_6,7:numero_7}
    
    #Imprime la secuencia de inicio usando el metodo splitlines, osea que imprime las filas una a una cada 0.05 segundos
    for line in secuencia_inicio.splitlines():
        print(f"\033[93m{line}\033[0m")
        time.sleep(0.05)
        
    #Inicia el bucle principal, con el menu de inicio, sistema anti errores y una forma de salir       
    while True:
        
        try:
            menu_selector = int(input ("selecciona tu modo \n 0: Ayuda \n 1: Tiro Parabolico \n 2: Sucesion de Collatz \n 3: Base de datos \n 4: Curp \n 5: formula cuadratica \n 6: Multiplicacion de matrices 3x3 \n 7: Inversa de matriz 3x3 \n 8: Salir \n 9: Sobre el programa \n"))
            
            
            match menu_selector:
                case 0:
                    print(instrucciones)
                    input("presiona cualquier tecla para continuar")
                
                case 8:
                    #finalizar el codigo    
                    print ("hasta la vista, baby")
                    break

                case 9:
                    print(readme)
                    input("presiona cualquier tecla para continuar")
                    

                case _:
                    #empezar funcion seleccionada
                    dic[menu_selector]()
                    
        except Exception as e:
            print ("Error, vuelve a intentarlo.", e)
            time.sleep(1)


#iniciar el codigo
if __name__ == "__main__":
    main()