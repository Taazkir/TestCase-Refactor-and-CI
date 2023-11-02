from src.assignment_lists_solutions import Node, DoublyLinkedList

# **Task 1 (5 points)**: Using the constructor from the **DoublyLinkedList**, create a new doubly linked list of random integers between 1 and 10.

# In[3]:
dL = DoublyLinkedList()

for i in range(4):
    dL.add_last(Node(i))

def testingConstructor():
    assert str(dL) == f"(0, (1, (2, (3, ('Trailer', None)))))"

# ## Using a Doubly Linked List
# 
# The given **DoublyLinkedList** Python class
# contains helpful methods for using a doubly linked list.
# Answer the following questions while implementing
# the methods of the **DoublyLinkedList** class.
# 
# **Task 2 (10 points)**: Implement the `size` method that returns the size of a doubly linked list.
# 
# ```python
# def size(self):
#   """Returns the number of elements in the list."""
#   pass 
# ```

# In[4]:


#Test your implementation here
def testSize():
    assert dL.size() == 4


# **Task 3 (5 points)**: Implement the `is_empty` method that checks
# whether a doubly linked list is empty.
# 
# ```python
# def is_empty(self):
#   """Returns the number of elements in the list"""
#   pass
# ```

# In[5]:


#Test your implementation here
def test_isEmpty():
    print(dL.is_empty())

    dL2 = DoublyLinkedList()


    assert dL.is_empty() == False
    assert dL2.is_empty() == True
    del dL2


# **T4 (10 points)**: Implement the methods `get_first` and `get_last`
# to get the first and the last element of the list, respectively.
# 
# _Hint_: Return an exception in case the list is empty.
# 
# ```python
# def get_first(self):
#   """Get the first element of the list"""
#   pass
# 
# def get_last(self):
#   """Get the last element of the list"""
#   pass
# ```

# In[6]:


#Test your implementation here
def test_getFirst():
    assert str(dL.get_first()) == f"(0, (1, (2, (3, ('Trailer', None)))))"

def test_getLast():
    assert str(dL.get_last()) == f"(3, ('Trailer', None))"


# **Task 5 (10 points)**: Implement the methods `get_previous` and `get_next`
# to get the previous and the next node of the list, respectively.
# 
# _Hint_: Return an exception in case the list is empty.
# 
# ```python
# def get_previous(self, node):
#   """Returns the node before the given node"""
#   pass      
# 
# def get_next(self, node):
#   """Returns the node after the given node"""
#   pass
# ```

# In[7]:


#Test your implementation here
def get_previous(): 
    assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"

def get_next():
    assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"


# **Task 6(10 points)**: Implement the methods `add_before` and `add_after`
# to respectively insert new elements before and after a node of the list.
# 
# ```python
# def add_before(self, new, existing):
#   """Insert the new before existing"""
#   pass
# 
# def add_after(self, new, existing):
#   """Insert the new after existing"""
#   pass
# ```

# In[8]:


#Test your implementation here

#Test your implementation here
def add_before():
    dL.add_after(Node(42),dL.get_first())
    assert str(dL) == "(0, (42, (1, (2, (3, ('Trailer', None)))))))"

def add_after():
    dL.add_before(Node(34),dL.get_last())
    assert str(dL) == "(0, (1, (2, (34, (3, ('Trailer', None)))))))"




# **Task 7 (10 points)**: Implement the methods `add_first` and `add_last`
# to respectively insert new nodes in the beginning and in the end of a list.
# 
# ```python
# def add_first(self, new):
#   """Insert the node at the head of the list"""
#   pass
# 
# def add_last(self, new):
#   """Insert the node at the tail of the list"""
#   pass
# ```

# In[17]:


#Test your implementation here
def add_first():
    dL.add_first(Node(7))
    assert str(dL) == "(0, (42, (1, (2, (34, (3, (-1, ('Trailer', None)))))))))"

def add_last():
    dL.add_last(Node(-1))
    assert str(dL) == "(7, (0, (42, (1, (2, (34, (3, ('Trailer', None)))))))))"


# **Task 8 (10 points)**: Implement the method `remove` to remove
# a node from a list.
# 
# ```python
# def remove(self, node):
#   """Removes the given node from the list"""
#   pass
# ```

# In[16]:


#Test your implementation here
def remove():
    dL.remove(dL.get_first())
    assert dL.get_first().get_element() == 0


# **Task 9 (10 points)**: Implement the method `map` to apply a function on
# each element of a list.
# 
# ```python
# def map(self, function):
#   """Run function on every element in the list"""
#   pass
# ```

# In[15]:


#Test your implementation here
def map():
    dL.map(lambda x: x**2)
    assert str(dL) == "(0, (1764, (1, (4, (1156, (9, (1, ('Trailer', None))))))))"


# **Task 10 (10 points)**: Implement the method `next` to iterate the elements
# of a list.
# 
# ```python
# """Standard methods for Python iterator"""
# def __iter__(self):
#   pass
# 
# def __next__(self):
#   pass
# ```

# In[13]:


#Test your implementation here


# def test_next(): 
#     assert str(node.get_element() == dL.__next__().get_element())
    



# 
# ## Applying methods of the DoublyLinkedList and Node classes
# 
# Answer the following questions by using
# the implemented methods from the Node and DoublyLinkedList classes.
# Apply your operations on the list you created in T1.

# **Task 11 (5 points)**: Add 2 to each element of the list.
# 
# _Hint_: Use the methods `map`.

 


def twenties():
    LL = DoublyLinkedList()
    for t in range(20,30):
        LL.add_last(Node(t))
    
    LL.map(lambda x: x+10)

    assert str(LL) =="(30, (31, (32, (33, (34, (35, (36, (37, (38, (39, ('Trailer', None)))))))))))"

