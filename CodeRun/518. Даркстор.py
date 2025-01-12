

def max_submatrix_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Префиксные суммы для каждой строки
    prefix_sums = [[0] * (m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(1, m + 1):
            prefix_sums[i][j] = prefix_sums[i][j - 1] + matrix[i][j - 1]

    max_sum = float('-inf')

    # Выбираем левую и правую границы
    for left in range(m):
        for right in range(left, m):
            current_sum = 0
            best_sum = float('-inf')

            # Используем алгоритм Каданэ для столбцов между left и right
            for row in range(n):
                sum_segment = prefix_sums[row][right + 1] - prefix_sums[row][left]
                current_sum += sum_segment
                if current_sum > best_sum:
                    best_sum = current_sum
                if current_sum < 0:
                    current_sum = 0

            if best_sum > max_sum:
                max_sum = best_sum

    return max_sum


# Пример использования:
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(max_submatrix_sum(matrix))
