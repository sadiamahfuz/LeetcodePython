# Problem 102
# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_level_order(root):
    # This is BFS
    queue = []
    if not root:
        return
    
    queue.append(root)
    levelLength = 1

    while len(queue) > 0:
        while levelLength > 0:
            current = queue.pop(0)
            levelLength -= 1
            print(current.value, end='\t')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        levelLength = len(queue)
        print()


if __name__ == "__main__":
    root = Node(5)
    left1 = Node(3)
    right1 = Node(7)
    left2 = Node(1)
    right2 = Node(4)
    left3 = Node(6)
    right3 = Node(9)

    root.left = left1
    root.right = right1
    left1.left = left2
    left1.right = right2
    right1.left = left3
    right1.right = right3

    print_level_order(root)



