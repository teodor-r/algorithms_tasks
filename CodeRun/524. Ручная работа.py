import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Чтение данных из двух CSV-файлов
data1 = pd.read_csv('path.csv')
data2 = pd.read_csv('path_v.csv')

# Извлечение данных
x1, y1 = data1['x'], data1['y']
x2, y2 = data2['x'], data2['y']

# Создание фигуры и осей
fig, ax = plt.subplots()
ax.set_xlim(min(min(x1), min(x2)), max(max(x1), max(x2)))
ax.set_ylim(min(min(y1), min(y2)), max(max(y1), max(y2)))

# Настройка графика
line1, = ax.plot([], [], 'bo-', label='График 1')
line2, = ax.plot([], [], 'ro-', label='График 2')
ax.set_title('Анимация наложения двух графиков')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

# Функция для инициализации
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Функция для обновления анимации
def update(frame):
    line1.set_data(x1[:frame+1], y1[:frame+1])
    line2.set_data(x2[:frame+1], y2[:frame+1])
    return line1, line2

# Создание анимации
frames = max(len(x1), len(x2))  # Количество кадров анимации - максимальное количество точек в данных
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=False)

# Сохранение анимации как GIF с использованием Pillow с уменьшением FPS для замедления
ani.save('combined_animation_slow.gif', writer=PillowWriter(fps=2))  # Уменьшение FPS для замедления анимации

# Отображение анимации
plt.show()
