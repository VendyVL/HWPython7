def Deleting():
    dict = open('phone_dictionary.txt', 'w')
    a = input('Кого ищем? ')
    for line in dict:
        if a not in line:
             dict.write(line, + '/n')
    dict.close