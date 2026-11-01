class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Contact Name: {self.name}\n Contact Number: {self.number}" 
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

class Node:
    def __init__(self, key, value):
        self.key = key #The key assciated with the contact which would be the name.
        self.value = value #The contact stored in this node
        self.next = None #Points to the next node in the list. Currently it points at nothing.
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            print(char, ord(char))
            total += ord(char)
        print(f"TOTAL: {total}")
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        if self.data[index] is None:
            self.data[index] = Node(key,value)
            return

        while current:
            if current.key == key: #If the key equals another. This means it is a duplicate
                current.value = value
                return

            if current.next is None:
                break #Break statement helps it stop at the last node.

            current = current.next
        current.next = Node(key, value) #Creates a new node that gets added to the end of the list. with the key/value pair.
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            if self.data[index] is None:
                print(f"Index {index}: Empty")
            else:
                current = self.data[index]
                while current:
                    print(f"Index {index}: {current.key} -> {current.value}")
                    current = current.next

    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
table = HashTable(size=10) #Had to specify the size of the hash table when creating the instance.
#Inserting Data Into the Table
table.insert("Deriya Wilson", "252-254-2265")
print("Inserting Deriya Wilson....")
print()

table.insert("Laila Hamilton", "414-541-2341")
print("Inserting Laila Hamilton....")
print()

table.insert("Reese Constamas", "312-802-7412")
print("Inserting Reese Constamas....")
print()

print("Printing the hash table:")
table.print_table()

#Searching for data in the table
contact = table.search("Deriya Wilson")
print("\nSearch Result:", contact)

#Updating duplicates
table.insert("Laila Hamilton", "414-398-8141") #Should update this contact with the new phone number
table.print_table()

#Search for a value that's not in the table
print(table.search("Talia")) #Should be none because I don't have a contact with this name.


'''
Deriya's Writer's Memo

1) Why is a hash table the right structure for fast lookups?
- A hash table is the right structure for fast lookups because it allocates memory for speed, in order to provide constant-time access to elements based on their keys.
- They do this with a hash function. First the key gets converted into an index within the array, then the index tells the program where to place the value.
- This process occurs quickly, ensuring that speed of access remains constant regardless of the size of the table. Even if the table grows, the time to retrieve an element stays the same.

2) How did you handle collisions?
- I handled collusions by using separate chaining, each index has a linked list to store multiple key-value pairs that hash to the same index.
- If there was a key value pair with the same name already in the table, I would update the existing value with the new one to avoid duplicates and keep data in place.

3) When might an engineer choose a hash table over a list or tree?
- An engineer might choose a hash table over a list or tree when they need fast lookops, to store and retrive data efficently, when they want to update or delete elements quickly, and when the order of elements isn't important.
- Hash tables are particularily useful for when quick access to data is critical, allowing engineers to jumo right into data without scanning through the entire structure.
- I feel like an engineer would use a hash table to creating a search engine or any system where quick data retrieval is essential.
'''