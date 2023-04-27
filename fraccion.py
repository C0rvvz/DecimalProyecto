class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator: int = numerator
        self.denominator: int = denominator

    def sumar(self, fraccion: int):
        try:
            numerador = (self.numerator * fraccion.denominator) + (self.denominator * fraccion.numerator)
            denominador = self.denominator * fraccion.denominator
            return print(f"{numerador / denominador}")
        except (ValueError, ZeroDivisionError):
            print("No es un numero valido.")
        finally:
            print("Operacion realizada")

    def restar(self, fraccion: int):
        try:
            numerador = (self.numerator * fraccion.denominator) - (self.denominator * fraccion.numerator)
            denominador = self.denominator * fraccion.denominator
            return print(f"{numerador / denominador}")
        except (ValueError, ZeroDivisionError):
            print("No es un numero valido.")
        finally:
            print("Operacion realizada")

    def multiplicar(self, fraccion: int):
        try:
            numerador = self.numerator * fraccion.numerador
            denominador = self.denominator * fraccion.denominator
            return print(f"{numerador / denominador}")
        except (ValueError, ZeroDivisionError):
            print("No es un numero valido.")
        finally:
            print("Operacion realizada")

    def dividir(self, fraccion: int):
        try:
            numerador = self.numerator * fraccion.denominator
            denominador = self.denominator * fraccion.numerator
            return print(f"{numerador / denominador}")
        except (ValueError, ZeroDivisionError):
            print("No es un numero valido.")
        finally:
            print("Operacion realizada")

operacion1 = Fraction(6,7)
operacion2 = Fraction(9,5)

operacion1.sumar(operacion2)