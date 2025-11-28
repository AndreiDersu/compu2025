import numpy as np
import time

def data_base():
	#Funciones
	def read_horario(entrada,dic,horario):
		alumno = dic[entrada]
		print(f"Alumno: {alumno[[1]][0]} ({alumno[[0]][0]}) \n Carrera: {alumno[[2]][0]} \n Grupo: {alumno[[3]][0]}")
		print("horario:")
		for index in range (1,horario.shape[0]):
			print(f"   {horario[index,0]}:     {horario[index,1]}     {horario[index,2]}")
			time.sleep(0.09)

	def escritura_datos(storage):
		ncuenta = input ("numero de cuenta: \n")
		nombre = input ("nombre: \n")
		carrera = input ("carrera: \n")
		grupo = input ("grupo: \n")
		data = np.array([[ncuenta,nombre,carrera,grupo]])
		
		new_storage = np.concatenate([storage, data], axis=0)
		return new_storage

	def escritura_horarios():
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


	#Cargar datos de los alumnos
	alumno = np.loadtxt("sources/alumnos.csv", delimiter=",", dtype=str)

	#Almacenar datos en un diccionario, key = numero de cuenta
	dic = {}
	for index in range(alumno.shape[0]):
		dic[str(alumno[index,0])] = alumno[index]

	#Iniciar programa
	modo = int(input ("selccionar modo: 1 para leer, 2 para escribir "))
	match modo:
		case 1:
			print("Lectura \n")
			print("ingresa el número de cuenta:")
			entrada = input()
			try:
				horario = np.loadtxt(f"sources/horarios/{entrada}.csv", delimiter=",", dtype=str)
				read_horario(entrada=entrada,dic=dic,horario=horario)
			except Exception:
				print("usuario no encontrado	")
		case 2:
			print("Escritura \n")
	
			#actualizar datos de alumnos
			nueva_data = escritura_datos(alumno)

			#actualizar horario
			nuevo_horario = escritura_horarios()
			name = str(nueva_data[-1][0])
	
			#salvar trabajo
			np.savetxt("sources/alumnos.csv", nueva_data,
		delimiter = ",", fmt='%s')
			np.savetxt(f"sources/horarios/{name}.csv", nuevo_horario, delimiter = ",", fmt='%s')
   
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