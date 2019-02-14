import os
import random

num = random.randint(1, 10)
def kazoo_number():
    if num == 1:
        os.startfile('')
    elif num == 3:
        os.startfile('')
    elif num == 4:
        os.startfile('')
    elif num == 5:
        os.startfile('')
    elif num == 6:
        os.startfile('')
    elif num == 7:
        os.startfile('')
    elif num == 8:
        os.startfile('')
    elif num == 9:
        os.startfile('')
    elif num == 10:
        os.startfile('')

def main():
    f = open("A_brandnew_kazoo_for_you.txt", "w+")
    for i in range(100):
        f.write("Kazoo for you \r\n")
    f.close()
if __name__=="__main__":
    main()
    print("Weather you wanted it or not, there you go a brawn new kazoo whereever this progam is stored at!")
else:
    print("Well thats not very cash money of you")

print("Hello welcome to the main Kazoo interface MkII")
responce = input('''Would you like to:
1: Play some sick Kazoo sounds that will rock your world
2: Add some new totally radial kazoos into your directory
3: idk close the program i guess
''')

def what_to_do():
    if responce == '1':
        kazoo_number()
    else:
        main()
