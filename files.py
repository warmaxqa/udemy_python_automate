var = input("Type here someone : ")
fw = open("doc/file.txt", "a")
fw.write(var)
fw.close()

# a -  Запись новых данных в файл, помещение новых данных в конец файла

fw = open("doc/file2.txt", "w")
fw.write("Hello!!!")
fw.close()

# w - Запись новых данных, с удалением старых данныхc

fr = open("doc/file.txt", "r")
text = fr.read()
fr.close()

print(text)

# r - Читать данные / содержимое. Выводит текст с файла file.txt