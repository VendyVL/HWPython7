
def Printing():
    dict = open('phone_dictionary.txt', 'r')
    for line in dict:
        print (line)
    dict.close