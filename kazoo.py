name_input = (input("Hello welcome to the master Kazoo interface may I have your name?"))
name_begining = "Xx420"
name_ending = "MLGxX"
name = (f"%s{name_input}%s" % (name_begining, name_ending))
print(f"Well hello there general {name} its good to see you again")
responce = str(input("Would you add another Kazoo to your collection? "))
if responce in ['yes', 'y', 'YES', 'sure', 'no', 'nope' ]:
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
