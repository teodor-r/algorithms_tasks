"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""
from collections import  deque
class Node:
    def __init__(self):
        self.next_node =None
        self.value = None

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
        print(linked_list.value)
        linked_list = linked_list.next_node

def merge_linked_lists(fL, sL):
    if fL.value >= sL.value:
        first_node =  sL
        sL = sL.next_node
    else:
        first_node = fL
        fL = fL.next_node
    first_node.next_node = None
    reference_to_fn = first_node
    while fL!=None and sL!=None:
        #print_chain(first_node)
        if fL.value >= sL.value:
            reference_to_fn.next_node = sL
            reference_to_fn = sL
            sL = sL.next_node
        else:
            reference_to_fn.next_node = fL
            reference_to_fn = fL
            fL = fL.next_node
        reference_to_fn.next_node = None
    if  fL==None:
        reference_to_fn.next_node = sL
    else:
        reference_to_fn.next_node = fL
    return  first_node




first_chain = convert_from_list_to_linked_list([1,2,3,4])
second_chain = convert_from_list_to_linked_list([3,4,5,6,7])

print_chain(merge_linked_lists(first_chain,second_chain))


