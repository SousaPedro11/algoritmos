class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
"""


def height(root):
    if root is None:
        return 0
    queue_nodes = [root]

    tree_height = 0

    while True:
        node_number = len(queue_nodes)
        if node_number == 0:
            return tree_height

        tree_height += 1

        while node_number > 0:
            node = queue_nodes[0]
            queue_nodes.pop(0)

            if node.left is not None:
                queue_nodes.append(node.left)
            if node.right is not None:
                queue_nodes.append(node.right)

            node_number -= 1


tree = BinarySearchTree()
t = int(input())
# t = 7

arr = list(map(int, input().split()))
# arr = [3, 5, 2, 1, 4, 5, 7]

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
