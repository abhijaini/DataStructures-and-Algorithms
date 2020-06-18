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
                        current_node = current_node.right
    def lookup(self, value):
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

    def printt(self, current_node):
        if current_node is not None:
            self.printt(current_node.left)
            print(current_node.value)
            self.printt(current_node.right)

    def remove(self, value):
        pass

    #         15
    #    10        20
    # 5     12  17    22
    # BFS should give [15, 10, 20, 5, 12, 17, 22] for above BST
    def BFS(self):
        if self.root is None:
            return(print("The tree is empty"))
        current_node = self.root
        tracker = []
        result = []
        tracker.append(current_node)
        while len(tracker) > 0:
            current_node = tracker[0]
            tracker.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                tracker.append(current_node.left)
            if current_node.right is not None:
                tracker.append(current_node.right)
        return result

    def BFS_recursive(self, tracker, result):
        if len(tracker) == 0:
            return result
        current_node = tracker[0]
        if current_node is None:
            return(print("The tree is empty"))
        tracker.pop(0)
        result.append(current_node.value)
        if current_node.left is not None:
            tracker.append(current_node.left)
        if current_node.right is not None:
            tracker.append(current_node.right)
        return self.BFS_recursive(tracker, result)

    #         15
    #    10        20
    # 5     12  17    22
    # DFS are three types
    # 1. Inorder  - [5,10,12,15,17,20,22]
    # 2. Preorder - [15,10,5,12,20,17,22] - used to recreate the tree
    # 3. Postorder - [5,12,10,17,22,20,15]

    def DFSInorder(self):
        return self.traverseInOrder(self.root, [])

    def traverseInOrder(self, current_node, result):
        if current_node.left is not None:
            self.traverseInOrder(current_node.left, result)
        result.append(current_node.value)
        if current_node.right is not None:
            self.traverseInOrder(current_node.right, result)
        return result

    def DFSPreorder(self):
        return self.traversePreOrder(self.root, [])

    def traversePreOrder(self, current_node, result):
        result.append(current_node.value)
        if current_node.left is not None:
            self.traversePreOrder(current_node.left, result)
        if current_node.right is not None:
            self.traversePreOrder(current_node.right, result)
        return result

    def DFSPostorder(self):
        return self.traversePostOrder(self.root, [])

    def traversePostOrder(self, current_node, result):
        if current_node.left is not None:
            self.traversePostOrder(current_node.left, result)
        if current_node.right is not None:
            self.traversePostOrder(current_node.right, result)
        result.append(current_node.value)
        return result


def main():
    b1 = BST()
    b1.insert(15)
    b1.insert(10)
    b1.insert(20)
    b1.insert(5)
    b1.insert(12)
    b1.insert(17)
    b1.insert(22)
    # b1.print_tree()
    print(b1.BFS())
    # print(b1.BFS_recursive([b1.root],[]))
    print(b1.DFSInorder())
    print(b1.DFSPreorder())
    print(b1.DFSPostorder())


if __name__ == '__main__':
    main()
