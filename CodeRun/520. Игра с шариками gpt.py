from fractions import Fraction
from math import gcd

def calculate_probability(n):
    # Инициализация вероятностей для каждого мешка
    prob1 = Fraction(1, 2)
    prob2 = Fraction(2, 3)
    prob3 = Fraction(6, 7)

    # Общая вероятность вытащить три белых шара на текущем шаге
    total_prob = prob1 * prob2 * prob3

    # Вероятность того, что игра завершится за k шагов
    current_prob = total_prob
    result_prob = 0

    for k in range(1, n + 1):
        result_prob += current_prob
        # Обновление вероятностей
        prob1 = Fraction(prob1.numerator, prob1.denominator + 1)
        prob2 = Fraction(prob2.numerator, prob2.denominator + 1)
        prob3 = Fraction(prob3.numerator, prob3.denominator + 1)

        total_prob = prob1 * prob2 * prob3
        current_prob *= (1 - total_prob)

    # Вероятность того, что игра завершится не более чем за n шагов
    p = result_prob.numerator
    q = result_prob.denominator
    res_del = gcd(p,q)
    p, q   = int(p/res_del) , int(q/res_del)
    return p, q


# Пример использования:
n = int(input("Введите n: "))
p, q = calculate_probability(n)
print(f"{p} {q}")
