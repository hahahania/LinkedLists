class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        if self.head == None:
            print('The list is empty')

        current = self.head
        linked_list = []
        # while self.head is not None
        while current:
            linked_list.append(str(current.data))
            current = current.next
        print('-->'.join(linked_list))

    def list_lenght(self):
        counter = 0
        current = self.head
        # until self.head is None function is adding 1 to counter
        # if self.head == None, returned counter == 0 --> list is empty
        while current:
            counter += 1
            current = current.next
        return counter

    def add_at_the_beginning(self, data):
        # our current self.head has to be next element of the node
        self.head = Node(data, self.head)

    def add_at_the_end(self, data):
        # creating node if there aren't any
        if self.head == None:
            self.head = Node(data)
            return

        current = self.head
        # iterating through nodes until we find the end (when self.next == None)
        while current.next:
            current = current.next
        # adding new node at the end of linked list
        current.next = Node(data)

    def insert_at_index(self, data, index):
        current = self.head
        counter = 0
        while current:
            # we have to stop at previous node to add new connection
            # new node is followed current.next
            # we insert new node between current node and the one after it
            if counter == index-1:
                new_node = Node(data, current.next)
                current.next = new_node
                break
            counter += 1
            current = current.next

    def deleting_at_index(self, index):
        current = self.head
        counter = 0
        if index == 0:
            self.head = self.head.next
        while current:
            if counter == index - 1:
                # next element has to be omitted
                current.next = current.next.next
                break
            counter += 1
            current = current.next

    # adding more than one elements from list
    def insert_list(self, list):
        for element in list:
            self.add_at_the_end(element)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_list([1, 2, 3, 4, 5])
    linked_list.show_list()
