import moduls_1
import math
from mod import math - # from - Откуда (mod- папка) и импортируем через импорт ( файл math )
import random
moduls_1.some_1()
print(math.pi)
r = random.randrange (0, 10)
print(r)
print(math.pi)

from mod import some
some.sub(19, 11, 2)

some.sum(10, 15, 10)

В примере выше мы импортировали с папки (Mod) функцию some с параметрами "sum / sub". В файле some - у нас 2 функции
со значениями def sub(a, b, c): и def sum(a, b, c): и мы уже в модуле подставляем свои цифры и выводим результат