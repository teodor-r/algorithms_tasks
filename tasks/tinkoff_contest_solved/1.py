def read_input():
    _, s = map(int, input().split())
    costs = list(map(int, input().split()))
    return s, costs


def find_most_expensive_and_available(s, costs):
    most_expensive_and_available = 0
    for cost in costs:
        if most_expensive_and_available < cost <= s:
            most_expensive_and_available = cost
    return most_expensive_and_available


def main():
    print(find_most_expensive_and_available(*read_input()))


if __name__ == '__main__':
    main()
