var_1 = 100 # Глобальная переменная
var_2 = 20 # Глобальная переменная

def summ() :
    var_1 = 244 # Локальная переменная
    result = var_1 + var_2
    print(result)

def sub() :
    var_2 = 46 # Локальная переменная
    result = var_1 - var_2
    print(result)

summ()
sub()