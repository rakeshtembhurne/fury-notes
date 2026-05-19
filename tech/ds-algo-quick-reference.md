---
created: 2026-05-19
tags: [topics/personal/tech]
source: notes directory
---

# DS & Algo Quick Reference

_JavaScript-focused data structures and algorithms reference from notes and CTCI/Grokking resources._

## String/Array — Reverse a String (12 Methods)

```javascript
// Method 1: Inverse for loop with string
function forLoopInverse(str) {
  let reverse = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reverse += str[i];
  }
  return reverse;
}

// Method 2: Straight for loop with string
function forLoopStraight(str) {
  let reverse = "";
  for (let i = 0; i < str.length; i++) {
    reverse += str[str.length - 1 - i];
  }
  return reverse;
}

// Method 3: Split and Reduce
function arraySplitAndReduce(str) {
  return str.split("").reduce((x, y) => y.concat(x));
}

// Method 5: Split and Reverse
function arraySplitAndReverse(str) {
  return str.split("").reverse().join("");
}

// Method 7: Swapping Indices with while loop
function reverseBySwappingIndices(str) {
  const strArr = [...str];
  let leftIndex = 0;
  let rightIndex = strArr.length - 1;
  while (leftIndex < rightIndex) {
    let temp = strArr[leftIndex];
    strArr[leftIndex] = strArr[rightIndex];
    strArr[rightIndex] = temp;
    leftIndex++;
    rightIndex--;
  }
  return strArr.join("");
}

// Method 8: Divide and Conquer (swapping with for loop)
function divideAndConquer(str) {
  const strArr = [...str];
  let n = strArr.length - 1;
  for (let i = 0; i <= n / 2; i++) {
    let temp = strArr[i];
    strArr[i] = strArr[n - i];
    strArr[n - i] = temp;
  }
  return strArr.join("");
}
```

---

## CTCI 1.1 — Is Unique

```javascript
// Method: Unique by Set
function hasUniqueCharactersSet(str) {
  let chars = new Set();
  for (let i = 0; i < str.length; ++i) {
    if (chars.has(str[i])) return false;
    chars.add(str[i]);
  }
  return true;
}

// Method: Unique by Bitwise Operation
function isUniqueByBitwiseOp(str, indexOffset = "a".charCodeAt()) {
  let counterTable = Number();
  for (let index of [...str].map((c) => c.charCodeAt() - indexOffset)) {
    const mask = 1 << index;
    if (counterTable & mask) return false;
    counterTable |= mask;
  }
  return true;
}

// Method: Unique by Sorted String
function hasUniqueCharactersSort(str) {
  const strArray = str.split("");
  strArray.sort();
  for (var i = 1; i < strArray.length; ++i) {
    if (strArray[i] === strArray[i - 1]) return false;
  }
  return true;
}
```

---

## CTCI 1.2 — Check Permutation

```javascript
function checkPermuteWithSort(stringOne, stringTwo) {
  if (stringOne.length !== stringTwo.length) return false;
  const sortedStringOne = stringOne.split("").sort().join("");
  const sortedStringTwo = stringTwo.split("").sort().join("");
  return sortedStringOne === sortedStringTwo;
}

function checkPermuteWithMap(str1, str2) {
  if (str1.length === 0 || str1.length !== str2.length) return false;
  let chars = new Map();
  for (let i = 0; i < str1.length; ++i)
    chars.set(str1[i], chars.get(str1[i]) + 1 || 1);
  for (let i = 0; i < str2.length; ++i) {
    let count = chars.get(str2[i]);
    if (!count) return false;
    if (count === 1) chars.delete(str2[i]);
    else chars.set(str2[i], count - 1);
  }
  return chars.size === 0;
}
```

---

## Array Algorithms

### Maximum Sum Subarray (Kadane's Algorithm) — O(n)
```javascript
let findMaxSumSubArray = function(array_) {
  if (array_.length < 1) return 0;
  let currMax = array_[0];
  let globalMax = array_[0];
  for (let i = 1; i < array_.length; i++) {
    if (currMax < 0) currMax = array_[i];
    else currMax += array_[i];
    if (globalMax < currMax) globalMax = currMax;
  }
  return globalMax;
};
```

### Find Two Numbers that Add up to Value
```javascript
// Solution 3: Moving indices — O(n log n) after sort
function findSum(arr, value) {
  arr.sort((a, b) => a - b);
  var index1 = 0, index2 = arr.length - 1, result = [], sum = 0;
  while (index1 != index2) {
    sum = arr[index1] + arr[index2];
    if (sum < value) index1++;
    else if (sum > value) index2--;
    else {
      result.push(arr[index1]);
      result.push(arr[index2]);
      return result;
    }
  }
  return false;
}
```

### Array of Products of All Elements — O(n)
```javascript
function findProduct(arr) {
  var temp = 1, product = [];
  for (var i = 0; i < arr.length; i++) {
    product[i] = temp;
    temp = temp * arr[i];
  }
  temp = 1;
  for (var i = arr.length - 1; i > -1; i--) {
    product[i] *= temp;
    temp *= arr[i];
  }
  return product;
}
```

### Right Rotate Array by n — O(n)
```javascript
function rightRotate(arr, n) {
  return (arr.splice(arr.length - n)).concat(arr.splice(0, arr.length));
}
```

### Rearrange Positive & Negative Values — O(n)
```javascript
function reArrange(arr) {
  var leftMostPosEle = 0, tmp;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      if (i != leftMostPosEle) {
        tmp = arr[i]; arr[i] = arr[leftMostPosEle]; arr[leftMostPosEle] = tmp;
      }
      leftMostPosEle += 1;
    }
  }
  return arr;
}
```

