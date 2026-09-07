# Te dan:

# 1 → 2 → 3 → 4 → None

# Debes devolver:

# 4 → 3 → 2 → 1 → None

# No debes crear otra lista con los valores.

# La intención es modificar los next existentes.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    previous = None
    
    while head:
        next_node = head.next
        head.next = previous
        previous = head
        head = next_node
    
    return previous
    
def print_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


# 1 → 2 → 3 → 4
head = ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4))))

result = reverse_list(head)
print_list(result)
# [4, 3, 2, 1]

head = ListNode(5)

result = reverse_list(head)
print_list(result)
# [5]
result = reverse_list(None)
print_list(result)
# []