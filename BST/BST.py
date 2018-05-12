class BST(object):
    """
    Simply binary search tree implementation.
    This BST supports insert,find,and delete-min operations.
    Each tree contains some (possibly 0) BSTnode objects,representing nodes,
    and a pointer to the root.
    """
    def __init__(self):
        self.root=None

    def insert(self,t):
        new = BSTnode(t)
        #二叉树为空，则新插入的节点为根节点
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:
                    #往左边
                    if node.left==None:
                        node.left=new
                        new.parent=node
                        break
                    node = node.left
                else:
                    #往右
                    if node.right == None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return  new

    def find(self,t):
        node = self.root
        while node is not None:
            if t == node.key:
                return  node
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return  node

    def delete_min(self):
        """Delete the minimum key (and return the old node containing it)."""
        node = self.root
        if node is None:
            return  None,None
        else:
            while node.left is not None:
                node = node.left
            # Remove that node and promote its right subtree
            if node.parent is not None:
                node.parent.left = node.right
            else:# The root was smallest.
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return  node,parent


    def tree_maximun(self,node):
        #return the maximun node in the given subtree
        while node.right is not None:
            node = node.right
        return  node

    def tree_minimun(self,node):
        #return the maximun node in the given subtree
        while node.left is not None:
            node=node.left
        return  node

    def tree_successor(self,node):
        #return the successor at the given node
        if node.right is not None:
            return self.tree_minimun(node.right)
        else:
            y = node.parent
            while y is not None and y.right == node:
                node = y
                y = y.parent
            return  y

    def transplant(self,u,v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent=u.parent

    def delete(self,node):
        if node.left == None:
            self.transplant(node,node.right)
        elif node.right == None:
            self.transplant(node,node.left)
        else:
            y = self.tree_minimun(node.right)
            if y.parent != node:
                self.transplant(y,y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node,y)
            y.left=node.left
            y.left.parent = y



    def __str__(self):
        if self.root is None: return '<empty tree>'

        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
                    node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        return '\n'.join(recurse(self.root)[0])


class BSTnode(object):
    """
    Representation of a node in a binary search tree.
    Has a left child, right child, and key value.
    """
    def __init__(self,t):
        self.key = t
        self.disconnect()
        
    def disconnect(self):
        self.left=None
        self.right=None
        self.parent=None


def test(args=None, BSTtype=BST):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print ('usage: %s <number-of-random-items | item item item ...>' % \
              sys.argv[0])
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in xrange(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print (tree)
    for item in items:
        tree.insert(item)
        print()
        print(tree)

#if __name__ == '__main__': test()
t=BST()
print(t)
for i in range(22):
    t.insert(i)
print(t)
node_5 = t.find(5)
node_5_successor = t.tree_successor(node_5)
print(node_5_successor.key)
t.delete(node_5_successor)
print(t)