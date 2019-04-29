path = '1.txt'
with open(path, 'r') as file:
    a = file.readlines()


for i in a:
    print(i)