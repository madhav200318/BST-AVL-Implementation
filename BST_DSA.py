
import random
import time
import math
import csv
import matplotlib.pyplot as plt


# ---------------- PLAIN BST ----------------

class Node:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, name):
        new = Node(key, name)
        if not self.root:
            self.root = new
            return
        current = self.root
        while True:
            if key < current.key:
                if not current.left:
                    current.left = new
                    return
                current = current.left
            elif key > current.key:
                if not current.right:
                    current.right = new
                    return
                current = current.right
            else:
                current.name = name
                return

    def search(self, key):
        current = self.root
        count = 0
        while current:
            count += 1
            if key == current.key:
                return current.name, count
            current = current.left if key < current.key else current.right
        return None, count

    def delete(self, key):
        parent = None
        current = self.root

        while current and current.key != key:
            parent = current
            current = current.left if key < current.key else current.right

        if not current:
            return

        if not current.left or not current.right:
            child = current.left or current.right
            if not parent:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child
        else:
            p = current
            s = current.right
            while s.left:
                p, s = s, s.left
            current.key, current.name = s.key, s.name
            if p.left == s:
                p.left = s.right
            else:
                p.right = s.right

    def height(self):
        if not self.root:
            return 0
        stack = [(self.root, 1)]
        result = 0
        while stack:
            node, level = stack.pop()
            result = max(result, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return result

    def inorder(self):
        result, stack = [], []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.key)
            current = current.right
        return result

    def is_bst(self):
        a = self.inorder()
        return all(a[i] < a[i+1] for i in range(len(a)-1))


# ---------------- AVL TREE ----------------

