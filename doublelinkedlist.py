class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        if self.head is None:
            print('The list is empty')

        current = self.head
        linked_list = []
        # while self.head is not None
        while current:
            linked_list.append(str(current.data))
            current = current.next
        print('<-->'.join(linked_list))

    def list_length(self):
        counter = 0
        current = self.head
        # until self.head is None function is adding 1 to counter
        # if self.head == None, returned counter == 0 --> list is empty
        while current:
            counter += 1
            current = current.next
        return counter

    def add_at_the_beggining(self, data):
        self.head = Node(data, next=self.head)

    def add_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, prev=self.head)
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data, prev=current)

    def insert_at_index(self, data, index):
        current = self.head
        counter = 0
        while current:
            if index == 0:
                self.add_at_the_beggining(data)
                break

            if counter == index-1:
                new_node = Node(data, prev=current, next=current.next)
                current.next = new_node
                break

            counter += 1
            current = current.next

    def delete_at_index(self, index):
        current = self.head
        counter = 0
        if index == 0:
            if self.list_length() > 1:
                self.head = self.head.next
                return
            else:
                self.head = None
                return

        while current:
            if counter == self.list_length()-1:
                self.head = None
                break
            if counter == index - 1 and index < self.list_length()-1:
                current.next = current.next.next
                break
            if counter == index - 1 and index == self.list_length() - 1:
                current.next = None
            counter += 1
            current = current.next

    def insert_list(self, list):
        for element in list:
            self.add_at_the_end(element)
