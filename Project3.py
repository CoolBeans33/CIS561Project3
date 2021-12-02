import numpy as np
import pandas as pd


concepts = pd.read_csv("concepts.csv", header=None)

concepts[0] = concepts[0].str.lower()
num_concepts = concepts.nunique()[0]
print(concepts.value_counts())
print(num_concepts)

frequency_matrix = np.zeros((num_concepts, num_concepts))
print(frequency_matrix)
