class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node  = current_node.right


    def lookup(self,value):
        if self.root is None:
            print("The tree is empty")
            return False
        else:
            current_node = self.root
            while current_node is not None:
                if value == current_node.value:
                    return True
                elif value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            return False

    def print_tree(self):
        if self.root is None:
            return(print("The tree is empty"))
        else:
            self.printt(self.root)

    def printt(self,current_node):
        if current_node is not None:
            self.printt(current_node.left)
            print(current_node.value)
            self.printt(current_node.right)

    def remove(self,value):
        pass


def main():
    b1 = BST()
    b1.insert(15)
    b1.insert(10)
    b1.insert(20)
    b1.insert(5)
    b1.insert(12)
    b1.insert(17)
    b1.insert(22)
    b1.print_tree()


if __name__ == '__main__':
    main()

