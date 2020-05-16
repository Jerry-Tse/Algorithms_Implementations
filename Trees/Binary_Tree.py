class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
        
    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.__search(self.root, find_val)
        
        
    def __search(self, current_node, find_val):
                
        if (current_node.value == find_val):
            return True
        
        left = False
        right = False

        if current_node.left != None:
            left = self.__search(current_node.left, find_val)
        
        if current_node.right != None:
            right = self.__search(current_node.right, find_val)
        
        return left or right

        

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""        
        return self.__print_tree(self.root)
    
    def __print_tree(self, current_node):
        print(current_node.value)
        
        if current_node.left != None:
            self.__print_tree(current_node.left)
        
        if current_node.right != None:
            self.__print_tree(current_node.right)
        

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())
