# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self,name):
        self.name = name
        self.next = None
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    
    def __init__(self):
        self.head = None 

    def add_front(self,name):
        new_node = Node(name)
        new_node.next = self.head 
        self.head = new_node 
        print(f"{name} has been added to the front of the waitlist.") 

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node 
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_node
        print(f"{name} has been added to the end of the waitlist.")
    
    def remove(self, name):
        current = self.head 
        prev = None 
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"{name} was removed from the waitlist.")
                return
            prev = current 
            current = current.next 
        print(f"{name} was not found in the waitlist.") 

    def print_list(self):
        if not self.head:
            print("The waitlist is empty.")
            return
        current = self.head 
        position = 1 
        while current:
            print(f"{position}. {current.name}")
            current = current.next
            position += 1
            
                
                    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method 
            waitlist.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method 
            waitlist.add_end(name)
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method 
            waitlist.remove(name)
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method. 
            waitlist.print_list()
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program 
if __name__ == "__main__":
    waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- My list works as a singly linked list, this list is used to store the customers name and a connecting piece to the next node. This type of list is very beneficial as it makes adding and removing from the front of the list a quick and easy function, it also makes the list work as a chain of sorts having one customer lead to the next. 
- The head plays a very important role as it is acting as the very beginning to our list without it the whole chain of customers will break causing massive issues within my code. The head is also something that is being changed by updating the list with new names and replacing with old ones when the current head is removed. If the current head is removed the next name in line will move up as the new head of the list preventing there from being no head. 
- A custom list like this could be used by a real engineer for something like a custom database or as it is being used now as an educational tool to teach others about how to operate and build code for lists like this. Another use case of this could be if you have a database that has elements that are constantly moving around. 
'''
