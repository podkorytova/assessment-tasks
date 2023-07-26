class Node:
    def __init__(self, data_val):
        self.data_val = data_val
        self.next_val = None


class SLinkedList:
    def __init__(self):
        self.head_val = None

    def fill_list(self, data):
        self.head_val = Node(data[0])
        current = self.head_val
        for i in range(1, len(data)):
            current.next_val = Node(data[i])
            current = current.next_val

    def search_middle_element(self):
        priv_element = self.head_val
        middle_element = self.head_val
        current_element = self.head_val
        count = 0
        while current_element.next_val is not None:
            count += 1
            if count % 2 != 0:
                current_element = current_element.next_val
                priv_element = middle_element
                middle_element = middle_element.next_val
            else:
                current_element = current_element.next_val
        return priv_element, middle_element

    def delete_element(self, priv, middle):
        if priv == middle:
            self.head_val = None
        elif middle.next_val is None:
            self.head_val = middle
        else:
            priv.next_val = middle.next_val

    def list_print(self):
        print_val = self.head_val
        if print_val is None:
            print("Your list is empty")
        else:
            while print_val is not None:
                print(print_val.data_val)
                print_val = print_val.next_val


current_list = SLinkedList()
input_data = input("Input data:").split(" ")
current_list.fill_list(input_data)
previous, middle = current_list.search_middle_element()
current_list.delete_element(previous, middle)
current_list.list_print()
