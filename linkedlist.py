class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
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
        return '-->'.join(linked_list)

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
        if self.head is None:
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
            if index > self.list_lenght():
                print('Given index does not exist, item added at the end of the list')
                self.add_at_the_end(data)
                break
            if index == 0:
                self.add_at_the_beginning(data)
                break
            # we have to stop at previous node to add new connection
            # new node is followed current.next
            # we insert new node between current node and the one after it
            if counter == index-1:
                new_node = Node(data, current.next)
                current.next = new_node
                break
            counter += 1
            current = current.next

    def delete_at_index(self, index):
        current = self.head
        counter = 0
        if index == 0:
            if self.list_lenght() > 1:
                self.head = self.head.next
                return
            else:
                self.head = None

        while current:
            if counter == self.list_lenght()-1:
                self.head = None
                break
            if counter == index - 1:
                current.next = current.next.next
                break
            counter += 1
            current = current.next

    def insert_list(self, list):
        for element in list:
            self.add_at_the_end(element)

    def get(self, index):
        counter = 0
        current = self.head
        while current:
            if counter == index:
                return current.data
            if index == -1:
                if current.next is None:
                    return current.data
            counter += 1
            current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_list([1, 2, 3, 4])
    print(ll.show_list())
