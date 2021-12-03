import numpy as np
import pandas as pd
import csv
import sys


with open('concepts.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

# using join() +  split() to
# perform removal
for i in range(len(data)):
    data[i] = ' '.join(data[i]).split()
print(data)

'''
# Solution 1
words = set()
for sublst in data:
    words |= set(sublst)
words = list(words)
print("Words:\n",words)

result = [[0] * len(words)] * len(words) # zeros matrix N x N

for sublst in data:
    sublst = list(set(sublst)) # selecting unique words only
    for i in range(len(sublst)):
        for j in range(i + 1, len(sublst)):
            index1 = words.index(sublst[i])
            index2 = words.index(sublst[j])
            result[index1][index2] += 1
            result[index2][index1] += 1

print(result)
'''
#Solution 2
#Names of all dicts
all_words = sorted(set([w for sublist in data for w in sublist]))

#Creating the dicts
dicts = []
for i in all_words:
    dicts.append([i, dict.fromkeys([w for w in all_words if w != i],0)])

#Updating the dicts
for l in data:
    for word in sorted(set(l)):
        tmpL = [w for w in l if w != word]
        ind = ([w[0] for w in dicts].index(word))

        for w in dicts[ind][1]:
            dicts[ind][1][w] += l.count(w)

print("Apple\n", dicts[0])