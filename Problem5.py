
f = open(
    'C:\\Users\\timpo\\OneDrive\\Namizje\\Bioinformatika\\rosalind_ini5.txt', 'r')
lines = f.readlines()
for x in range(1, len(lines), 2):
    print(lines[x].rstrip())

f.close()
