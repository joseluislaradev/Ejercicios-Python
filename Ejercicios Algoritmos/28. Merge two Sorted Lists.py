class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def merge_two_sorted_lists(list1, list2):
    
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
        else: 
            tail.next = list1
            list1 = list1.next
          
        tail = tail.next
        
    while list1:
          tail.next = list1
          list1 = list1.next
          tail = tail.next
    
    while list2:
          tail.next = list2
          list2 = list2.next
          tail = tail.next

    
    return dummy.next
    


def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


assert to_list(
    merge_two_sorted_lists(
        build_list([1, 2, 4]),
        build_list([1, 3, 4])
    )
) == [1, 1, 2, 3, 4, 4]

assert to_list(
    merge_two_sorted_lists(
        build_list([]),
        build_list([])
    )
) == []

assert to_list(
    merge_two_sorted_lists(
        build_list([]),
        build_list([0])
    )
) == [0]

assert to_list(
    merge_two_sorted_lists(
        build_list([1]),
        build_list([2])
    )
) == [1, 2]

print("All tests passed!")