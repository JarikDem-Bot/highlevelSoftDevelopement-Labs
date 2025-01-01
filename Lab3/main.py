class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)
    
    def left_rotate(self, node):
        newRoot = node.right_child
        node.right_child = newRoot.left_child
        newRoot.left_child = node

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        newRoot.height = 1 + max(self.get_height(newRoot.left_child), self.get_height(newRoot.right_child))

        return newRoot
    
    def right_rotate(self, node):
        newRoot = node.left_child
        node.left_child = newRoot.right_child
        newRoot.right_child = node

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        newRoot.height = 1 + max(self.get_height(newRoot.left_child), self.get_height(newRoot.right_child))

        return newRoot
    
    def insert(self, root, value):
        if not root:
            return Node(value)
        
        if value < root.value:
            root.left_child = self.insert(root.left_child, value)
        else:
            root.right_child = self.insert(root.right_child, value)

        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))
        balance = self.get_balance(root)

        if balance > 1 and value < root.left_child.value:
            return self.right_rotate(root)
        
        if balance < -1 and value > root.right_child.value:
            return self.left_rotate(root)
        
        if balance > 1 and value > root.left_child.value:
            root.left_child = self.left_rotate(root.left_child)
            return self.right_rotate(root)
        
        if balance < -1 and value < root.right_child.value:
            root.right_child = self.right_rotate(root.right_child)
            return self.left_rotate(root)
        
        return root
    
    def insert_value(self, value):
        self.root = self.insert(self.root, value)
    

if __name__ == "__main__":

    def print_tree(node):
        if not node:
            return
        print_tree(node.left_child)
        print(node.value)
        print_tree(node.right_child)

    tree = AVLTree()
    tree.insert_value(10)
    tree.insert_value(20)
    tree.insert_value(30)
    tree.insert_value(40)
    tree.insert_value(50)
    tree.insert_value(25)

    print("Tree:")
    print(f"Root: {tree.root.value}")
    print_tree(tree.root)


    tree.insert_value(5)
    tree.insert_value(2)   
    tree.insert_value(3)
    tree.insert_value(4)
    tree.insert_value(15)

    print("\nUpdated tree:")
    print(f"Root: {tree.root.value}")
    print_tree(tree.root)

