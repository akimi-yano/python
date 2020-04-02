class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None

class SList:
    def __init__ (self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node 
        return self

    def print_values(self):
        runner = self.head
        while (runner!=None):
            print(runner.val)
            runner=runner.next
        return self

    def add_to_back(self, val):
        new_node = Node(val)
        runner = self.head
        while (runner.next!=None):
            runner = runner.next
        runner.next = new_node
        return self
        
    def is_circle(self):
        if self.head is None:
            return False
        if self.head.next is None:
            return False
        runner1=self.head
        runner2=self.head.next
        while runner1!=runner2:
            if runner2 is None:
                return False
            if runner2.next is None:
                return False
            elif runner2.next is not None: 
                runner2 = runner2.next.next
                runner1 = runner1.next
                if runner1 == runner2:
                    return True
        return False
    
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)

new_list = SList()
new_list.add_to_front(1).add_to_front(2).add_to_front(3).add_to_front(4).add_to_front(5).print_values()

runner = new_list.head

while runner.next != None:
    runner = runner.next
runner.next = new_list.head.next.next    

print(new_list.is_circle())
    