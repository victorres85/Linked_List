from node import Node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def remove_all_node(self, value_to_remove):
        self.value_to_remove = value_to_remove
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if current_node.get_next_node() == None:
                    current_node = None
                elif next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    if current_node.get_next_node() == None:
                        current_node = None
                    else:
                        current_node = next_node
                else:
                    current_node = next_node


def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')

    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    if val1 == val2:
        print("Elements are the same - no swap needed")
        return  # "Elements are the same - no swap needed"

    while node1 is not None:
        if node1.get_value() == val1:
            break
        else:
            node1_prev = node1
            node1 = node1.get_next_node()
    while node2 is not None:
        if node2.get_value() == val2:
            break
        else:
            node2_prev = node2
            node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return

    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


def find_middle(linked_list):
    middle_node = linked_list.get_head_node()
    head_node = linked_list.get_head_node()
    count = 0
    while head_node.get_next_node():
        head_node = head_node.get_next_node()
        if count % 2 != 0:
            middle_node = middle_node.get_next_node()
        count = count + 1
    return middle_node


def nth_last_node(linked_list, n):
    count = 1
    last_position = linked_list.get_head_node()
    n_position = None
    last_position_found = 0

    while last_position.get_next_node():

        if n != last_position.get_value():
            last_position = last_position.get_next_node()
        else:
            n_position = count
            if last_position.get_next_node():
                last_position = last_position.get_next_node()
            else:
                break

        count = count + 1
    return n_position


teste = LinkedList()
teste.insert_beginning(1)
teste.insert_beginning(2)
teste.insert_beginning(3)
teste.insert_beginning(4)
# teste.insert_beginning(5)
# teste.insert_beginning(6)
# teste.insert_beginning(7)
# teste.insert_beginning(8)
# teste.insert_beginning(5)
# teste.insert_beginning(7)
# teste.insert_beginning(5)
# teste.insert_beginning(7)
# teste.insert_beginning(9)


print(teste.stringify_list())
print('\n')
swap_nodes(teste, 1, 3)
print(teste.stringify_list())

print(nth_last_node(teste, 3))
