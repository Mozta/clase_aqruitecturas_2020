from numpy import hypot, sqrt
class Figura(object):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

class Rectangulo(Figura):
    def __init__(self,dim1,dim2):
        super(Rectangulo,self).__init__(dim1,dim2)

    def area(self):
        if(self.dim1 != self.dim2):
            print("El area del rectangulo es: ")
        else:
            print("El area del cuadrado es: ")
        return (self.dim1 * self.dim2)

class Triangulo(Figura):
    def __init__(self, dim1,dim2,base, altura):
        super(Triangulo,self).__init__(dim1,dim2)
        self.base = base
        self.altura = altura

    def area(self):
        print("El area del triangulo es: ")
        return(self.altura * self.base)

    def perimetro(self):
        print("El perimetro del triangulo es: ")
        return(self.dim1 + self.dim2 + self.base)

    def hipotenuse(self):
        print("La hipotenusa es: ")
        return (hypot(self.base, self.altura))

def main():

        F = Figura(5,5)
        R = Rectangulo(6,5)
        T = Triangulo(3,7,6,5,4)
        print((R.area()))
        print((T.area()))
        print((T.perimetro()))

    
main()
