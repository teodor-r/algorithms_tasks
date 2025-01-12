class Node:
    def __init__(self):
        self.next_node =None
        self.value = None
        self.trace_ten = False

def convert_from_list_to_linked_list(array):
    if len(array) ==0:
        return Node()
    prev_node = Node()
    first_node = prev_node
    prev_node.value = array[0]
    for i in range(1,len(array)):
        node  = Node()
        prev_node.next_node = node
        node.value = array[i]
        prev_node = node
    return first_node

def print_chain(linked_list):
    while linked_list != None:
        print(linked_list.value, end=' ')
        linked_list = linked_list.next_node

def solution():
    s1 = [9,9,9,9,9,9,9]
    s2 = [8,2,1,2]
    num1_first  = convert_from_list_to_linked_list(s1)
    num2_first = convert_from_list_to_linked_list(s2)
    if len(s1) < len(s2):
        num1_first , num2_first = num2_first, num1_first
    extract_digit = lambda x: x%10
    mirror_num1_first = num1_first
    while num1_first!=None:
        if num2_first!= None:
            sum_digits = num1_first.value + num2_first.value
        else:
            sum_digits = num1_first.value

        if sum_digits >=10:
            if  num1_first.next_node!= None:
                num1_first.next_node.value +=1
            else:
                node = Node()
                node.value = 1
                num1_first.next_node = node
        num1_first.value = extract_digit(sum_digits)
        print(num1_first.value)
        num1_first = num1_first.next_node
        if  num2_first!= None:
            num2_first = num2_first.next_node

    print_chain(mirror_num1_first)
solution()
