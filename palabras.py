
import unittest

def operacion():
    palabra = str(input('Introduzca una palabla '))
    primera = palabra[0]
    ultima=palabra[(len(palabra))-1]
    print('el primer y ultimo caracter de la palabra ingresada son: ')
    print (primera, ultima)
    return (primera, ultima)


class PruebasFunciones(unittest.TestCase):
     def test_palabra(self):
        (p,s)=operacion()
        self.assertEquals('m', p)
        self.assertEquals('l',s)


if __name__ == '__main__':
    unittest.main()
