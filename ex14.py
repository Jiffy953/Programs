from sys import argv
#names our script var and filename with the argv module
script, filename = argv
#creates the "txt" var and makes it open the given filename
txt = open(filename)
#returns the name file's name and prints its contexts as a string
print(f"Here's your file {filename}:")
print(txt.read())
#Creates a var of the name file_again and assigns it the users input
print("Type the filename again:")
file_again = input("zoop ")
#opens the pereviously named file stored in the file_again var
txt_again = open(file_again)
#prints the contents of the named file
print(txt_again.read())
def
