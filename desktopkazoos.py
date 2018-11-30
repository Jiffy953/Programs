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
print("Enjoy!")
