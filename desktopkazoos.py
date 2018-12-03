import random
import os

login = os.getlogin()
num = input("How may kazoos would you like to add to your desktop? ")
for x in range(int(num)):
    f = open(f"C:\\Users\\{login}\\Desktop\\brandnewkazoo{random.randint(0, 100)}.txt", "w+")
    for i in range(10):
        f.write('''
88
88
88
88   ,d8  ,adPPYYba, 888888888  ,adPPYba,   ,adPPYba,
88 ,a8"   ""     `Y8      a8P" a8"     "8a a8"     "8a
8888[     ,adPPPPP88   ,d8P'   8b       d8 8b       d8
88`"Yba,  88,    ,88 ,d8"      "8a,   ,a8" "8a,   ,a8"
88   `Y8a `"8bbdP"Y8 888888888  `"YbbdP"'   `"YbbdP"'
\r\n''')
    f.close()

def kazoo_noise_number():
    if int(num) == 1:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Recording')
    elif int(num) == 2:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Merged0_1.mp3')
    elif int(num) == 3:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Merged0_2.mp3')
    elif int(num) == 4:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Merged0_3.mp3')
    elif int(num) == 4:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Merged0_4.mp3')
    elif int(num) == 5:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Merged0_5.mp3')
    elif int(num) == 6:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Merged0_6.mp3')
    elif int(num) == 7:
        os.startfile('C:\\Users\\Jared\\Documents\\GitHub\\Programs\\Merged0_7.mp3')
    elif int(num) == 8:
        os.startfile('C:\Users\Jared\Documents\GitHub\Programs\Merged0_8.mp3')
    else:
        os.startfile('C:\Users\Jared\Documents\GitHub\Programs\Merged0_9.mp3')
kazoo_noise_number()
input("Enjoy!")