### Max Min Arrangement — O(n)
```javascript
function maxMin(arr) {
  var result = [];
  for (var i = 0; i < Math.floor(arr.length / 2); i++) {
    result.push(arr[arr.length - (i + 1)]);
    result.push(arr[i]);
  }
  if (arr.length % 2) result.push(arr[Math.floor(arr.length / 2)]);
  return result;
}
```

### Find Second Maximum — O(n)
```javascript
function findSecondMaximum(arr) {
  var max = Number.NEGATIVE_INFINITY;
  var secondmax = Number.NEGATIVE_INFINITY;
  for (var val of arr) {
    if (val > max) { secondmax = max; max = val; }
    else if (val > secondmax && val != max) secondmax = val;
  }
  return secondmax;
}
```

### Find First Unique Integer
```javascript
function findFirstUnique(arr) {
  const counts = {};
  for (let number of arr) counts[number] = (counts[number] || 0) + 1;
  for (let number of arr) if (counts[number] === 1) return number;
  return;
}
```

### Merge Two Sorted Arrays — O(n+m)
```javascript
function mergeArrays(arr1, arr2) {
  var merged = [], i = 0, j = 0;
  while ((i < arr1.length) && (j < arr2.length)) {
    if (arr1[i] < arr2[j]) merged.push(arr1[i++]);
    else merged.push(arr2[j++]);
  }
  if (i <= arr1.length - 1) merged = merged.concat(arr1.splice(0, i));
  else if (j <= arr2.length - 1) merged = merged.concat(arr2.splice(0, j));
  return merged;
}
```

---

## LinkedList Implementation

```javascript
class LinkedListNode {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  prepend(value) {
    const newNode = new LinkedListNode(value, this.head);
    this.head = newNode;
    if (!this.tail) this.tail = newNode;
    return this;
  }

  append(value) {
    const newNode = new LinkedListNode(value);
    if (!this.head) { this.head = newNode; this.tail = newNode; return this; }
    this.tail.next = newNode;
    this.tail = newNode;
    return this;
  }

  delete(value) {
    while (this.head && this.head.value === value) this.head = this.head.next;
    let current = this.head;
    while (current && current.next) {
      if (current.next.value === value) current.next = current.next.next;
      else current = current.next;
    }
    if (this.tail.value === value) this.tail = current;
  }

  reverse() {
    let curr = this.head, prev = null, next = null;
    while (curr) {
      next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }
    this.tail = this.head;
    this.head = prev;
    return this;
  }

  toArray() {
    const nodes = [];
    let current = this.head;
    while (current) { nodes.push(current); current = current.next; }
    return nodes;
  }
}
```

---

## Java Collections — Quick Reference

**Collections Framework:**
- Interfaces: `Collection`, `List`, `Set`, `Queue`, `Map`
- ArrayList: Dynamic array — `List<String> list = new ArrayList<>();`
- LinkedList: Doubly linked — good for insertions/deletions
- HashSet: Unordered, no duplicates — `Set<Integer> set = new HashSet<>();`
- HashMap: Key-value pairs — `Map<String, Integer> map = new HashMap<>();`

**Concurrency:**
```java
// Thread pool
ExecutorService executor = Executors.newFixedThreadPool(2);

// Atomic counter
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();

// Reentrant lock
Lock lock = new ReentrantLock();
lock.lock();
try { /* critical section */ }
finally { lock.unlock(); }
```

**Stream API:**
```java
int sum = numbers.stream()
  .filter(n -> n % 2 == 0)
  .mapToInt(Integer::intValue)
  .sum();
```

**Lambda Expressions:**
```java
list.forEach(s -> System.out.println(s));
// java.util.function: Predicate<T>, Consumer<T>, Function<T, R>
```

---

## Data Structures & Algorithm Topics (Study Guide)

### Basic DSA
1. Array 2. String 3. Matrix 4. Maths 5. Stack 6. Queue 7. Recursion
8. Searching and Sorting 9. Linked List 10. Binary Trees and BST
11. Asymptotic analysis (Big-O Notation)

### Advanced Topics
- **Hashing** — Collision handling, hash functions
- **Tries** — Prefix trees, search/insert/delete
- **Heap** — Min/Max heap, priority queue
- **Graph** — BFS, DFS, Dijkstra, Prim, Kruskal
- **Greedy** — Activity selection, fractional knapsack, Huffman coding
- **Backtracking** — N-queen, rat in maze, Sudoku
- **Dynamic Programming** — Memoization, tabulation, LCS, coin change, LIS, egg dropping
- **Segment Trees & BIT** — Range queries, point updates
- **Disjoint Set** — Union by rank, path compression

### Weekly Study Plan
| Week | Topics |
|------|--------|
| Week 1 | Analysis of Algorithms, Mathematics, Bit Magic |
| Week 2 | Recursion, Arrays, Searching |
| Week 3 | Sorting, Matrix, Hashing |
| Week 4 | Strings, Linked List |
| Week 5 | Stack, Queue, Deque, Tree |
| Week 6 | BST, Heap, Graph |
| Week 7 | Greedy, Backtracking, Dynamic Programming |
| Week 8 | Trie, Segment/BIT, Disjoint Set |

### Resources
- [leetcode-js](https://github.com/everthis/leetcode-js)
- [javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)
- [Formation](https://formation.dev) — Finds lacuna in DSA knowledge

### Abbreviations
- LCUS = Leetcode US, LCCN = Leetcode China
- AC = Accepted, WA = Wrong Answer, OJ = Online Judge
- TC = Total Compensation, TLE = Time Limit Exceeded, MLE = Memory Limit Exceeded
