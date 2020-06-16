class Node ():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def Dprint(self):
        if self.Disempty():
            print("The list is empty")
            return
        temp = self.head
        while temp is not None:
            if temp.next is not None:
                print("{} <=> ".format(temp.value), end="")
            else:
                print(temp.value)
            temp = temp.next



    def Dpop(self):
        if self.Disempty():
            print("The list is empty")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        # self.tail.prev = None
        
        self.tail.next = None

    def Ddelete(self,index):
        if self.Disempty():
            return(print("List is already empty"))
        elif index > self.Dsize():
            return(print("Index is out of range. Please check"))
        elif self.Dsize() == 1:
            self.head = None
            self.tail = None
            return
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        elif index == self.Dsize() - 1 :
            self.tail = self.tail.prev
            self.tail.next = None
            return
        else:
          


            temp = self.head
            count = 0
            while count != index:
                count += 1
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev


    def Dinsert(self,value,index):
        
        
        if index == 0 :
            self.Dprepend(value)
            return
        if self.Dsize() == index:
            self.Dappend(value)
            return
        if (self.Dsize()-1) < index:
            print("List size is {}, while you are trying to insert at index {}".format(self.Dsize(),index))
            return
        new_node = Node(value)
        temp = self.head
        count = 0
        while count != index:
            count += 1
            temp = temp.next
        new_node.prev = temp.prev
        new_node.next = temp
        temp.prev.next = new_node
        # temp.next = None

    def Dappend(self,value):
        temp_node = Node(value)
        if self.Disempty():
            self.head = temp_node
            self.tail = temp_node
        else:
            temp_node.prev = self.tail
            self.tail.next = temp_node
            self.tail = temp_node
            

    def Dprepend(self,value):
        if self.Disempty():
            self.Dappend(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node

    def Disempty(self):
        if self.head == None:
            return True
    
    def Dsize(self):
        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            count += 1
        return count

def main():
    dl = DoublyLinkedList()
    # dl.Dprint()
    # dl.Dappend(2)
    # dl.Dpop()
    # dl.Dprint()
    # dl.Dappend(3)
    # dl.Dprint()
    # dl.Dpop()
    # dl.Dprint()
    # dl.Dappend(4)
    # dl.Dappend(7)
    # dl.Dprint()
    # dl.Dpop()
    # dl.Dprint()
    # # dl.Dprint()
    # # print(dl.Dsize())
    # dl.Dprepend(1)
    # dl.Dprepend(0)
    # # dl.Dappend(3)
    
    # dl.Dprint()
    # print(dl.Dsize())
    

    # dl.Dinsert("test",1)
    # dl.Dinsert("foo",4)
    
    # dl.Dprint()
    
    # dl.Dinsert("test",3)
    # dl.Dprint()



    dl.Dappend(1)
    dl.Dappend(2)
    dl.Dappend(5)
    dl.Dprint()
    dl.Ddelete(1)
    dl.Dprint()
    dl.Ddelete(0)
    dl.Ddelete(5)
    dl.Dprint()
    # print(dl.Dsize())

    dl.Ddelete(0)
    dl.Dprint()

if __name__== "__main__":
    main()