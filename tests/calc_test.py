import pytest
from calc_app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Проверяем функцию умножения
    def test_mult(self):
        assert self.calc.multiply(self, 2, 3) == 6

    # Проверяем функцию деления
    def test_divis(self):
        assert self.calc.division(self, 6, 2) == 3

    # Проверяем функцию вычитания
    def test_subtr(self):
        assert self.calc.subtraction(self, 2, 3) == -1

    # Проверяем функцию сложения
    def test_add(self):
        assert self.calc.adding(self, 2, 3) == 5

    #Негативное тестирование
    # Проверяем функцию умножения
    def test_mult(self):
        assert self.calc.multiply(self, 2, 3) == 5

    # Проверяем функцию деления
    def test_divis(self):
        assert self.calc.division(self, 6, 2) == 2

    # Проверяем функцию вычитания
    def test_subtr(self):
        assert self.calc.subtraction(self, 2, 3) == 0

    # Проверяем функцию сложения
    def test_add(self):
        assert self.calc.adding(self, 2, 3) == 7