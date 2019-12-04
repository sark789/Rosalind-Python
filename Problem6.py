from collections import Counter

counter = Counter()

f = open(
    'C:\\Users\\timpo\\OneDrive\\Namizje\\Bioinformatika\\rosalind_ini6.txt', 'r')
lines = f.read().rstrip()


def Dictionaries(lines):
    for word in lines.split(' '):
        counter[word] += 1  # counter[key] = value
    for k in counter.keys():
        print("", k, counter[k])


Dictionaries(lines)
