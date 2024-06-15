# Querying a BST

Suppose the definition of a node is 
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

```

### Searching for a value

The property of BST makes this operation straightforward. Start from a specific node (usually the root of a BST), and navigate down the tree based on the relationship between the value encountered and the target value.

![alt text](images\search_value_eg.png)


```python
def searchValue(current_node, target):
    
    while current_node.value != target and current_node is not None
        if current_node.value < target:
            current_node = current_node.right
        else:
            current_node = current_node.left
    
    return current_node
```

### Getting max/min value

The max/min values are at the rightmost/leftmost node in the BST.

```python
def getMin(current_node):
    
    while current_node.left is not None
        current_node = current_node.left
    
    return current_node

def getMax(current_node):
    
    while current_node.right is not None
        current_node = current_node.right
    
    return current_node
```