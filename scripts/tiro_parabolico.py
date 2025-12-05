from math import *
import numpy as np
import matplotlib.pyplot as plt

def graficadora(
    v:float,
    ang:float
    ) -> None:
    
    """Grafica de tiros parabolicos de posicion contra posicion usando matplotlib.

    Args:
        v (float): velocidad en metros por segundo.
        ang (float): angulo en grados.
    """
    
    #calcula las raices (cruces con el eje x) y pasa el angulo a radianes
    angle=np.radians(ang)
    end= np.roots([-4.9, v * np.sin(angle), 0])
    
    #intervalo de tiempo a graficar
    t=np.linspace(0, end[0], 100)
    
    #Separa los componentes de la velocidad |v|coseno(theta),|v|seno(theta)
    x= v * np.cos(angle) * t
    y= v * np.sin(angle) * t - 4.9 * t ** 2

    #generar grafica usando matplotlib
    plt.plot(x, y)
    plt.xlabel("eje X")
    plt.ylabel("eje Y")
    plt.title("grafica del tiro")

    plt.show()


def tiro_parabolico(
    v0:float,
    ang:float
    )-> list:
    G=float(4.9)
    """Funcion para calcular datos de un tiro parabolico. Angulo en grados, rapidez inicial en metros sobre segundo

    Args:
        v0 (float): Velocidad inicial
        ang (float): 
    Returns:
        list: altura maxima en metros, alcance en metros y velocidad final en metros sobre segundo.
    """
    
    #Separa los componentes de la velocidad |v|coseno(theta),|v|seno(theta) y pasa los angulos a radianes
    v0_x = v0 * cos(radians(ang))
    v0_y = v0 * sin(radians(ang))
        
        
    #Busca los momentos donde el proyectil llega al suelo usando la funcion x(t)=0 lo que implica  v0(t) + 4.9(t)^2 = 0
    end_time = np.roots([-G, v0_y, 0])
    
    #Encuentra el alcance usando la funcion x(t) = v0_x(t)
    alcance = v0_x * end_time[0]
    
    #Encuentra la altura maxima usando la funcion y(t) = v0_y(t) - 4.9(t)^2
    alt_max = v0_y * ( end_time[0] / 2 ) - G * (end_time[0] / 2) ** 2
    
    #Encuentra la velocidad final, usando la formula de la velocidad a partir de velocidad inicial y aceleracion
    vf= v0_x + v0_y - 9.8 * end_time[0]
    
    #regresa una lista con todos los datos obtenidos
    return [round(alt_max, 3), round(alcance, 3), vf]

def main():
    """Codigo principal para graficar tiros parabolicos.
    """
    while True:
        try:        
            ang = float(input("Ingresa el angulo de inclinación del tiro en grados: "))
            rapidez = float(input("Ingresa la rapidez inicial del tiro: "))
            
            salida = tiro_parabolico(v0=rapidez, ang=ang)
            
            print("Los datos obtenitos son:")
            print (f"La altura maxima fue: {salida[0]} metros")
            print(f"El alcanse del tiro fueron {salida[1]} metros")
            print(f"La velocidad final es de {salida[2]} metros sobre segundo")
            
            graficadora(rapidez,ang)
            break
                
        except ValueError:
            print("Entrada desconocida, vuelve a intentarlo")
            
        except Exception as e:
            print(f"Error desconocido: {e}")

if __name__ == "__main__":
    main()