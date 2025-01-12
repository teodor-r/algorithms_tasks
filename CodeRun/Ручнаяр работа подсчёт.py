import pandas as pd
import numpy as np


# Функция для чтения данных из CSV и вычисления длины пути
def calculate_path_length(filename):
    data = pd.read_csv(filename)
    x = data['x']
    y = data['y']

    # Вычисляем расстояние между последовательными точками
    distances = np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2)

    # Суммируем расстояния, чтобы получить общую длину пути
    total_length = np.sum(distances)
    return total_length


# Файлы с данными
file1 = 'path_v.csv'
file2 = 'path.csv'

# Вычисляем длины путей для двух наборов данных
length1 = calculate_path_length(file1)
length2 = calculate_path_length(file2)

print(f"Длина пути для path_v.csv: {length1}")
print(f"Длина пути для path.csv: {length2}")
