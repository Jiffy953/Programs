print("words") #prints your thing
print(f"{var}") #prints a thing that already is assinged
input("words") #will ask for input
from sys import argv #import argument varible function which is assinged when deploying the code
script, a, b, c = argv #assign varibles to it
var = open(file_name) #opens an assigned file in the libiary, doesnt need a varible
print(var.read()) #will print out a targeted file's contents
target = open(file_name, 'w')
target.write(var) #gets a file open and if it doesnt exist it creates one with 'w' then we are able to write strings in it with them assinged to varibles input to (var)
def functionname(a, b, c):
    return a + b - c #basic funtion notation this one sets up varibles and does math to them
def functionname(a, b, c):
    print(f"{a}, {b}, {c}") #this one prints the stuff
def functionname(file):
    file.seek(0) #this one seeks a file and goes to byte 0 of the file
