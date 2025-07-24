import pandas as pd
import numpy as np


def calculate_path_length(filename):
    data = pd.read_csv(filename)
    x = data['x']
    y = data['y']
    distances = np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2)

    total_length = np.sum(distances)
    return total_length


file1 = 'path_v.csv'
file2 = 'path.csv'

length1 = calculate_path_length(file1)
length2 = calculate_path_length(file2)

print(f"Длина пути для path_v.csv: {length1}")
print(f"Длина пути для path.csv: {length2}")
