import numpy as np
import time
from numpy.typing import NDArray

def data_base():
	"""Funcion para leer o escribir en la base de datos de horarios de los alumnos
	"""
	#Funciones
 
	def read_horario(
     entrada: str,
     dic: dict,
     horario: NDArray[any]
     ) -> None:
		"""Imprime los datos y el horario del estudiante en la terminal desde una base de datos.

		Args:
			entrada (str): numero de cuenta del estudiante
			dic (dict): base de datos a usar con los datos de cada estudiante (alumnos.csv)
			horario (NDArray[any]): Array con los horarios de cada estudiante (horarios)
		"""
		#selecciona un alumno a partir de su numero de cuenta
		alumno = dic[entrada]
		#imprime los datos del alumno seleccionado
		print(f"Alumno: {alumno[[1]][0]} ({alumno[[0]][0]}) \n Carrera: {alumno[[2]][0]} \n Grupo: {alumno[[3]][0]}")
		
		#imprime su horario usando un for segun el numero de clases
		print("horario:")
		for index in range (1,horario.shape[0]):
			print(f"   {horario[index,0]}:     {horario[index,1]}     {horario[index,2]}")
			time.sleep(0.09)

	def escritura_datos(
     storage: NDArray[any]
     )-> NDArray[any]:
		"""Funcion para actualizar los datos de los alumnos y guardarlos en la base de datos

		Args:
			storage (NDArray[any]): base de datos a usar (alumnos.csv)

		Returns:
			NDArray[any]: base de datos actualizada
		"""
		ncuenta = input ("numero de cuenta: \n")
		nombre = input ("nombre: \n")
		carrera = input ("carrera: \n")
		grupo = input ("grupo: \n")
		data = np.array([[ncuenta,nombre,carrera,grupo]])
		
		new_storage = np.concatenate([storage, data], axis=0)
		return new_storage

	def escritura_horarios(
     )->NDArray:
		"""Funcion para actualizar los horarios de los alumnos

		Returns:
			NDArray: nuevo horario, que posteriormente se va a guardar en el directorio horarios
		"""
		storage = np.array([[0,0,0]])
		while True:
			nueva = input ("¿Agregar nueva materia? y,n \n")
			match nueva:
				case "y":
					materia = input("Nombre de la materia: \n")
					dia = input("Dias de la materia (no usar comas): \n")
					hora = input("Horario de clase: \n")
					data = np.array([
								[materia,dia,hora]])
					storage = np.concatenate([storage,data], axis=0)
				case "n":
					break
		return storage


	#Cargar datos de los alumnos de la carpeta de recursos (alumnos.csv)
	alumno = np.loadtxt("sources/alumnos.csv", delimiter=",", dtype=str)

	#Almacenar datos en un diccionario, donde la key es el numero de cuenta
	dic = {}
	for index in range(alumno.shape[0]):
		dic[str(alumno[index,0])] = alumno[index]

	#Iniciar programa
	modo = int(input ("selccionar modo: 1 para leer, 2 para escribir "))
	match modo:
		case 1:
			print("Lectura \n")
			entrada = input("ingresa el número de cuenta:\n")
			try:
				#trta de cargar el horario del numero de cuenta ingresado
				horario = np.loadtxt(f"sources/horarios/{entrada}.csv", delimiter=",", dtype=str)
				read_horario(entrada=entrada,dic=dic,horario=horario)
			except Exception:
				print("usuario no encontrado")
    
		case 2:
			print("Escritura \n")
	
			#actualizar datos de alumnos
			nueva_data = escritura_datos(alumno)

			#actualizar horario
			nuevo_horario = escritura_horarios()
			name = str(nueva_data[-1][0])
	
			#salvar trabajo en el directorio sources (horarios y alumnos.csv)
			np.savetxt("sources/alumnos.csv", nueva_data, delimiter = ",", fmt='%s')
			np.savetxt(f"sources/horarios/{name}.csv", nuevo_horario, delimiter = ",", fmt='%s')
   
		case _:
			print("comando desconocido")
   
if __name__ == "__main__":
	print("Base de datos horario de alumnos")
	while True:
		data_base()
		select = input("pulsa n para salir, y para repetir \n")
		match select:
			case "y":
				pass
			case "n":
				break