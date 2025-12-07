from time import sleep


def es_bisiesto(
    year: int
    ) -> bool:
    """Ve si un anio es bisiesto o no

    Args:
        anio (int): anio en cuestion

    Returns:
        bool: Si o No
    """
    
    n = int (year)
    
    #un anio es bisiesto si es divisible entre 400 o es divisible entre 4 pero no entre 100. Usa la operacion % para saber el restos
    if n % 400 == 0: 
        pass    
    elif n % 4 == 0 and n % 100 != 0:
        pass

    else:
        return False #el anio no es bisiesto
 
    return True #el anio si es bisiesto

def main():
    
    while True:
        try:
            #entrada del usuario
            year = input("ingresa tu anio\n")
            
            #determina si el anio ingresado es bisiesto o no usando la funcion es_bisiesto
            output = es_bisiesto(year)
            match output:
                case True:
                    print(f"{year} es bisiesto")
                    
                case False:
                    print(f"{year} no es bisiesto")
            
            sleep(1)
            break #termina el programa
            
        except Exception:
            print("ingresa una fecha valida")  
            continue #repite el programa hasta que se ingrese un anio valido
        
if __name__ == "__main__":
    main()
    
    
