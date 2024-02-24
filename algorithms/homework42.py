"""This module represents my implementation of a single-linked list"""


class ListNode:
    """Each node stores the data and the pointer to the next node"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"ListNode with value: {self.value}"


class MyLinkedList:
    """Single-linked list"""
    def __init__(self):
        self._size: int = 0
        self._head = None

    def __str__(self):
        if self._size > 0:
            cur = self._head
            out = ""
            while cur:
                out += str(cur.value) + " >> "
                cur = cur.next
            return f"[ {out[:-4]} ]"
        else:
            return "Empty MyLinkedList"

    def is_empty(self) -> bool:
        """returns True if list is empty, else returns False"""
        return self._size == 0

    def get_size(self) -> int:
        return self._size

    def add(self, item):
        """adds an item to the head of the list"""
        new_node = ListNode(item)
        if self._head is None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    def search(self, item) -> bool:
        """returns True if an item is in list, else return False"""
        cur = self._head
        found = False
        while cur is not None and not found:
            if cur.value == item:
                found = True
            else:
                cur = cur.next
        return found

    def remove(self, item):
        """removes an item from the list"""
        if self.is_empty():
            raise ValueError("Removing from empty list")
        if self._head.value == item:
            self._head = self._head.next
            self._size -= 1
            return
        cur = self._head.next
        prev = self._head
        while cur is not None:
            if cur.value == item:
                break
            prev = cur
            cur = cur.next
        else:
            return
        prev.next = cur.next
        self._size -= 1

    # additional methods from task 1
    def append(self, item):
        """adds an item to the end of the list"""
        if self._head is None:
            self._head = ListNode(item)
            self._size += 1
            return
        cur = self._head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(item)
        self._size += 1

    def pop(self):
        """removes element from the top of the list and returns it (Value error if stack is empty)"""
        if self.is_empty():
            raise ValueError("Cannot pop from the empty stack")
        del_node = self._head
        self._head = self._head.next
        self._size -= 1
        return del_node.value

    def insert(self, position: int, item):
        """insert an item to the specified position in the list (0 < position < list size)"""
        if 0 < position < self._size:
            prev = self._head
            for i in range(position - 1):
                prev = prev.next
            new_node = ListNode(item)
            new_node.next = prev.next
            prev.next = new_node
            self._size += 1
        else:
            raise IndexError("position must be in range: 0 < position < list size")

    # implementation of slicing/indexing for my list
    def __getitem__(self, ndx):
        if isinstance(ndx, slice):
            begin, end = ndx.start, ndx.stop
            if begin < -self._size or begin >= self._size or end < -self._size or end >= self._size:
                raise KeyError("index out of range")
            if begin > end:
                raise KeyError("start index must be less than or equal stop")
            if begin < 0:
                begin = self._size + begin
            if end < 0:
                end = self._size + end
            new_list = MyLinkedList()
            cur = self._head
            counter = 0
            while cur is not None:
                if counter >= begin:
                    new_list.append(cur.value)
                if counter == end:
                    break
                cur = cur.next
                counter += 1
            return new_list
        elif isinstance(ndx, int):
            if ndx < -self._size or ndx >= self._size:
                raise KeyError("index out of range")
            index = ndx if ndx >= 0 else (self._size + ndx)
            cur = self._head
            for _ in range(index):
                cur = cur.next
            return cur.value
        else:
            raise TypeError("Incorrect index type")


if __name__ == "__main__":
    my_list = MyLinkedList()
    print(my_list)
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    print(my_list, "list size: ", my_list.get_size())
    print("Find 93 in list: ", my_list.search(93))
    my_list.remove(54)
    print("After removing 54", my_list, "list size: ", my_list.get_size())
    my_list.remove(93)
    print("After removing 93", my_list, "list size: ", my_list.get_size())
    my_list.remove(31)
    print("After removing 31", my_list, "list size: ", my_list.get_size())
    my_list.append(100)
    print("After appending 100", my_list, "list size: ", my_list.get_size())
    my_list.append(111)
    print("After appending 111", my_list, "list size: ", my_list.get_size())
    my_list.insert(1, 11)
    print("After inserting 11 at 1 position:", my_list, "list size: ", my_list.get_size())
    print("Indexing:", my_list[0], my_list[-1])
    print("Slicing:", my_list[2:4])
