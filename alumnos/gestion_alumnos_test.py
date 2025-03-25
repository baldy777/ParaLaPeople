'''importar libreria para busqueda de errores'''
import unittest

'''metodo para buscar alumnos si existe en el archivo'''
def buscar_alumno(alumnos, nombre):
    for alumno in alumnos:
        if alumno["nombre"] == nombre:
            return alumno
    return None

'''clase para mandar resultados fuera del archivo 
    en caso de que este exista'''
class TestGestionAlumnos(unittest.TestCase):

    '''metodo de asignacion de datos'''
    def setUp(self):
        self.alumnos = [
            {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
            {"nombre": "Luis", "edad": 22, "carrera": "Matemáticas"},
            {"nombre": "María", "edad": 21, "carrera": "Física"}
        ]

    ''' funciones para ver si axiste alumno buscado'''
    def test_buscar_alumno_existente(self):
        resultado = buscar_alumno(self.alumnos, "Ana")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Ana")

    def test_buscar_alumno_inexistente(self):
        resultado = buscar_alumno(self.alumnos, "Carlos")
        self.assertIsNone(resultado)

'''inicializacion de metodo unittest'''
if __name__ == "__main__":
    unittest.main()