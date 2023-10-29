def union_gangs(x, y):
    x_g = spirits.get(x).get('current_gang')
    y_g = spirits.get(y).get('current_gang')
    global MNG
    if x_g != y_g:
        current_number_gang = MNG + 1

        gangs[current_number_gang] = gangs[x_g] + gangs[y_g]

        for member_gang in gangs[current_number_gang]:
            spirits[member_gang]['count'] += 1
            spirits[member_gang]['current_gang'] = current_number_gang

        MNG = current_number_gang
        plag()

def plag():
    pass

def one_gane(x, y):
    x_gang = spirits.get(x).get('current_gang')
    y_gang = spirits.get(y).get('current_gang')
    if x_gang == y_gang:
        print("YES")
    else:
        print("NO")


def get_num_bands(x):
    print(spirits.get(x).get('count'))


n, m = map(int, input().split())
MNG = n

gangs = {
    i: [i] for i in range(1, n+1)
}

spirits = {
   i: { 'count': 1, 'current_gang': i} for i in range(1, n+1)
}

for i in range(m):
    input_numbers = list(map(int, input().split()))
    task_type = input_numbers[0]
    if task_type == 1:
        union_gangs(input_numbers[1], input_numbers[2])
    elif task_type == 2:
        one_gane(input_numbers[1], input_numbers[2])
    elif task_type == 3:
        get_num_bands(input_numbers[1])
