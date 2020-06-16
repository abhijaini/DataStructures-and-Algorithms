# Create node class for linked list
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

# Create Linked List class
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None


#print entire Linked List
    def Lprint(self):
        if self.isempty():
            print("There is nothing to print; the Linked List is empty")
            return
        temp = self.head
        # print("head = {} ".format(self.head.value), end="")
        print("Printing the linked list...")
        while temp is not None:
            if temp.next is not None:
                print("{} --> ".format(temp.value),end="")
            else:
                print(temp.value)
            temp = temp.next
        # print("tail = {}".format(self.tail.value), end="")

#Add/append a node in the Linked List
    def Lappend(self,value):
        new_node = Node(value)
        # print("Appending {} to the list".format(value))
        if self.isempty(): # check if list is empty
            self.head = new_node
            self.tail = new_node
            # self.Lprint()
        else:
            self.tail.next = new_node
            self.tail = new_node
            # self.Lprint()

#Delete a node based on the value passed and print the new list
    def Ldelete(self,value):
        if self.isempty():
            print("The list is empty")
            return
        # print("Searching {} in the list....".format(value))
        if self.head.value == value:        
            self.head = None
            self.tail = None
            # print("Deleted {} from the list".format(value))
            self.Lprint()
            return
        temp = self.head
        found = False
        while temp.next is not None:
            last_temp = temp
            temp = temp.next
            if temp.value == value:
                last_temp.next = temp.next
                temp.next = None
                # print("Deleted {} from the list".format(value))
                found = True
                break
            # temp = temp.next
        if found == False:
            print("Node with value {} couldn't be found in the list".format(value))
        self.Lprint()
            

#Pop the last value from the list and print the new list
    def Lpop(self):
        # print("Deleting last Node...")
        if self.isempty(): # check if list is empty
            print("The linked list is already empty")
            return
        elif self.head == self.tail: # check if only one node
            self.head = None
            self.tail = None
            self.Lprint()
            return

        temp = self.head # if more than one node
        while temp.next is not self.tail:
            temp = temp.next
        temp.next = None
        self.Lprint()

#Prepend a node and print the new list
    def Lprepend(self,value):
        # print("Prepending {} to the list".format(value))
        if self.isempty():
            self.Lappend(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        # self.Lprint()

#Insert a node at an index and print the new list
    def Linsert(self, value, index):
        # print("Inserting {} at index {}".format(value,index))
        if index == 0:
            self.Lprepend(value)
            return
        if self.Lsize() == index:
            self.Lappend(value)
            return
        if (self.Lsize()-1) < index:
            print("List size is {}, while you are trying to insert at index {}".format(self.Lsize(),index))
            return
        
        count = 0
        temp = self.head
        new_node = Node(value)
        while count < index-1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node
        # self.Lprint()

    def Lsize(self):
        count = 0
        temp = self.head
        while(temp is not None):
            count += 1
            temp = temp.next
        return count


#Reverse the list
    def Lreverse(self):
        # temp_list = LinkedList()
        first = self.head
        self.tail = first
        second = first.next
        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return
            

    def isempty(self):
        if self.head == None:
            return True
    


def main():
    l1 = LinkedList()
    l1.Lappend(3)
    # l1.Lpop()
    l1.Lappend(4)
    l1.Lappend(5)
    l1.Lappend(7)
    l1.Lappend(10)
    # # l1.Lprepend(1)
    # # l1.Lprepend(1)
    # # l1.Lprepend(2)
    
    # # l1.Ldelete(3)
    # l1.Linsert("test",2)
    # l1.Linsert("test",0)
    # print(l1.Lsize())
    # l1.Linsert("test",6)
    # l1.Linsert("test",1)
    # l1.Linsert("test",4)
    # l1.Linsert("test",5)
    # l1.Linsert("test1",5)
    l1.Lprint()
    l1.Lreverse()
    l1.Lprint()
    
if __name__ == "__main__":
    main()
    
