
def Write_num():
    w = open('HomeworkPython7\phone_dictionary.txt', 'a',  encoding='utf-8')
    w.write(f"Фамилия: " + input("Фамилия: ") + "; ")
    w.write(f"Имя: " + input("Имя: ") + "; ")
    w.write(f"Отчество: " + input("Отчество:: ") + "; ")
    w.write(f"Должность: " + input("Должность: ") + "; ")
    w.write(f"Номер телефона: " + input("Номер телефона: ") + "\n")
    w.close


# w = open('HomeworkPython7\phone_dictionary.txt', 'a',  encoding='utf-8')
# w.write(f"Фамилия: " + input("Фамилия: ") + "; ")
# w.write(f"Имя: " + input("Имя: ") + "; ")
# w.write(f"Отчество: " + input("Отчество:: ") + "; ")
# w.write(f"Должность: " + input("Должность: ") + "; ")
# w.write(f"Номер телефона: " + input("Номер телефона: ") + "\n")
# w.close