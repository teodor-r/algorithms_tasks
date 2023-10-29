import time
start_time = 0.0
def read_input():
    global start_time
    n, _ = map(int, input().split())
    coin_denominations = list(map(int, input().split()))
    start_time = time.time()
    return n, coin_denominations


def dfs(current_comb, residue, start_ind, coin_denominations):
    if residue == 0:
        return current_comb

    if residue < 0 or start_ind >= len(coin_denominations):
        return None

    is_coin = dfs(current_comb + [coin_denominations[start_ind]], residue - coin_denominations[start_ind], start_ind + 1, coin_denominations)
    is_not_coin = dfs(current_comb, residue, start_ind + 1, coin_denominations)

    if is_coin is not None:
        return is_coin
    else:
        return is_not_coin


def find_combination(n, coin_denominations):
    coins = []
    for coin in coin_denominations:
        coins.append(coin)
        coins.append(coin)
    result = dfs([], n, 0, coins)

    return result


def main():
    result = find_combination(*read_input())
    if result is not None:
        print(len(result))
        print(*result)
    else:
        print('-1')


if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
