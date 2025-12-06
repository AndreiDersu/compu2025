from math import *

def cuadratic_formula (a=int, b=int, c=int):
    """Sean a,b,c numeros reales tal que ax**2+bx+c=0, con a distinto a 0.
    Se admiten resultados complejos."""
    if a != 0:
        dis = b ** 2 - 4 * a * c
        
        x1 = -b + dis ** (1/2) / (2 * a)
        
        x2 = -b - dis ** (1/2) / (2 * a)
        
        x=[x1,x2]
        print(x1,x2)
        return (x)
    else:
        pass
    

def cuadtic_form (
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
    try:
        if a != 0:
            pass
        else:
            return False
        dis = b ** 2 - 4 * a * c
        x1 = -b + dis ** (1/2) / (2 * a)
        x2 = -b - dis ** (1/2) / (2 * a)
        return (x1,x2)

    except Exception:
        return False

def main():
    while True:
        try: 
            a = float (input("ingresa el termino a\n"))
            b = float (input("ingresa el termino b\n"))
            c = float (input("ingresa el termino c\n"))
            
            roots = cuadratic_formula(a,b,c)
            print("a")
            match roots:
                case False:
                    print("Error, vuelve a intentarlo")
                    continue
                case _:
                    pass
            
            print(f"las raices de la ecuacion: {a}x^2 + {b}x + {c} son:")
            for i in range (0,len(roots)):
                print (f"x_{i+1}={roots[i]}")
            break
            
        except Exception as e:
            print ("un error a ocurrido:", e)
        
if __name__ == "__main__":
    main()