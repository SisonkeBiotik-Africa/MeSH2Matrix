import numpy as np

dataset = open('output/dataset.txt')

for entry in dataset.readlines():
    matrix, label = entry.split(";")
    print(matrix)
    print(label)
    break
