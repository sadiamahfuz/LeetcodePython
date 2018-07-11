class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_two_numbers(list_node1, list_node2):
    return get_integer_value(list_node1) + get_integer_value(list_node2)


def get_integer_value(list_node):
    unit = 1
    value = 0

    while list_node is not None:
        value += unit * list_node.val
        list_node = list_node.next
        unit *= 10

    return value


if __name__ == "__main__":
    two = ListNode(2)
    four = ListNode(4)
    three = ListNode(3)

    two.next = four
    four.next = three
    three.next = None

    list1 = two

    five = ListNode(5)
    six = ListNode(6)
    one = ListNode(1)

    five.next = six
    six.next = one
    one.next = None

    list2 = five

    print(add_two_numbers(list1, list2))
