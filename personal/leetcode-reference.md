# LeetCode Reference - Key Patterns & Important Problems

## Study Strategy

**14 Patterns to Ace Any Coding Interview:**
1. Sliding Window
2. Two Pointers
3. Fast & Slow Pointers
4. Merge Intervals
5. Cyclic Sort
6. In-place Reversal of Linked List
7. Tree BFS
8. Tree DFS (Recursive)
9. Two Heaps
10. Subsets
11. Modified Binary Search
12. Top K Elements
13. K-way Merge
14. Longest Common Substring

**Time Management During Interviews:**
- Easy: max 10 minutes
- Medium: max 30 minutes
- Hard: max 1 hour

**Depth-First Approach:** Master each data structure before moving on. Use spaced repetition.

---

## Core Data Structures to Master

- Arrays and Lists
- 2D Arrays
- Strings
- Linked Lists (Singly, Doubly, Circular)
- Stacks
- Queues
- Hash Table and Hash Set
- Heap
- Graphs
- Binary Tree
- Binary Search Tree
- Trie

---

## Key Problems by Category

### Arrays & Sorting (HIGH IMPACT)

| Problem | Why Important |
|---------|---------------|
| Kadane's Algo - max subarray sum | Core DP/array pattern |
| Merge Intervals | Interval overlapping problems |
| Next Permutation | Array manipulation |
| Best time to buy and sell stock | Space/time tradeoffs |
| Trapping Rain Water | Two pointers + stack |
| Find duplicates (n+1 integers) | Floyd's cycle detection |
| Maximum product subarray | Dynamic handling of signs |

**Important Techniques:**
- Dutch National Flag (sort 0,1,2 in-place)
- Kadane's Algorithm for contiguous subarrays
- Two-pointer for sorted arrays
- Prefix/suffix arrays for optimization

---

### Strings

| Problem | Pattern |
|---------|---------|
| Longest Palindromic Substring | Expand around center, Manacher's |
| Edit Distance | DP - Levenshtein distance |
| Word Break Problem | Trie + DP |
| Rabin Karp / KMP | String matching |
| Minimum window substring | Sliding window |
| Longest Common Subsequence | DP |

**Key Insight:** Strings often converted to array problems. Hash maps for character frequency.

---

### Linked Lists

| Problem | Key Technique |
|---------|---------------|
| Reverse in groups of K | Dummy node + pointers |
| Detect cycle | Floyd's Tortoise-Hare |
| Merge K sorted lists | Min-heap approach |
| Clone with random pointer | Map original to clone |
| Add two numbers | Stack or reverse first |

**Critical:** Dummy node pattern, fast/slow for middle, reverse with recursion.

---

### Binary Trees

| Problem | Pattern |
|---------|---------|
| All traversals (in/pre/post/level) | Stack and Queue |
| Diameter of tree | DFS - longest path |
| LCA | Recursive search |
| Balanced BST from sorted array | Recursion |
| Serialize/Deserialize | Preorder + null markers |

**Views (HIGH VALUE):** Left view, Right view, Top view, Bottom view, Zigzag traversal.

---

### Binary Search Trees

| Problem | Notes |
|---------|-------|
| Search, Insert, Delete | BST properties |
| Inorder successor/predecessor | Traversal based |
| Largest BST in Binary Tree | Post-order check |
| Merge two BSTs | Stack-based iteration |
| Kth smallest/largest | Counter or reverse inorder |

---

### Stacks & Queues

| Problem | Key Insight |
|---------|-------------|
| Next Greater Element | Monotonic stack |
| LRU Cache | HashMap + Doubly Linked List |
| Celebrity Problem | O(n) elimination |
| Largest Rectangular Area | Monotonic stack |
| Merge Overlapping Intervals | Stack of intervals |
| Implement Stack with getMin() | Auxiliary stack trick |

**Monotonic Stack Pattern:** Maintain decreasing/increasing stack for next greater/smaller problems.

