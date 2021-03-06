"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта,
создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, number, inumber):
        self.complex = complex(number, inumber)

    def __add__(self, other):
        return self.complex + other.complex

    def __mul__(self, other):
        return self.complex * other.complex


if __name__ == '__main__':
    one = Complex(1, 2)
    two = Complex(3, 4)
    print(one + two)
    print(one * one)
