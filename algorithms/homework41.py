
class Node:
    """Node for my implementation of stack"""
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """My implementation of stack based on single-linked list"""
    def __init__(self):
        self._top: Node = Node("top")
        self._size: int = 0

    def __str__(self) -> str:
        cur = self._top.next
        out = ""
        while cur:
            out += str(cur.value) + " >> "
            cur = cur.next
        return out[:-4]

    def get_size(self) -> int:
        """returns size of the stack"""
        return self._size

    def is_empty(self) -> bool:
        """returns True if stack is empty, else return False"""
        return self._size == 0

    def peek(self):
        """returns the value of the top of the stack (Value error if stack is empty)"""
        if self.is_empty():
            raise ValueError("Cannot peek from the empty stack")
        return self._top.next.value

    def push(self, value):
        """adds element to the stack"""
        new_node = Node(value)
        new_node.next = self._top.next
        self._top.next = new_node
        self._size += 1

    def pop(self):
        """removes element from stack and returns it (Value error if stack is empty)"""
        if self.is_empty():
            raise ValueError("Cannot pop from the empty stack")
        del_node = self._top.next
        self._top.next = self._top.next.next
        self._size -= 1
        return del_node.value


if __name__ == "__main__":
    # task 1
    stack = Stack()
    for c in input("Enter some text to reverse: "):
        stack.push(c)
    for _ in range(stack.get_size()):
        print(stack.pop(), end="")
