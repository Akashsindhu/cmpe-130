
import time
import random
import matplotlib.pyplot as plt


class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):
        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx+1
        return False

    def bst(self, val, left, right):

        if right >= 1:
            mid = left + (right - left)/2
            if self.array[mid] == val:
                return mid
            elif self.array[mid] > val:
                return self.bst(val, left, mid-1)
            elif self.array[mid] < val:
                return self.bst(val, mid + 1, right)
            else:
                return -1

    def bsearch(self, val):
        self.bst(val, 0, len(self.array))
        return self.array

class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)#create a node

    def insert(self, val):
        if (self.root is None):
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        node = BST_Node(val)
        if current is None:
            current.val = val
        else:
            if current.val < val:
                if current.right is None:
                    current.right = node
                else:
                    self.insertNode(current.right, val)
            else:
                if current.left is None:
                    current.left = node
                else:
                    self.insertNode(current.left, val)

    def bst_search_value(self, curr, val):
        if curr is None:
            return False
        if curr.val == val:
            return True
        if curr.val < val:
            return self.bst_search_value(curr.right, val)

        return self.bst_search_value(curr.left, val)

    def bsearch(self, val): # check whether the val is in the node
        #find whether the val is in the tree
        return self.bst_search_value(self.root, val)


    def searchNode(self, current, val): #search the node contain tha node of that value, and return the node
        if current is None:
            return False
        if current.val == val:
            return current
        if current.val < val:
            return self.searchNode(current.right, val)
        return self.searchNode(current.left, val)

    def minValue(self,node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def delMin(self, node):
        if node.left is None:
            return node.right
        node.left = self.delMin(node.left)
        return node

    def delNode(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self.delNode(node.left, key)
        elif key > node.val:
            node.right = self.delNode(node.right, key)
        else:
            if node.right is None:
                temp = node.left
                return temp
            elif node.left is None:
                temp = node.right
                return temp
            t = node
            node = self.minValue(t.right)
            node.right = self.delMin(node.right)
            node.left = t.left
        return node

    def delete(self, val):
        self.root = self.delNode(self.root, val)


class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color
        self.parent = None


RED = True
BLACK = False

class RBBST:
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):
        if current is None:
            return False
        return current.color == RED

    def rotate_left(self, current):
        x = current.right
        current.right = x.left
        x.left = current
        x.color = current.color
        current.color = RED
        return x


    def rotate_right(self, current):
        x = current.left
        current.left = x.right
        x.right = current
        x.color = current.color
        current.color = RED
        return x

    def flip_colors(self, current):
        current.color = RED
        current.left.color = BLACK
        current.right.color = BLACK


    def insert(self, val):
        if self.root is None:
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)
        return self.root

    def insertNode(self, current, val):
        if current is None:
            current = RBBST_Node(val, RED)
        if val < current.val:
            current.left = self.insertNode(current.left, val)
            current.left.parent = current
        elif val > current.val:
            current.right = self.insertNode(current.right, val)
            current.right.parent = current
        else:
            current.val = val
        if self.is_red(current.right) and not self.is_red(current.left):
            current = self.rotate_left(current)
        if self.is_red(current.left) and self.is_red(current.left.left):
            current = self.rotate_right(current)
        if self.is_red(current.left) and self.is_red(current.right):
            self.flip_colors(current)
        return current


    def bsearch(self, val):
        if self.searchNode(self.root, val) is not None:
            return self.searchNode(self.root, val)
        return False

    def searchNode(self, current, val):
        while current is not None and current.val != val:
            if val < current.val:
                current = current.left
            else:
                current = current.right
        return current


if __name__ == "__main__":
    print("Testing Start!!!")
    set_szs = [10, 100, 1000, 10000, 10000]
    timing = []

    tut = BST()

    print("BST: ")
    for ind in set_szs:
        print("set_szs1", ind)
        vals = random.sample(range(1, ind*10), ind)
        t0 = time.time()
        for idx in range(ind):

            tut.insert(vals[idx])

        print("tut.bsearch(vals[1]): ", tut.bsearch(vals[1]))
        print("tut.bsearch(11):", tut.bsearch(11))
        t1 = time.time()
        total_time = t1 - t0
        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, label='BST_bsearch')

    timing1 = []
    tut_rb = RBBST()
    print("RBBST: ")
    for ind in set_szs:
        print("set_szs2", ind)
        vals = random.sample(range(1, ind * 10), ind)
        t0 = time.time()
        for idx in range(ind):
            tut_rb.insert((vals[idx]))

        print("tut_rb.bsearch(vals[1]): ", tut_rb.bsearch(vals[1]))
        print("tut_rb.bsearch(11):", tut_rb.bsearch(11))
        t1 = time.time()
        total_time = t1 - t0
        timing1.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing1, label='RBBST_bsearch')

    plt.xscale('log')
    plt.yscale('log')
    plt.title('Sorting')
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.legend()
    plt.show()
