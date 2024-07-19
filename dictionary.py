# Список (выдает все значения, последовательно один за одним) может содержать дубликаты.

family_1 = ["Max", "Diana", "Kraken"]
print(family_1)

# Множества (выдаются в рандом порядке, не содержат дубликатов) То есть 2 одинаковых имени, не будет в множестве.

family_2 = {"Max", "Diana", "Kraken"}
print(family_2)

# Словарь

family_3 = {"Mom": "Diana", "Son": "Kraken", "Dad": "Max"}
# print(family_3["Dad"])
for k, v in family_3.items():
    print(v)
