"""
1. Создать класс TrafficLight (светофор)
и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def running(self):
        while True:
            self.__color = 'red'
            print(self.__color)
            time.sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'green'
            print(self.__color)
            time.sleep(4)


tr_l_1 = TrafficLight()
tr_l_1.running()
