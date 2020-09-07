
import unittest
def programa():
    year = int(input('Introduzca el año actual: '))
    edad = int(input('Introduzca su edad: ')) 
    incremento = int
    if (year < 0) :
        print('El año actual no es correcto')
    else:
        incremento =  2070-year
        edad = edad + incremento
        print("Su edad en el 2070 es " ,edad)

    return edad

def prueba(a,b): 
    return a+b

class PruebasFunciones(unittest.TestCase):
    def test_es_par(self):
        b = 2070 - 2020
        self.assertEqual(prueba(10,b), programa())

if __name__ == '__main__':
    unittest.main()
