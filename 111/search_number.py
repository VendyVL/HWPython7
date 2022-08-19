
def Searching():
    dict = open('phone_dictionary.txt', 'r')

    a = input('Кого ищем? ')

    for line in dict:
        if a in line:
            print (line)
    dict.close