# Lecture 2 Homework

## 4.5

### Question

写一个有效算法来测试一个给定的数组是否是一个堆（Heap）。该算法的时间复杂度是多少？

### Answer

这个简单——类似于树的结构，用递归特别好写。

参见 `./02-sorting.assets/heap_check.py`。

```python
class Node:
    value: int
    left: Node
    right: Node

# assume it's a minimized heap


def heap_check(node: Node) -> bool:
    if node == None:
        return True

    if node.left != None and node.left.value > node.value:
        return False

    if node.right != None and node.right.value > node.value:
        return False

    return heap_check(node.left) and heap_check(node.right)
```

总归，就是这样。

时间复杂度的话，在最坏情况下（也就是他是个 Heap 的情况下），对于 $n$ 个元素的堆，`heap_check` 函数会被调用 $n$ 次。

而每次调用的执行时间都是 $O(1)$ 的，因此总的时间复杂度当然就是 $O(n)$ 啦。

## 4.15

### Question

给出一个整数数组 $A$（$\lbrack 1 \dots n\rbrack$），可以按照下面的方法建立一个堆 $B$：

> 从空堆开始，反复将 $A$ 中元素插入 $B$，每次插入之後都调整元素位置使其仍然是堆，直至 $B$ 中包含 $A$ 中所有元素。

证明：在最坏的情况下，算法的运行时间是 $\Theta(n \log n)$。

### Answer

采用 SIFT-UP 操作，最坏情况下是插入了一个最小值，导致需要将其上渗到顶部去。这样每插入一个元素到第 $k$ 层需要花费的时间是 $\Theta(k)$ 级别的。又考虑到第 $k$ 层大约有 $2^k$ 个元素，因此每构筑一层所花费的时间复杂度是 $\Theta(k \times 2^k)$ 级别的。

求出 $\sum_{k = 0}^{\log n} k \times 2^k$，结果就是 $\Theta(n \log n)$ 啦。

## 6.31

### Question

对于数组 `[27, 13, 31, 18, 45, 16, 17, 53]`，应用算法 SPLIT。

### Answer

选定 27 作为分隔符元素。

`[27, 13, 31, 18, 45, 16, 17, 53]`

采用单指针遍历 SPLIT 法。初始态记录交换目标 `target` 为 0。

```
[27, 13, 31, 18, 45, 16, 17, 53]
     ^^
```

13 小于 27，所以递增 `target` 为 1，并将其与 `A[target]` 交换。

```
[27, 13, 31, 18, 45, 16, 17, 53]
         ^^
```

31 大于 27，什么也不做。

```
[27, 13, 31, 18, 45, 16, 17, 53]
             ^^
```

18 小于 27，所以递增 `target` 为 2，并将其与 `A[target]` 交换。

```
[27, 13, 18, 31, 45, 16, 17, 53]
                 ^^
```

45 大于 27，什么也不做。

```
[27, 13, 18, 31, 45, 16, 17, 53]
                     ^^
```

16 小于 27，所以递增 `target` 为 3，并将其与 `A[target]` 交换。

```
[27, 13, 18, 16, 45, 31, 17, 53]
                         ^^
```

17 小于 27，所以递增 `target` 为 4，并将其与 `A[target]` 交换。

```
[27, 13, 18, 16, 17, 31, 45, 53]
                             ^^
```

53 大于 27，所以什么也不做。

最後，将 27 交换到合适的位置。

```
[17, 13, 18, 16, 27, 31, 45, 53]
```

## 6.32

### Question

对于算法 SPLIT，当算法以输入数组 $A$（$\lbrack 1 \dots n \rbrack$）表示时，执行的元素交换次数记作 $f(n)$（不包括 $A_{\mathrm{low}}$ 同 $A_i$ 交换的次数）。

a) 对于怎么样的数组，$f(n)$ 为 $0$？

b) $f(n)$ 的最大值是？什么时候取到最大值？

## 6.33

### Question

修改算法 SPLIT，使得它按 $x$ 划分 $A\lbrack \mathrm{low} \dots \mathrm{high} \rbrack$ 中的元素。这里的 $x$ 是 $\lbrace A_{\mathrm{low}}, A_{\lfloor \frac {\mathrm{low} + \mathrm{high}} 2 \rfloor}, A_{\mathrm{high}} \rbrace$ 的中项。

利用这一 SPLIT 算法实现的 QUICKSORT 算法的运行时间能有所提升吗？请解释。 

## 6.35

### Question

设 $A$（$\lbrack 1 \dots n \rbrack$）是一整数集。给出一算法重排 $A$ 中元素，使得所有的负整数放到所有非负整数的左边，且应当在 $O(n)$ 时间内完成。