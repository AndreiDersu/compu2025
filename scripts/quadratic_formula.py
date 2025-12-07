from math import *    

def quadratic_formula (
    a:float,
    b:float,
    c:float
) -> list:
    """Sean a,b,c numeros reales tal que ax**2+bx+c=0, con a distinto a 0.
    Se admiten resultados complejos.

    Args:
        a (float): Termino x^2
        b (float): Termino x
        c (float): termino independiente

    Returns:
        list: raices
    """
    
    #a debe de ser distinto a cero para que sea cuadratica
    try:
        if a != 0:
            pass #a si es distinto a cero
        else:
            return False #a es cero
    
    #calcula el discriminante y las raices usando la formula cuadratica
        dis = b ** 2 - 4 * a * c
        x1 = -b + dis ** (1/2) / (2 * a)
        x2 = -b - dis ** (1/2) / (2 * a)
        return (x1,x2)

    #en caso que un error ocurra
    except Exception:
        return False

def main():
    while True:
        try: 
            #entradas del usuario
            a = float (input("ingresa el termino a\n"))
            b = float (input("ingresa el termino b\n"))
            c = float (input("ingresa el termino c\n"))
            
            #saca las raices usando la funcion quadratic_formula
            roots = quadratic_formula(a,b,c)
            match roots:
                case False:
                    print("Error, vuelve a intentarlo")
                    continue #repite el codigo si hay un error en las entradas
                case _:
                    pass #pasa a imprimir las respuestas
            
            #imprime las dos posibles raices
            print(f"las raices de la ecuacion: {a}x^2 + {b}x + {c} son:")
            for i in range (0,len(roots)):
                print (f"x_{i+1}={roots[i]}")
            break #finaliza el programa
            
        except Exception as e:
            print ("un error a ocurrido:", e)
        
if __name__ == "__main__":
    main()