class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dictionary = {}
        self.front = None
        self.back = None

    def get(self, key: int):
        if key in self.dictionary:
            self.shift_node(self.dictionary[key])

            return self.dictionary[key].value

        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.dictionary:
            self.shift_node(self.dictionary[key])
            self.dictionary[key].value = value

        else:

            node = Node(key, value)
            self.dictionary[key] = node

            if self.size == 0:
                self.front = node
                self.back = node
                self.size += 1

            elif self.size < self.capacity:
                self.front.next = node
                node.prev = self.front
                self.front = node
                self.size += 1

            elif self.size == self.capacity:
                tail_key = self.back.key

                if self.capacity == 1:
                    self.front = node
                    self.back = node

                else:
                    node.prev = self.front
                    self.front.next = node
                    self.front = node
                    self.back = self.back.next
                    self.back.prev = None

                self.dictionary.pop(tail_key)

    def shift_node(self, node):

        if node is self.front:
            return

        else:

            if node.next is not None and node.prev is not None:
                node.next.prev = node.prev
                node.prev.next = node.next

            if node is self.back:
                self.back = node.next
                self.back.prev = None

            self.front.next = node
            node.prev = self.front
            node.next = None
            self.front = node
