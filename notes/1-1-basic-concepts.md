# Lecture 1

## 课本

算法设计技巧与分析，M.H.Alsuwaiyel 写的。

## 课程大纲

![image-20200713172642079](1-1-basic-concepts.assets/image-20200713172642079.png)

## 算法

### 定义

一个算法就是有穷规则的集合，其中的规则规定了一个解决某一个特定问题的运算序列。

### 特征

* 有穷性
	* 执行有穷步后结束

* 确定性
	* 每一步有确定的含义
* 能行性
	* 原则上能精确的进行，用纸和笔有限次完成
* 有输入
	* 不绝对：例如随机数生成算法就无需输入
* 有输出
	* 不绝对：例如数组原地排序算法就不会输出

### 评判标准

* 正确性
	* 最基本的
* 有效性
	* 主要指的是时间、空间的花费是否可接受
* 健壮性
* 可读性

按照算法的有效性（占用时间、空间的多少）可以讲算法分为「易性算法」和「顽性算法」。

时间、空间复杂度在对数级别、多项式级别的算法都可以称之为「易性」。但是指数级别的算法通常称之为顽性的。

## 查找算法

从一组数据之中找到符合要求的那一个。

### 顺序查找

逐个比对数组中的元素。

```python
def linear_search(array: list, target) -> int:
    index = 0
    length = len(array)
    while index < length:
        if array[index] == target:
            return index
        index += 1
    return -1
```

很显然，需要进行元素比较的次数最少需要 $1$ 次（假如目标元素位于头部），最多需要 $n$ 次（假如目标元素位于尾部或不存在）。考虑到 `target` 在列表中均匀分布，这个算法所耗费的时间是 $O(N)$ 级别的。

### 二分查找

这个算法要求输入的数组是已经排序的。

也是很简单的思路：总尽量把待查找的数组一分为二，并且通过中间元素来排除不可能包含目标元素的那一半。

下面的实现基于输入数组 `array` 已经被递增排序。

```python
def binary_search(array: list, target) -> int:
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```

元素比较的次数最少 $1$ 次（假如目标元素刚好位于正中心），最多 $\lfloor \log n \rfloor + 1$ 次。

## 合并算法

把两个已经排序好的数组合成一个，并且保证这个新数组仍然是有序的。

### 简单合并

最简单的思路就是保留两个指针，分别指向两个需要 Merge 的数组；然后从指向的元素中取出比较小的那一个填入结果。依次往後，直到触及了某个数组的结尾。

```python
def plain_merge(array_a: list, array_b: list) -> list:
    pointer_a, pointer_b = 0, 0
    length_a, length_b = len(array_a), len(array_b)

    result = []

    while pointer_a < length_a and pointer_b < length_b:
        if array_a[pointer_a] <= array_b[pointer_b]:
            result.append(array_a[pointer_a])
            pointer_a += 1
        else:
            result.append(array_b[pointer_b])
            pointer_b += 1

    if pointer_a != length_a:
        result += array_a[pointer_a:]
    elif pointer_b != length_b:
        result += array_b[pointer_b]

    return result
```

双指针，挺好写的。

复杂度分析，比较次数最少需要 $\min \lbrace A_{size}, B_{size} \rbrace$ 次；最多需要 $A_{size} + B_{size} - 1$ 次。

赋值次数肯定是 $A_{size} + B_{size}$ 次。

## 排序算法

### 选择排序

