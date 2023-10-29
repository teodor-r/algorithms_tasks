from collections import deque
from operator import itemgetter, attrgetter
items_deque = deque()
items_in_cell = deque()
commands_deque = deque()
mas   = [int(num) for num in input().split()] # otseki
n = mas[0]
m = mas[1]

class  Cell():
    counter =1
    def  __init__(self, capacity):
        self.capacity = capacity
        self.rest_capacity = capacity
        self.index = Cell.counter
        Cell.counter+=1
    def append(self, weight):
        self.rest_capacity-= weight
    def __repr__(self):
        return f"|{self.index }, {self.rest_capacity}, {self.capacity}|"

class Item():
    counter = 1
    def __init__(self,weight, st,et):
        self.weight= weight
        self.start_time = st
        self.end_time = et
        self.index_cell = None
        self.cell = None
        self.index = Item.counter
        Item.counter+=1
    def put_item(self, cell):
        self.cell = cell
        self.index_cell = cell.index
        cell.append(self.weight)
        commands_deque.append(f"put cargo {self.index} to cell {self.index_cell}")
    def move_item(self, cell_dest):
        commands_deque.append(f"move cargo {self.index} from cell {self.index_cell} to cell {cell_dest.index}")
        self.cell.rest_capacity =+ self.weight
        cell_dest.append(item.weight)
        self.index_cell = cell_dest.index
        self.cell = cell_dest
    def take_item(self):
        commands_deque.append(f"take cargo {self.index} from cell {self.index_cell}")
        self.cell.rest_capacity =+ self.weight
    def  not_be_stored(self):
        commands_deque.append(f"cargo {self.index} cannot be stored")
    def __repr__(self):
        return f"class Item, index: {self.index}"

cell_list = [Cell(int(s)) for s in input().split()]

for i in range(m):
    items_deque.append(Item(*[int(s) for s in input().split()]))

max_end_time = max(items_deque, key = lambda item: item.end_time).end_time
max_start_time = max(items_deque, key = lambda item: item.start_time).start_time

def put_in_cell(item):
    cell_list_sorted = sorted(cell_list, key=attrgetter('rest_capacity', 'index'))
    #if  len(cell_list_sorted) ==0:
    for cell in  cell_list_sorted:
        if cell.rest_capacity - item.weight >=0:
            item.put_item(cell)
            items_in_cell.append(item)
            return True
    list_movement = []
    for item_in_cell in items_in_cell:
        index_cell_from = item_in_cell.index_cell
        current_cell = item_in_cell.cell
        for cell_dest in  cell_list:
            if cell_dest.index == index_cell_from:
                continue
            if current_cell.rest_capacity + item_in_cell.weight >= item.weight and  cell_dest.rest_capacity>=item_in_cell.weight:
                movement = (item_in_cell.weight,current_cell.rest_capacity+ item_in_cell.weight,
                            cell_dest.rest_capacity - item_in_cell.weight,
                            item_in_cell.index, cell_dest.index,index_cell_from,current_cell,cell_dest,item_in_cell)
                list_movement.append(movement)
    if len(list_movement) ==0:
        return False
    else:
        list_movement.sort()
        list_movement[0][-1].move_item(list_movement[0][-2])
        item.put_item(list_movement[0][-3])
        items_in_cell.append(item)
        return True


for time  in range(1,max_start_time+1):
    items_to_remove = filter(lambda item: (item.end_time == time),items_in_cell)
    for item in list(items_to_remove):
        item.take_item()
        items_in_cell.remove(item)
    items_to_append = filter(lambda item: (item.start_time == time),items_deque)
    for item in list(items_to_append):
        if not put_in_cell(item):
            item.not_be_stored()
        items_deque.popleft()

for rest_item in sorted(items_in_cell, key=attrgetter('end_time')):
    rest_item.take_item()

for i in range(len(commands_deque)-1):
    print(commands_deque.popleft())
print(commands_deque.popleft(),end='')











