# age = 20
# name = "Alex"
# if age == 20 and name == "Alex":
#     print("My name is Alex, me 20 years old")
# elif age == 20 and name == "Max" :
#     print("My name is Max, and me 20 years")
# else:
#     print("right conditions")

# age = 30
# name = "Max"
# if age == 20 or name == "Max":
#     print("My name is Max, me 30 years old")
# else:
#     print("right conditions")


# name = "Max"
# if "x" in name == "Max":
#     print("My name is Max, me 35 years old")
# else:
#     print("right conditions")

pin = 777
print("Type please your pin-code")
user_pin = int(input())

if pin == user_pin :
    print("What a mount money you withdraw")
else:
    print("Error, type correctly pin, you have more 2 chance")
    user_pin = int(input())
    if pin == user_pin:
        print("What a mount money you withdraw")
    else:
        print("Error, type correctly pin, you have more 1 chance")
        user_pin = int(input())
        if pin == user_pin:
            print("What a mount money you withdraw")
        else:
            print("Error, blocked")