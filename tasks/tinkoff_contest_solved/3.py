# def determine_if_win_is_possible(joe_sequence, winning_sequence):
#     l, diff, k = 0, 0, 0
#     for joe_val, win_val in zip(joe_sequence, winning_sequence):
#         if joe_val == win_val and diff == 0:
#             l += 1
#         elif joe_val != win_val:
#             diff += (1 + k)
#             k = 0
#         elif joe_val == win_val:
#             k += 1
#     joe_sequence[l: l+diff] = sorted(joe_sequence[l: l+diff])
#     return joe_sequence == winning_sequence


def read_input():
    n = int(input())
    joe_sequence = list(map(int, input().split()))
    winning_sequence = list(map(int, input().split()))
    return n, joe_sequence, winning_sequence


def determine_if_win_is_possible(n, joe_sequence, winning_sequence):
    if joe_sequence == winning_sequence:
        return True

    if n <= 2:
        return sorted(joe_sequence) == winning_sequence

    l, r = 0, n - 1
    while (joe_sequence[l] == winning_sequence[l]) or (joe_sequence[r] == winning_sequence[r]):
        if joe_sequence[l] == winning_sequence[l]:
            l += 1
        if joe_sequence[r] == winning_sequence[r]:
            r -= 1
    joe_sequence[l: r+1] = sorted(joe_sequence[l: r+1])
    return joe_sequence == winning_sequence


def main():
    if determine_if_win_is_possible(*read_input()):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
