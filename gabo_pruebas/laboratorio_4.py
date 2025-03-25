import unittest

class Operaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b
    
    def multiplicacion(self):
        return self.a * self.b
    
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero"
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def es_palindromo(self, cadena):
        cadena = cadena.lower().replace(" ", "")  
        return cadena == cadena[::-1]

class TestOperaciones(unittest.TestCase):
    
    def setUp(self):
        
        self.ops = Operaciones(8, 2) 
    
    # Prueba para la función suma
    def test_suma(self):
        self.assertEqual(self.ops.suma(), 10, 'La suma tiene error.')

    def test_resta(self):
        self.assertEqual(self.ops.resta(), 2, 'La resta tiene error.')

    def test_multiplicacion(self):
        self.assertEqual(self.ops.multiplicacion(), 7, 'La multiplicación tiene error.')

    def test_division(self):
        self.assertEqual(self.ops.division(), 5, 'La división tiene error.')

    # Prueba para la función factorial
    def test_factorial(self):
        self.assertEqual(self.ops.factorial(0), 1,"No es su factorial")       
        self.assertEqual(self.ops.factorial(1), 1,"No es su factorial")       
        self.assertEqual(self.ops.factorial(5), 120,"No es su factorial")     

    # Prueba para la función es_palindromo
    def test_es_palindromo(self):
        self.assertTrue(self.ops.es_palindromo("anita lava la tina"),"No es palindromo")  
        self.assertTrue(self.ops.es_palindromo("reconocer"),"No es palindromo")           
           

if __name__ == "__main__":
    unittest.main()