class AVLNode:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.left = self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None
        self.rotations = 0

    def h(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.h(node.left) - self.h(node.right)

    def right_rotate(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        y.height = 1 + max(self.h(y.left), self.h(y.right))
        x.height = 1 + max(self.h(x.left), self.h(x.right))
        self.rotations += 1
        return x

    def left_rotate(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        x.height = 1 + max(self.h(x.left), self.h(x.right))
        y.height = 1 + max(self.h(y.left), self.h(y.right))
        self.rotations += 1
        return y

    def rebalance(self, node):
        node.height = 1 + max(self.h(node.left), self.h(node.right))
        b = self.balance(node)

        if b > 1 and self.balance(node.left) >= 0:
            return self.right_rotate(node)       # LL

        if b < -1 and self.balance(node.right) <= 0:
            return self.left_rotate(node)        # RR

        if b > 1 and self.balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)      # LR

        if b < -1 and self.balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)       # RL

        return node

    def _insert(self, node, key, name):
        if not node:
            return AVLNode(key, name)

        if key < node.key:
            node.left = self._insert(node.left, key, name)
        elif key > node.key:
            node.right = self._insert(node.right, key, name)
        else:
            node.name = name
            return node

        return self.rebalance(node)

    def insert(self, key, name):
        self.root = self._insert(self.root, key, name)

    def search(self, key):
        current = self.root
        count = 0
        while current:
            count += 1
            if key == current.key:
                return current.name, count
            current = current.left if key < current.key else current.right
        return None, count

    def minimum(self, node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            s = self.minimum(node.right)
            node.key, node.name = s.key, s.name
            node.right = self._delete(node.right, s.key)

        return self.rebalance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def height(self):
        return self.h(self.root)

    def inorder(self):
        result, stack = [], []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.key)
            current = current.right
        return result

    def is_bst(self):
        a = self.inorder()
        return all(a[i] < a[i+1] for i in range(len(a)-1))

    def is_balanced(self):
        def check(node):
            if not node:
                return True, 0
            left_ok, lh = check(node.left)
            right_ok, rh = check(node.right)
            return (left_ok and right_ok and abs(lh-rh) <= 1,
                    1 + max(lh, rh))
        return check(self.root)[0]


# ---------------- SAMPLE DEMONSTRATION ----------------

print("SAMPLE INPUT: 10, 20, 30, 40, 50, 25")

b = BST()
a = AVL()

for key in [10, 20, 30, 40, 50, 25]:
    b.insert(key, "Patient_" + str(key))
    a.insert(key, "Patient_" + str(key))

print("BST root:", b.root.key, "Height:", b.height())
print("AVL root:", a.root.key, "Height:", a.height())
print("AVL rotations:", a.rotations)
print("BST inorder:", b.inorder())
print("AVL inorder:", a.inorder())


# ---------------- DELETION TESTS ----------------

print("\nDELETION TESTS")

for Tree in [BST, AVL]:
    tree = Tree()
    for key in [20, 10, 30, 5, 15, 25, 35, 27]:
        tree.insert(key, str(key))

    tree.delete(5)       # Leaf
    print(Tree.__name__, "After leaf deletion:", tree.inorder())

    tree.delete(25)      # One child
    print(Tree.__name__, "After one-child deletion:", tree.inorder())

    tree.delete(30)      # Two children
    print(Tree.__name__, "After two-child deletion:", tree.inorder())

    assert tree.is_bst()
    if isinstance(tree, AVL):
        assert tree.is_balanced()


# ---------------- WORKLOAD GENERATION ----------------

def workload(n, kind, rng):
    data = list(range(1, n + 1))

    if kind == "Random":
        rng.shuffle(data)

    elif kind == "Nearly sorted":
        for i in range(max(1, int(n * 0.05))):
            x, y = rng.randrange(n), rng.randrange(n)
            data[x], data[y] = data[y], data[x]

    return data


# ---------------- EXPERIMENTS ----------------

rng = random.Random(42)
sizes = [1000, 5000, 10000]
datasets = ["Sequential", "Random", "Nearly sorted"]

rows = []
graph_data = []

for n in sizes:
    for kind in datasets:

        data = workload(n, kind, rng)
        searches = rng.sample(range(1, n+1), 1000)
        deletions = rng.sample(range(1, n+1), n//5)

        # Plain BST
        bst = BST()
        start = time.perf_counter()

        for key in data:
            bst.insert(key, "Patient_" + str(key))

        bst_time = time.perf_counter() - start
        bst_height = bst.height()
        bst_avg = sum(bst.search(k)[1] for k in searches) / 1000

        for key in deletions:
            bst.delete(key)

        bst_delete_height = bst.height()

        # AVL Tree
        avl = AVL()
        start = time.perf_counter()

        for key in data:
            avl.insert(key, "Patient_" + str(key))

        avl_time = time.perf_counter() - start
        avl_height = avl.height()
        avl_avg = sum(avl.search(k)[1] for k in searches) / 1000

        for key in deletions:
            avl.delete(key)

        avl_delete_height = avl.height()

        assert bst.is_bst()
        assert avl.is_bst() and avl.is_balanced()

        minimum = math.floor(math.log2(n))

        rows.append([n, kind, "BST", bst_height, minimum,
                     round(bst_time, 6), 0, round(bst_avg, 2),
                     bst_delete_height])

        rows.append([n, kind, "AVL", avl_height, minimum,
                     round(avl_time, 6), avl.rotations,
                     round(avl_avg, 2), avl_delete_height])

        if kind == "Sequential":
            graph_data.append((n, bst_height, avl_height))

        print("\nN:", n, "| Dataset:", kind)

        print("BST Height:", bst_height,
              "| Time:", round(bst_time, 6),
              "| Comparisons:", round(bst_avg, 2),
              "| After deletion:", bst_delete_height)

        print("AVL Height:", avl_height,
              "| Time:", round(avl_time, 6),
              "| Comparisons:", round(avl_avg, 2),
              "| Rotations:", avl.rotations,
              "| After deletion:", avl_delete_height)


# ---------------- CSV OUTPUT ----------------

headers = ["N", "Dataset", "Tree", "Final Height",
           "Minimum Height", "Insertion Time",
           "Rotations", "Average Comparisons",
           "Height After Deletion"]

with open("comparison_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("\nCSV file generated: comparison_results.csv")


# ---------------- GRAPH ----------------

x = [v[0] for v in graph_data]
bst_y = [v[1] for v in graph_data]
avl_y = [v[2] for v in graph_data]

plt.plot(x, bst_y, marker="o", label="Plain BST")
plt.plot(x, avl_y, marker="o", label="AVL Tree")

plt.xlabel("Number of Patient IDs")
plt.ylabel("Tree Height")
plt.title("BST vs AVL - Sequential Dataset")
plt.legend()
plt.grid()
plt.savefig("sequential_height_comparison.png")
plt.show()



