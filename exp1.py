# q1 = try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count

import string

text = open("sample.txt", "r")

d = dict()

for line in text:
    line = line.strip()

    line = line.lower()

    line = line.translate(line.maketrans("", "", string.punctuation))

    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
