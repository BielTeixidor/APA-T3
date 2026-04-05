"""
Biel Teixidor Cladellas

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4, 10, 18])
>>> v1 @ v2
32
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])

"""


class Vector:
    vector = []
    
    def __init__(self, numeros):
        """ Inicialitzacio de la funció
            Args: cadena de numeros que volem que tingui el vector. 
                  ex. [1,2,3,4,5]
            Sortida: llista amb la cadena de numeros.
        """
        self.vector = [numero for numero in numeros]



    def __repr__(self):
        """ Variable de representació visual del vector
        """
        return 'Vector(' + repr(self.vector) + ')'


    def __str__(self):
        """ Representació en cadena del vector
        """
        str_ = '['
        for componente in self.vector:
            str_ += ' ' + str(componente)
        str_ += ' ] '
        return str_

    
    def __mul__(self, other):
        """ Multiplicación de vectores metodo Hadamard o la multiplicacion de un vector por un escalar
            Args: (Vector1,Vector2) o (Vector1,int)
            Output: La multiplicacion por elemento de Vector1 por Vector2 en el caso Args = (Vector1,Vector2) o
                    la multiplicacion de Vector1 por int en el caso de Args = (Vector1,int)
        """
        resultado = []

        if isinstance(other, (int, float)):
            for elemento in self.vector:
                nuevo_numero = elemento * other 
                resultado.append(nuevo_numero)

        elif isinstance(other, Vector):
            for elem_mio, elem_suyo in zip(self.vector, other.vector):
                nuevo_numero = elem_mio * elem_suyo
                resultado.append(nuevo_numero)
        
        return Vector(resultado)


    def __rmul__(self, other):
        """ Multiplicación de vectores metodo Hadamard o la multiplicacion de un vector por un escalar
            Args: (Vector1,Vector2) o (Vector1,int)
            Output: La multiplicacion por elemento de Vector2 por Vector1 en el caso Args = (Vector1,Vector2) o
                    la multiplicacion de int por Vector1 en el caso de Args = (Vector1,int)
        """
        resultado = []

        if isinstance(other, (int, float)):
            for elemento in self.vector:
                nuevo_numero = elemento * other 
                resultado.append(nuevo_numero)

        elif isinstance(other, Vector):
            for elem_mio, elem_suyo in zip(self.vector, other.vector):
                nuevo_numero = elem_mio * elem_suyo
                resultado.append(nuevo_numero)
        
        return Vector(resultado)

    
    def __matmul__(self, v2):
        """Producto escalar de dos vectores
            Args: (Vector1, Vector2)
            Output: Producto escalar entre Vector1 y Vector2
        """
        resultado = 0

        for elem1, elem2 in zip(v2.vector, self.vector):
            resultado += (elem1*elem2)

        return resultado

    def __rmatmul__(self, v2):
        """Producto escalar de dos vectores (reverso)
            Args: (Vector1, Vector2)
            Output: Producto escalar entre Vector1 y Vector2
        """

        return self @ v2


    def __floordiv__(self,v2):
        """Componente tangencial (paralela) de un vector respecto a otro
            Args: (Vector1, Vector2)
            Output: Vector paralelo resultante de la proyección de Vector1 sobre Vector2
        """
        temp = (self @ v2) / (v2 @ v2)
        return v2 * temp


    def __rfloordiv__(self,v2):
        """Componente tangencial (paralela) de un vector respecto a otro (reverso)
            Args: (Vector1, Vector2)
            Output: Vector paralelo resultante de la proyección de Vector2 sobre Vector1
        """
        temp = (self @ v2) / (self @ self)
        return self * temp

    def __mod__(self,v2):
        """Componente normal (perpendicular) de un vector respecto a otro
            Args: (Vector1, Vector2)
            Output: Vector normal (perpendicular) de Vector1 respecto a Vector2
        """
        resultado = []
        v1_paralelo = self // v2
        
        for elem_mio, elem_paralelo in zip(self.vector, v1_paralelo.vector):
            nuevo_numero = elem_mio - elem_paralelo
            resultado.append(nuevo_numero)
            
        return Vector(resultado)

    def __rmod__(self,v2):
        """Componente normal (perpendicular) de un vector respecto a otro (reverso)
            Args: (Vector1, Vector2)
            Output: Vector normal (perpendicular) de Vector2 respecto a Vector1
        """
        resultado = []
        v1_paralelo = v2 // self
        
        for elem_mio, elem_paralelo in zip(v1_paralelo.vector, self.vector):
            nuevo_numero = elem_mio - elem_paralelo
            resultado.append(nuevo_numero)
            
        return Vector(resultado)