# Data Structure and Algorithms

## Why
**Data Structures**: particular ways of storing and retrieving data to be used efficiently
**Algorithms**: instructions that computer follows to carry out tasks


### Nodes
**Node**: contains data and links (aka pointers) to other nodes

### Linked Lists:
**Linked Lists**: a linear data structure where elements are not stored at *contiguous* location
- Runner technique: can be used in problem like: "return the **nth** last element in a singly linked list"
1. create two pointers at different positions but they move at the same rate
2. second pointer delay **n** steps behind the first pointer
3. when first pointer reached tail node, return second pointer

### Doubly Linked Lists:
- Bidirectional

## Abstract Data Types
### Queue: an ordered set of data (FIFO)
1. Enqueue
2. Dequeue
3. Peek

*"Queue overflow"*: attempting to enqueue when queue is full

### Stacks: (Last in, First out - LIFO)
1. Push
2. Pop
3. Peek

*"Stack overflow"*: attempting to enqueue when stack is full

## ----

### Hash Map:


## Recursion
- Recursive Functions
    - Base Case: to stop recursion
    - Recursive step; to get closer and closer to the base case
- Similar to iterative loops. Tend to be **less** efficient because of the call stack. Both method have O(n) runtime

New Concepts:
- Call stack
- Execution Context (執行上下文) - values inside the recursive functions
- Powerset
    - All subset of values in a list (eg. [a, b] -> [a, b], [a], [b], [])


## Sorting Algorithms
Bubble Sort
- swapping neighbor/adjacent elements. 1 iteration/comparison each time, move the larger element to the right.
- Optimization:
    1.


Merge Sort
- **Divide-and-conquer**
- **Time: O(n * log(n))**
- **Space: O(n)**
- Split list into left and right recursively. Like a tree branching out.


Quick Sort
- **Divide-and-conquer**

(2/4/2022)
## Trees
Definitions:
1. A graph that does not contain any **cycle**
2. **Cycle**: a path through edges that begins and ends on the same node

### Breath-first
- Level-by-level search
- Implement with **queue** (enqueue all nodes on the same level and dequeue these nodes before accessing the nodes in the next level)
- Good for identifying shortest path

### Depth-first
- Search exhaust until leaf node is reached before move onto sibling nodes
- Implement with **stack** (sibling nodes are added to stack, but children nodes continue to add on top of stack. All child, child, ...., child node need to be searched/ push off the stack before we move onto the siblings nodes on the samve level)
- Can have recursive version - b/c recursion uses an underlying call stack
