a = int(input("Type here first value :"))
b = int(input("Type here second value :"))
#
try:
    result = int(a / b)
except ZeroDivisionError :
    result = 0
    print("Division to zero cannot possible")
print("Result : " + str(result))

# ZeroDivisionError