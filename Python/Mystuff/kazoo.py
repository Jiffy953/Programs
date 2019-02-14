name_input = (input("Hello welcome to the master Kazoo interface may I have your name?"))
name_begining = "Xx420"
name_ending = "MLGxX"
name = (f"%s{name_input}%s" % (name_begining, name_ending))
print(f"Well hello there general {name} its good to see you again")
responce = str(input("Would you add another Kazoo to your collection? "))
if responce in ['yes', 'y', 'YES', 'sure', 'no', 'nope' ]:
    def main():
        for i in range(2):
            f = open("A_brandnew_kazoo_for_you.txt", "w+")
            f.write("Kazoo for you \r\n")
        f.close()
