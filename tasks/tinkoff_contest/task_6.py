def union_gangs(x, y):
    global MAX_NUMBER_GANG
    x_gang = spirits.get(x).get('current_band')
    y_gang = spirits.get(y).get('current_band')
    if x_gang != y_gang:
        current_number_gang = MAX_NUMBER_GANG + 1

        gangs[current_number_gang] = gangs[x_gang] + gangs[y_gang]

        for member_gang in gangs[current_number_gang]:
            spirits[member_gang]['changes'] += 1
            spirits[member_gang]['current_band'] = current_number_gang

        MAX_NUMBER_GANG = current_number_gang


def are_spirits_in_same_gang(x, y):
    x_gang = spirits.get(x).get('current_band')
    y_gang = spirits.get(y).get('current_band')
    if x_gang == y_gang:
        print("YES")
    else:
        print("NO")


def get_number_of_gangs(x):
    print(spirits.get(x).get('changes'))


n, m = map(int, input().split())
MAX_NUMBER_GANG = n

gangs = {
    i: [i] for i in range(1, n+1)
}

spirits = {
   i: {
       'changes': 1, 'current_band': i
   } for i in range(1, n+1)
}


for i in range(m):
    input_numbers = list(map(int, input().split()))
    task_type = input_numbers[0]
    if task_type == 1:
        union_gangs(input_numbers[1], input_numbers[2])
    elif task_type == 2:
        are_spirits_in_same_gang(input_numbers[1], input_numbers[2])
    elif task_type == 3:
        get_number_of_gangs(input_numbers[1])
