class SquareException(ValueError):
    pass
class NonPositiveDigitException(SquareException):
    pass
class Square:
    def __init__(self,a):
        if a>0:
            self.a=a
            print(f"Сторона квадрата равна {self.a}")
        else:
            self.a = a
            print(f"Сторона квадрата равна {self.a}")
            print("Введите значение больше 0")
            raise NonPositiveDigitException("Возникла ошибка")
    def get_area_square(self):
        return self.a**2
square_1=Square(0)

