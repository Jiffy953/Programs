import random
import os
import time

login = os.getlogin()
print("Hello welcome to the master kazoo interfact MKII, please enjoy")
time.sleep(3)
num = input("How many kazoos would you like to add to your desktop? ")
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
        os.startfile('Recording.mp3')
    elif int(num) == 2:
        os.startfile('Merged0_1.mp3')
    elif int(num) == 3:
        os.startfile('Merged0_2.mp3')
    elif int(num) == 4:
        os.startfile('Merged0_3.mp3')
    elif int(num) == 4:
        os.startfile('Merged0_4.mp3')
    elif int(num) == 5:
        os.startfile('Merged0_5.mp3')
    elif int(num) == 6:
        os.startfile('Merged0_6.mp3')
    elif int(num) == 7:
        os.startfile('Merged0_7.mp3')
    elif int(num) == 8:
        os.startfile('Merged0_8.mp3')
    else:
        os.startfile('Merged0_9.mp3')
kazoo_noise_number()
print("Enjoy!")
time.sleep(.5)
print('E')
time.sleep(.5)
print('N')
time.sleep(.5)
print('J')
time.sleep(.5)
print('O')
time.sleep(.5)
print('Y')
time.sleep(.5)
