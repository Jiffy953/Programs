list = []
for numbers in range(1, 21):
    list.append(numbers)
print(list)

one_mil = []
for mil in range(1, 1000001):
    one_mil.append(mil)
print("The firt three items of the one mil list are: ")
print(one_mil)

odd_list = []
for odd in range(1,21,2):
    odd_list.append(odd)
print(odd_list)

threes = []
for three in range(3, 31):
    threes.append(three * 3)
print(threes)

cubes = []
for cube in range(1,11):
    cubes.append(cube ** 3)
    print(cubes[-1])

squares = [value**2 for value in range(1,11)]
print(squares)

cubes_comp = [value**3 for value in range(1,11)]
print(cubes_comp)
