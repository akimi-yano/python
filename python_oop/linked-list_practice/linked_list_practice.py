#Practiced Linked List

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

    def remove_from_front(self):
        if self.head == None:
            return self          
        current_head = self.head
        self.head = current_head.next
        return self

    def remove_from_back(self):
        runner = self.head
        if runner == None:
            return self
        while (runner.next.next != None):
            runner = runner.next
        runner.next = None
        return self

    def remove_val(self, val):
        runner = self.head
        if runner == None:
            return self
        if runner.val == val:
            self.head = self.head.next
            return self
        while (runner.next != None):
            next_node = runner.next.next
            if runner.next.val == val:
                runner.next = next_node
            runner = runner.next
        return self

    # def insert_at(self, val, n):
    #     if n == 0:
    #         return self.add_to_front(val)
    #     current = self.head
    #     new_node = Node(val)
    #     for i in range(n-1):
    #         if current.next == None:
    #             break
    #         current = current.next
    #     new_node.next = current.next
    #     current.next = new_node
    #     return self

    def insert_at(self, idx, val):
        if self.head is None or idx == 0:
            self.add_to_front(val)
        new_node = Node(val)
        runner = self.head
        node_idx = 0
        while node_idx<idx-1:
            if runner.next is None:
                self.add_to_back(val)
                return self
            runner = runner.next
            node_idx+=1
        new_node.next = runner.next
        runner.next = new_node
        return self

    def remove_at(self, idx):
        if self.head is None:
            print('Nothing is list to remove')
            return False
        if idx == 0:
            self.remove_from_front()
            return self
        runner = self.head
        node_idx = 0
        while node_idx<idx-1:
            if runner.next is None:
                print('Idx out of range')
                return False
            runner = runner.next
            node_idx += 1
        if runner.next.next is None:
            self.remove_from_back()
            return self
        runner.next = runner.next.next
        return self

    def remove_negs(self):
        #this method removes negative numbers
        if self.head is None:
            return False
        while self.head.val<0:
            self.remove_from_front()
        if self.head is None:
            return False
        runner = self.head
        while (runner.next is not None):
            if runner.next.val <0:
                if runner.next.next is None:
                    self.remove_from_back()
                    return self
                runner.next = runner.next.next
            else:
                runner = runner.next
        return self

my_list = SList()
my_list.add_to_front(3).add_to_back(5).add_to_front(1).add_to_back(7).print_values()
print('************') 
my_list.insert_at(2,9).print_values() # Insert_at works
print('************')
my_list.remove_at(2).print_values() # Remove_at works
print('************')
my_list.insert_at(2,-1).insert_at(2,-3).insert_at(2,-5).print_values()
print('************')
my_list.remove_negs().print_values()