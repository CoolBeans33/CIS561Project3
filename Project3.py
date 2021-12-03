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