---

### Heap / Priority Queue

| Problem | Technique |
|---------|-----------|
| K largest/smallest elements | Heap of size K |
| Merge K sorted arrays | Min-heap merge |
| Median in a stream | Two heaps (max/min) |
| Smallest range in K lists | Heap + sliding window |
| Reorganize strings | Max-heap + greedy |

---

### Graphs

| Problem | Algorithm |
|---------|-----------|
| Number of Islands | DFS/BFS flood fill |
| Clone graph | BFS with mapping |
| Word Ladder | BFS with transformation |
| Dijkstra | Priority queue |
| Topological Sort | DFS or Kahn's BFS |
| Detect cycle (directed) | DFS colors / BFS indegree |
| Detect cycle (undirected) | DFS with parent tracking |
| Bellman Ford | Edge relaxation |
| Floyd Warshall | All-pairs shortest path |

**Key Patterns:** BFS for shortest paths, DFS for connectivity, Union-Find for cycle detection.

---

### Dynamic Programming (DP)

**Common Types:**
1. **Optimization:** Max/Min (Knapsack, Longest Increasing Subsequence)
2. **Counting:** Number of ways (Coin change, Fibonacci)
3. **可行性:** Yes/No (Word break, Jump game)

**Most Important Problems:**
| Problem | Pattern |
|---------|---------|
| Coin Change | Unbounded knapsack |
| 0/1 Knapsack | Weight/value selection |
| Longest Common Subsequence | 2-string DP |
| Longest Increasing Subsequence | O(n log n) or O(n^2) |
| Edit Distance | Character replacement |
| House Robber | Adjacent selection |
| Climbing Stairs | Simple DP |
| Word Break | Trie + DP |
| Egg Drop | Binary search + DP |

**DP Framework:**
1. Define subproblem
2. Guess (transition)
3. Relate subproblem solutions
4. Build order / memoize

**Key Insight:** If you can phrase it as "maximum/minimum/count of something", it's likely DP.

---

### Backtracking

| Problem | Notes |
|---------|-------|
| N-Queens | Placement validation |
| Sudoku Solver | Constraint checking |
| Subsets | Build-up approach |
| Permutations | Swap-based |
| Combination Sum | Pruning with sorting |
| Rat in Maze | Direction exploration |

**Key Insight:** When DFS depth is unknown or large, consider BFS/iteration instead.

---

### Greedy

| Problem | Strategy |
|---------|----------|
| Activity Selection | Earliest finish first |
| Job Sequencing | Deadline + profit sorting |
| Huffman Coding | Min-heap frequency |
| Fractional Knapsack | Value/weight ratio |
| Minimum Platforms | Greedy timeline |

**Warning:** Greedy only works when local optimal leads to global optimal.

---

### Trie

| Problem | Application |
|---------|-------------|
| Implement Trie | Insert, search, prefix |
| Word Break | Dictionary matching |
| Auto-complete | Prefix matching |
| Longest Common Prefix | Array of strings |

---

### Bit Manipulation

| Technique | Use Case |
|-----------|----------|
| AND, OR, XOR | Toggle/check bits |
| Left/Right Shift | Power of 2 |
| Brian Kernighan's | Count set bits |
| XOR trick | Find unique in pairs |

---

## Recommended Practice Lists

1. **Blind 75 LeetCode** - Most common interview problems
2. **14 Patterns List** - Grokking the Coding Interview
3. **450 Problems DSA** - Complete coverage

---

## System Design (Interview)

**Key Topics:**
- API Design
- Caching (LRU, LFU)
- Load Balancing
- Database sharding
- CAP Theorem
- Microservices patterns
- Message queues
- CDN

**Resources:**
- System Design Primer (GitHub)
- Grokking the System Design Interview

---

## Resources

- Neetcode YouTube
- BackToBackSWE
- Tech Dose
- AlgoExpert
- Cracking the Coding Interview solutions (GitHub)

