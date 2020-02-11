# Problems:

# Create a new Python file and recreate the Node and SList classes - x
# Add the add_to_front method to your SList class - x
# Add the print_values method to your SList class - x
# Add the add_to_back method to your SList class
# Practice the above in code and on paper/whiteboard. Then try to write these methods from scratch without referencing the platform!
# Practice the above on your computer and on paper or a whiteboard. Then try to write these methods from scratch without referencing the platform!
# NINJA BONUS: complete the remove_from_front method
# remove_from_front(self) - remove the first node and return its value
# NINJA BONUS: complete the remove_from_back method
# remove_from_back(self) - remove the last node and return its value
# NINJA BONUS: complete the remove_val method
# remove_val(self, val) - remove the first node with the given value
# SENSEI BONUS: complete the insert_at method
# SENSEI BONUS: consider and account for edge cases for all previous methods

# Consider the following cases:
# the node with the given value is the first node
# the node with the given value is in the middle of the list
# the node with the given value is the last node

# insert_at(self, val, n) - insert a node with value val as the nth node in the list
# Consider the following cases:
# n is 0
# n is the length of the list
# n is between 0 and the length of the list

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

    def insert_at(self, val, n):
        if n == 0:
            return self.add_to_front(val)
        current = self.head
        new_node = Node(val)
        for i in range(n-1):
            if current.next == None:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return self

my_list = SList()
my_list.add_to_front('are').add_to_front('Linked Lists').add_to_back('fun!').print_values()
print("*"*50)
my_list.remove_from_front().print_values()
print("*"*50)
# my_list.remove_from_back().print_values()
my_list.remove_val('are').print_values()
print("*"*50)
my_list.insert_at('love coding', 1).print_values()