import time

#Importa los modulos a utilizar, uno por cada programa del proyecto final.
from cuadratic_formula import cuadratic_formula, matmult, matinv
from Collatz import collatz
from tiro_parabolico import this_tiro_parabolico
from data_base import data_base

#Cargar instrucciones, el readme y la secuencia de inicio
with open('sources/inicio.txt', 'r', encoding='utf-8') as archivo:
    inicio = archivo.read()
with open('sources/instrucciones.txt', 'r', encoding='utf-8') as archivo:
    instrucciones = archivo.read()
with open('readme.txt', 'r', encoding='utf-8') as archivo:
    readme = archivo.read()

#Define funciones para usar cada uno de los modulos importados
def numero_2():
    """Sucesion de Collatz.
    A partir de este modoulo se ejecuta 
    """
    while True:
        k = input("Calcula la sucesion de collatz de un numero natural.\n ingresa un numero natural o pulsa x para salir\n") 
        if k != "x":
            result = collatz(k)
            try:
                for i in range (0,len(result)):
                    print(f"a_{i} = {result[i]}")
                    time.sleep(0.09)
            except Exception:
                pass
            time.sleep(1)
        else:
            break
        
def numero_1():    
    while True:
        print("bienvendio al programa de tiro parabolicos, \n presiona cualquier tecla si quieres calcular el tiro parabolico con condiciones iniciales, pulsa x para salir")
        try: 
            index=input("")
            if index != "x":
                print("cargando tiro parabólico...")
                this_tiro_parabolico() #Ejercicio uno
            elif index == "x":
                print("Finalizando procesos")
                break
            else:
                print("Ingresa una entrada válida")
        except ValueError: 
            print("Ingresa una entrada válida")

def numero_3():
	print("Base de datos horario de alumnos")
	while True:
		data_base()
		select = input("pulsa n para salir, y para repetir \n")
		match select:
			case "y":
				pass
			case "n":
				break

#inicia el codigo principal
def main():
    dic = {1:numero_1, 2:numero_2,3:numero_3}
    for line in inicio.splitlines():
        print(f"\033[93m{line}\033[0m")
        time.sleep(0.05)
    while True:
        try:
            dic[int(input ("selecciona tu modo \n 1: Tiro Parabolico \n 2: Sucesion de Collatz \n 3: Base de datos\n 9: Salir \n"))]()
        except KeyError:
            print ("hasta la vista, baby")
            break
        except Exception:
            print ("error, vuelve a intentarlo")

if __name__ == "__main__":
    main()