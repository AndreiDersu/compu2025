from math import *
import numpy as np
import matplotlib.pyplot as plt

def graficadora(
    v:float,
    ang:float
    ):
    """Grafica de tiros parabolicos de posicion contra posicion

    Args:
        v (float): velocidad en metros por segundo
        ang (float): angulo en grados        
    """
    angle=np.radians(ang)
    end= np.roots([-4.9, v * np.sin(angle), 0])
    
    t=np.linspace(0, end[0], 100)
    
    x= v * np.cos(angle) * t
    y= v * np.sin(angle) * t - 4.9 * t ** 2
    plt.plot(x, y)

    plt.xlabel("eje X")
    plt.ylabel("eje Y")
    plt.title("grafica del tiro")

    plt.show()


def tiro_parabolico(
    v0:float,
    ang:float
    ):
    G=float(4.9)
    """Funcion para calcular datos de un tiro parabolico. Angulo en grados, rapidez inicial en metros sobre segundo

    Args:
        v0 (float): Velocidad inicial
        ang (float): 
    Returns:
        list: altura maxima en metros, alcance en metros y velocidad final en metros sobre segundo.
    """
    
    
    v0_x = v0 * cos(radians(ang))
    v0_y = v0 * sin(radians(ang))
        
        
    #   4.9(t)^2 + v0(t) = 0
    end_time = np.roots([-G, v0_y, 0])
    
    # x = v0_x(t)
    alcance = v0_x * end_time[0]
    
    # y = v0_y(t) - 4.9(t)^2
    alt_max = v0_y * ( end_time[0] / 2 ) - G * (end_time[0] / 2) ** 2
    
    vf= v0_x + v0_y - 9.8 * end_time[0]
    
    return [round(alt_max, 3), round(alcance, 3), vf]

def this_tiro_parabolico():
    """funcion para resolver el problema 1.
    """
    while True:
        try:        
            ang = float(input("Ingresa el angulo de inclinación del tiro en grados: "))
            rapidez = float(input("Ingresa la rapidez inicial del tiro: "))
            
            output = tiro_parabolico(v0=rapidez, ang=ang)
            
            print("Los datos obtenitos son:")
            print (f"La altura maxima fue: {output[0]} metros")
            print(f"El alcanse del tiro fueron {output[1]} metros")
            print(f"La velocidad final es de {output[2]} metros sobre segundo")
            
            graficadora(rapidez,ang)
            
            rep = input("deseas repetir el tiro? pulsa y, sino, pulsa n ")
            
            if  rep == ("n"):
                print("Finalisando procesos")
                break
            elif rep == ("y"):
                print("ok")
            else:
                print("Entrada desconocida, finalisando procesos")
                break
        
        except ValueError:
            print("Entrada desconocida, vuelve a intentarlo")
            
        except Exception as e:
            print(f"Error desconocido: {e}")

if __name__ == "__main__":
    this_tiro_parabolico()