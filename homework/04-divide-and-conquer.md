# Lecture 6 Homework

## 6.3

### Question

导出一个迭代的求最小值、最大值的算法，要求仅用 $\dfrac {3n} 2 - 2$ 次比较，在一个 $n$ 元素的集合中找出最大值和最小值。

假定 $n$ 是 $2$ 的整数次幂的形式。

### Answer

很显然，只需要 $n - 1$ 次比较就能找出最大值**或**最小值。但是这样的话一共需要 $2n - 2$ 次比较才能得到最大值**和**最小值。怎么办？

因为 $n = 2^k$，因此始终可以将问题分解为两部分。而平凡情况就是 $n = 2^1 = 2$ 的时候，这时仅仅需要一次比较就可以返回最大值和最小值。

现在考虑将两个子问题合并。左右两个数组各自包含最大值和最小值。很显然，$V_\max = \max \{ L_\max, R_\max\}$，且 $V_\min = \min\{L_\min, R_\min\}$。所以合并子问题需要 2 次比较。

很容易地写出对应的代码：

```python
#!/usr/bin/env python

def minmax(array: list) -> (int, int):
    global compare_count
    length = len(array)
    if length == 2:
        left, right = array[0], array[1]
        return (left, right) if left < right else (right, left)

    min1, max1 = minmax(array[:length // 2])
    min2, max2 = minmax(array[length // 2:])
    return min(min1, min2), max(max1, max2)
```

试着运行一下，并统计其比较次数：

```
array list, compare count: (2, 1)
array list, compare count: (4, 4)
array list, compare count: (8, 10)
array list, compare count: (16, 22)
array list, compare count: (32, 46)
array list, compare count: (64, 94)
array list, compare count: (128, 190)
array list, compare count: (256, 382)
array list, compare count: (512, 766)
array list, compare count: (1024, 1534)
array list, compare count: (2048, 3070)
```

![image-20200907110610286](04-divide-and-conquer.assets/image-20200907110610286.png)

绘图可以发现，有着很好的线性关系。而且，比例越来越接近于 $\dfrac 3 2$。

![image-20200907110807969](04-divide-and-conquer.assets/image-20200907110807969.png)

从数学角度分析，每两个元素之间都被比较了一次（最平凡的情况时）。因此带来了 $\dfrac n 2$ 次比较。

除此之外，在对 $\log_2n = k$ 层归化进行整理时，显然地有：第 $i$ 层有 $2^{i - 1}$ 个子部分，需要 $2^{i - 2}$ 次整合。而每次整合伴随着 2 次比较，所以每一层都需要 $2^{i - 1}$（$ i \ge 2$）次比较才能合并到第 $i - 1$ 层。所以总共需要进行的比较次数是 $\sum_{i = 2}^k 2^{i - 1}$ 次，即 $2^k - 2$ 次。即 $2^{\log_2 n} - 2 = n - 2$ 次。 

因此，总的求和次数是 $\dfrac 3 2 n - 2$ 次。完毕。

## 6.7

### Question

修改算法 BINARYSEARCHREC，使得它可以搜索两个关键字。换句话说，给出一个由 $n$ 个元素组成的数组 $A \lbrack 1 \dots n \rbrack$ 和两个元素 $x_1$、$x_2$，返回他们俩在数组中的索引 $k_1$ 和 $k_2$。

### Answer

BINARYSEARCHREC 是这样的：

```python
def binarysearchrec(low: int, high: int) -> int:
    global array, target
    if low > high:
        return -1
    mid = (low + high) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binarysearchrec(low, mid - 1)
    else:
        return binarysearchrec(mid + 1, high)
```

很简单地，为了避免写成「调两次 `binarysearchrec`」，这里用了一些手段来减少没有用的递归。

简单说，如果说要求的两个 `target` 都位于同一半，那么就递归调用自己；如果两个 `target` 分立在两侧，就退化为两次 `binarysearchrec` 的调用。

```python
def __binarysearchrec(low: int, high: int, target: int) -> int:
    global array
    if low > high:
        return -1
    mid = (low + high) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return __binarysearchrec(low, mid - 1, target)
    else:
        return __binarysearchrec(mid + 1, high, target)


def binarysearchrecdup(low: int, high: int, no_left: bool = False, no_right: bool = False) -> (int, int):
    global array, target_a, target_b
    if low > high:
        return -1, -1

    mid = (low + high) // 2

    if no_left:
        return None, __binarysearchrec(low, high, target_b)
    elif no_right:
        return __binarysearchrec(low, high, target_a), None

    if target_b < mid:
        # target_a < target_b < mid
        return binarysearchrecdup(low, mid - 1)
    elif target_a < mid < target_b:
        # target_a < mid < target_b
        left, _ = binarysearchrecdup(low, mid - 1, False, True)
        _, right = binarysearchrecdup(mid + 1, high, True, False)
        return left, right
    else:
        # mid < target_a < target_b
        return binarysearchrecdup(mid + 1, high)
```

## 6.19

### Question

设 $A \lbrack 1 \dots 105 \rbrack$ 是一个已排序的、包含 $105$ 个整数的数组。假设我们运行算法 SELECT，试图找出其中第 $17$ 小的元素。对于此过程，将有多少次递归调用？

请明确解释你的答案。

### Answer

## 6.27

### Question

设 $A \lbrack 1 \dots n \rbrack$ 和 $B \lbrack 1 \dots n \rbrack$ 是两个已按升序排列的整数数组，且其中所有整数都互不相同。请给出一个有效的算法找出这 $2n$ 个元素的中项。

你的算法运行时间是多少？

### Answer

## 6.32

### Question

对于算法 SPLIT，当输入为 $A \lbrack 1 \dots n \rbrack$、且不考虑 $A_\mathrm{low}$ 和 $A_i$ 交换耗费时，执行的元素交换次数记为 $f(n)$。

#### a)

对于什么样的输入数组，$f(n) = 0$？

#### b)

$f(n)$ 的最大值是？何时取到？

### Answer

## 6.52

### Question

给出一个分治算法，在一个具有 $n$ 个数的数组中找出第二大的元素。

请一并给出算法的时间复杂性分析。

### Answer