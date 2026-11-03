# BST-AVL-Implementation
DSA Implementation
# BST vs AVL Tree – Performance Analysis

## 📌 Project Overview

This project implements and compares two Binary Search Tree data structures:

- **Binary Search Tree (BST)**
- **AVL Tree (Self-Balancing Binary Search Tree)**

The project analyzes their performance based on different input datasets and sizes. It compares tree height, insertion time, average search comparisons, and the number of rotations performed by the AVL Tree.

The implementation uses patient IDs as keys and patient names as associated values.

## 🚀 Features

- Implementation of a standard Binary Search Tree.
- Implementation of a self-balancing AVL Tree.
- Insertion, searching, and deletion operations.
- Inorder traversal of both trees.
- Height calculation and BST validation.
- AVL balance verification.
- Handling of all four AVL rotation cases:
  - LL (Left-Left)
  - RR (Right-Right)
  - LR (Left-Right)
  - RL (Right-Left)
- Testing deletion of leaf nodes, nodes with one child, and nodes with two children.
- Performance comparison using different datasets.
- Automatic generation of CSV results.
- Graphical comparison of BST and AVL Tree heights.

## 🛠️ Technologies Used

- Python
- Random module
- Time module
- Math module
- CSV module
- Matplotlib

## 📂 Dataset and Experiments

The project uses three types of datasets:

1. **Sequential:** Numbers inserted in ascending order.
2. **Random:** Numbers inserted in random order.
3. **Nearly Sorted:** Mostly sorted numbers with a few randomly swapped elements.

The experiments are performed using three input sizes:

- 1,000 elements
- 5,000 elements
- 10,000 elements

A fixed random seed (`42`) is used to maintain reproducibility.

## 📊 Performance Metrics

The following metrics are measured:

| Metric | Description |
|---|---|
| Tree Height | Measures the height of the tree. |
| Insertion Time | Time taken to insert all elements. |
| Average Comparisons | Average number of comparisons during searching. |
| Rotations | Number of rotations performed by the AVL Tree. |
| Height After Deletion | Tree height after deletion operations. |

## 📈 Output Files

After executing the program, the following files are generated:

**1. `comparison_results.csv`**

Contains the performance results of BST and AVL Tree for all datasets and input sizes.

**2. `sequential_height_comparison.png`**

A graph comparing the heights of BST and AVL Tree for sequential datasets.

## ⚙️ Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### Step 2: Navigate to the Project Folder

```bash
cd your-repository-name
```

### Step 3: Install Required Library

```bash
pip install matplotlib
```

### Step 4: Run the Python Program

```bash
python BST_DSA.py
```

The program will execute the experiments, display the results in the terminal, generate a CSV file, and create a comparison graph.

## 🎯 Objective

The main objective of this project is to understand how self-balancing AVL Trees improve search performance compared to ordinary Binary Search Trees, especially when the input data is sorted or nearly sorted.

## 👨‍💻 Author

**Madhav Nair**

