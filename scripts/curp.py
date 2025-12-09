
import unicodedata

def normalizar(texto):
    # Mayúsculas
    texto = texto.upper()
    # Quitar acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # Quitar caracteres no permitidos
    permitido = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    texto = ''.join(c for c in texto if c in permitido)
    return texto.strip()

def primera_vocal_interna(palabra):
    vocales = "AEIOU"
    for c in palabra[1:]:
        if c in vocales:
            return c
    return "X"

def primera_consonante_interna(palabra):
    vocales = "AEIOU"
    for c in palabra[1:]:
        if c not in vocales and c.isalpha():
            return c
    return "X"

def obtener_letra_nombre(nombre):
    partes = nombre.split()
    # Regla especial
    ignorar = {"JOSE", "J", "MARIA", "MA"}
    if len(partes) > 1 and partes[0] in ignorar:
        return partes[1][0]
    return partes[0][0]

ENTIDADES = {
    "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS",
    "CAMPECHE": "CC", "COAHUILA": "CL", "COLIMA": "CM", "CHIAPAS": "CS",
    "CHIHUAHUA": "CH", "CIUDAD DE MEXICO": "DF", "DURANGO": "DG", "GUANAJUATO": "GT",
    "GUERRERO": "GR", "HIDALGO": "HG", "JALISCO": "JC", "MEXICO": "MC",
    "MICHOACAN": "MN", "MORELOS": "MS", "NAYARIT": "NT", "NUEVO LEON": "NL",
    "OAXACA": "OC", "PUEBLA": "PL", "QUERETARO": "QT", "QUINTANA ROO": "QR",
    "SAN LUIS POTOSI": "SP", "SINALOA": "SL", "SONORA": "SR", "TABASCO": "TC",
    "TAMAULIPAS": "TS", "TLAXCALA": "TL", "VERACRUZ": "VZ", "YUCATAN": "YN",
    "ZACATECAS": "ZS", "NACIDO EN EL EXTRANJERO": "NE"
}

def generar_curp(nombre, apellido_paterno, apellido_materno,
                fecha_nacimiento, sexo, estado):
    
    # Normalizar entradas
    nombre = normalizar(nombre)
    apellido_paterno = normalizar(apellido_paterno)
    apellido_materno = normalizar(apellido_materno) if apellido_materno else "X"
    sexo = sexo.upper()
    estado = ENTIDADES[normalizar(estado)]
    
    # Letras iniciales
    l1 = apellido_paterno[0]
    l2 = primera_vocal_interna(apellido_paterno)
    l3 = apellido_materno[0] if apellido_materno != "X" else "X"
    l4 = obtener_letra_nombre(nombre)
    
    # Fecha nacimiento: "YYYY-MM-DD"
    año, mes, dia = fecha_nacimiento.split("-")
    fecha = año[2:] + mes + dia    # YYMMDD
    
    # Consonantes internas
    c1 = primera_consonante_interna(apellido_paterno)
    c2 = primera_consonante_interna(apellido_materno)
    c3 = primera_consonante_interna(nombre)
    
    # Diferenciador por siglo
    diferenciador = "0" if int(año) < 2000 else "A"
    
    # Dígito verificador provisional (simplificado a 0)
    verificador = "0"
    
    curp = (
        l1 + l2 + l3 + l4 +
        fecha +
        sexo +
        estado +
        c1 + c2 + c3 +
        diferenciador + verificador
    )
    
    return curp

def main():
    curp = generar_curp(
        nombre=input("Nombre (s)\n"),
        apellido_paterno=input("apellido paterno \n"),
        apellido_materno=input("apellido materno \n"),
        fecha_nacimiento=input("fecha de nacimiento en formato YYYY-MM-DD \n"),
        sexo=input("sexo (h,m) \n"),
        estado=input("tu estado de nacimiento \n") 
    )
    print(f"tu curp es \n {curp}")

if __name__ ==  "__main__":
    print("Generador de CURP")
    while True:
        try:
            main()
        except Exception as e:
            print("error:", e)
