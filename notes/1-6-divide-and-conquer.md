# Lecture 6

> 分治策略。

## Divide & Conquer

### Example

来看一个简单的例子。这个算法要求一个数组（长度为 n），

```pseudocode
ALGORITHM 6.1: MINMAX
x <- A[1]
y <- A[1]
for i <- 2 to n
	if A[i] < x then x <- A[i]
	if A[i] > y then y <- A[i]
end for
return (x, y)
```

伪代码不好看，用 Python 改写：

```python
def find_min_max(array: list) -> (int, int):
    # x: min, y: max
    x, y = array[0], array[0]
    n = len(array)
    for i in range(1, n):
        if array[i] < x:
            x = array[i]
        # 这里实际上可以用 elif
        # 因为如果 array[i] < x 就必不可能 > y
        if array[i] > y:
            y = array[i]
    return (x, y)
```

或者，写得更简单一点：

```python
def find_min_max_opt(array: list) -> (int, int):
    if array == []:
        return None, None
    min_v = max_v = array[0]
    for v in array[1:]:
        if v < min_v:
            min_v = v
        elif v > max_v:
            max_v = v
    return min_v, max_v
```

很容易可以看出这个算法所做的事情。

复杂度也很显然，对于一个长度为 $n$ 的数组输入，需要进行 $2(n - 1)$ 次比较，即时间复杂度是 $O(n)$。

### Optimize Attempts

对于这种「涉及到 $n$ 个互不关联数据」的算法，通常来说极限就是 $O(n)$ 了；因为至少要在每个元素上均等地耗费常数时间。

但是，极限是 $O(n)$ 并不意味着我们上面的 $2(n - 1)$ 次比较的算法就是最优的了。

如果我们采用二分策略，给出一个数组时将其拆成两部分，分别求每一部分的最大最小值，然后做一次归并，会怎样？

> 这里当然不必要真的去拆解/拼凑数组。保留一个全局数组，传递索引就好了。

```python
def find_min_max_dvq(array: list) -> (int, int):
    def __minmax(low: int, high: int) -> (int, int):
        if high - low == 1:
            low_v, high_v = array[low], array[high]
            return (low_v, high_v) if low_v < high_v else (high_v, low_v)
        else:
            mid = (low + high) // 2
            x1, y1 = __minmax(low, mid)
            x2, y2 = __minmax(mid + 1, high)
            return min(x1, x2), max(y1, y2)
    if array == []:
        return None, None
    return __minmax(0, len(array) - 1)
```

分析这个算法的复杂度，可以发现对于 $n$ 个元素的问题可以将其拆成两个大约是 $\dfrac n 2$ 个元素的小问题、加上两次比较完成，且在平凡情况下（$n = 1$ 或 $n = 2$）仅仅消耗 $1$ 次比较。

这里，总的比较次数仅仅需要 $\dfrac {3n} 2 - 2$ 次。这就是一个显著的「分治」功效：「解决小问题」多次所消耗的总时间，比起解决「问题的总和」所耗费的时间更短。

### Main Idea

* 将问题拆分成若干个小问题，分别求解；
* 将求出的小规模问题的解合并为一个更大规模问题的解；
* 自底向上逐步求出原问题的解。

![image-20200811172318588](1-6-divide-and-conquer.assets/image-20200811172318588.png)

### Applicable Conditions

并非所有的问题都适合使用分治法求解。

