class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stacks():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def lookup(self):
        pass

    def pop(self):
        if self.isEmpty():
            return("Print Stack is already empty")
        elif self.top == self.bottom:
            self.top = None
            self.bottom = None
            self.length -= 1
            return
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length -= 1

    def push(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.bottom = new_node
            self.top = new_node
            self.length += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1
        return self

    def peek(self):
        return self.top.value

    def isEmpty(self):
        if self.top is None and self.bottom is None:
            return True

    def print_stack(self):
        if self.top is None:
            return(print("The stack is empty"))
        print("Printing Stack..")
        temp = self.top
        while temp is not None:
            if temp == self.bottom:
                print("|{}|".format(temp.value))
            else:
                print("|{}|".format(temp.value))

            temp = temp.next


def main():
    S1 = Stacks()
    S1.push(5)
    # print(S1.isEmpty())
    S1.print_stack()
    S1.push(7)
    S1.print_stack()
    S1.push(17)
    S1.print_stack()
    S1.pop()
    S1.print_stack()
    S1.pop()
    S1.print_stack()
    S1.pop()
    S1.print_stack()
    S1.pop()
    S1.print_stack()
    S1.print_stack()
    # print(S1.top.value)
    # print(S1.bottom.value)


if __name__ == "__main__":
    main()
