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
    
    if n % 400 == 0: 
        pass    
    elif n % 4 == 0 and n % 100 != 0:
        pass

    else:
        return False

    return True

def main():
    
    while True:
        try:
            year = input("ingresa tu anio\n")
            output = es_bisiesto(year)
            
            match output:
                case True:
                    print(f"{year} es bisiesto")
                    
                case False:
                    print(f"{year} no es bisiesto")
            
            sleep(1)
            break
            
        except Exception:
            print("ingresa una fecha valida")
            continue
        
if __name__ == "__main__":
    main()
    
    
