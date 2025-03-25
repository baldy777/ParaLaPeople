'''importar datos del archivo json'''
import json     

'''creando funcion para cargar datos de alumnos'''
def cargar_alumnos(ruta_archivo):               
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

'''funcion para la busqueda del nombre que se vaya a ingresar por
    terminal'''
def buscar_alumno(alumnos, nombre):             
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre.lower():
            return alumno
    return None

'''metodo principal para la ejecucion por terminal'''
if __name__ == "__main__":

    '''definicion de ruta de archivo json'''
    ruta = "laboratorio5/alumnos.json"
    alumnos = cargar_alumnos(ruta)
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")

    resultado = buscar_alumno(alumnos, nombre_buscar)

    '''condicional simple para mostrar datos por terminal'''
    if resultado:
        print(f"Alumno encontrado: {resultado}")
    else:
        print("Alumno no encontrado.")