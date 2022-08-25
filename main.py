from time import sleep
from linked_list import *
list = None


def if_empty():
    print(
        "No Linked List has been created so far, please start by entering values to your linked list")
    sleep(1)
    LinkedList_value = input(
        "Enter the head element of your linked list:   ")
    list = LinkedList(LinkedList_value)
    while True:
        keep_going = input(
            'Would you like to add a new value to your list?(y/n)   ').lower()
        if keep_going == 'y':
            LinkedList_value = input(
                "Enter the head element of your linked list:   ")
            list.insert_beginning(LinkedList_value)
        else:
            break
    return list


while True:
    print(
        '''
    Your Linke_List!

    What would you like to do?

    1. view the linked list
    2. add element at the beggining of the list
    3. remove node from the list
    4. remove all nodes which contain a value from the list
    5. Swap elements on the list
    6. find middle element of the list
    7. find Nth element on the list

    '''
    )

    option = input("Enter action you want to take:   ")
    if option == '1':
        if list == None:
            list = if_empty()
        else:
            print("Your Linked List contain the following values: \n")
            print(list.stringify_list())
            sleep(3)

    elif option == '2':
        if list == None:
            LinkedList_value = input(
                "Enter the head element of your linked list:   ")
            list = LinkedList(LinkedList_value)
        else:
            LinkedList_value = input(
                "Enter the head element of your linked list:   ")
            list.insert_beginning(LinkedList_value)
            sleep(3)

    elif option == '3':
        if list == None:
            list = if_empty()
        else:
            LinkedList_value = input(
                "Enter the value to be removed (remember only the first match will be removed):   ")
            list.remove_node(LinkedList_value)
            sleep(3)

    elif option == '4':
        if list == None:
            list = if_empty()
        else:
            LinkedList_value = input(
                "Enter the value to be removed from your list:   ")
            list.remove_all_node(LinkedList_value)
            sleep(3)

    elif option == '5':
        if list == None:
            list = if_empty()
        else:
            LinkedList_value1 = input(
                "Enter the first value to be swaped:   ")
            LinkedList_value2 = input(
                "Enter the second value to be swaped:   ")
            swap_nodes(list, LinkedList_value1, LinkedList_value2)
            sleep(3)

    elif option == '6':
        if list == None:
            list = if_empty()
        else:
            find_middle(list)
            sleep(3)

    elif option == '7':
        if list == None:
            list = if_empty()
        else:
            LinkedList_value = input(
                "Enter the value to be found:   ")
            position = nth_last_node(list, LinkedList_value)
            print(
                f'the value which you have searched, has been found at position {position}')
            sleep(3)
