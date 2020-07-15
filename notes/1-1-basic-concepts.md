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

为了放入第 $i$ 个元素的位置，我们只需要找出第 $i$ 小的元素即可。

这样，我们可以从左到右开始，在我们已经把 $i - 1$ 个元素都放置到位后，就可以直接在剩下的 $n - i + 1$ 个元素中找出最小的那个（这一定就是第 $i$ 小的元素了），将其同第 $i$ 位元素交换即可。

```python
def selection_sort(array: list):
    for i in range(len(array) - 1):
        min_value = min(array[i:])
        min_index = array.index(min_value, i)

        if min_index == i:
            # already in-place
            continue
        else:
            array[i], array[min_index] = array[min_index], array[i]
```

元素比较的次数是 $\dfrac {n(n - 1)} 2$，因为每两个元素之间都要进行一次比较。

而元素的赋值次数和原始数组的情况有关；假如原始数组已经有序，则不需要任何赋值；但如果原始数组是完全反序的，则需要 $3(n - 1)$ 次赋值。

> 因为每次交换需要三次赋值，这要记住。

### 插入排序

这也是简单的。把前 $i$ 个元素视作有序的，然后把第 $i + 1$ 个元素放置在合适的位置，使得前 $i + 1$ 个元素都有序。这样一次排开。

> 和选择排序很类似，都是把前置的有序数组一个一个延长。不同的是选择排序每次都从后续数组中选出最小的加入排序过的数组中；而插入排序总是采取临近的那个元素。

```python
def insertion_sort(array: list):
    for i in range(2, len(array)):
        to_insert = array[i]
        if array[i - 1] <= x:
            # that's already in place. no need to do anything
            continue
        insert_point = -1
        for j in range(i - 1):
            if array[j] >= to_insert:
                # found the insert point!
                insert_point = j
                break
        if insert_point == -1:
            # to_insert value in place. no need to change anything
            continue
        else:
            # crude implementation
            # could have merely modify values between array[insert_point:i]
            # but here it modifies array[insert_point:] totally
            del array[i]
            array.insert(insert_point, to_insert)
```

这种策略对于链表型数组还比较有用；但对于普通型数组来说，赋值次数太多（大部分都是插入一个值，后面的所有元素跟着移动）。一般不会用的。

比较次数最少是 $n - 1$ 次（假如完全有序，那么跑一遍就够了）。最多则是 $\dfrac {n(n-1)} 2$ 次。

赋值的次数是「比较的次数」+ $n - 1$ 次。

### 归并排序

用图来说明更简单：

![image-20200714111038565](1-1-basic-concepts.assets/image-20200714111038565.png)

借用了上面我们用到的 Merge 算法。

```python
from plain_merge import plain_merge

# simplified implementation. not considering list copy costs.
def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    split_point = len(array) // 2
    left_side, right_side = array[:split_point], array[split_point:]
    return plain_merge(merge_sort(left_side), merge_sort(right_side))
```

注意，这里为了体现算法，直接把 `list` 做了拷贝处理。可以很简单地改成传递起讫索引而避免拷贝的实现。

忽略拷贝的开销，这个算法的复杂度是…？

以数组大小 $n = 2^k$ 来讨论。这样 `merge_sort` 一共被分拆了 $k = \log n$ 次；每一层都对 $n$ 个元素进行了归并，因此一共进行的归并元素个数是 $n \log n$ 个；时间复杂度自然就是 $O(n \log n)$ 啦。

## 效率衡量

所谓的「效率」，指的是算法在输入规模变化的情况下，消耗时间的变化情况。也可以称为「时间复杂度」。

### 评估方法

* 事后统计
	* 试着给不同的输入并运行程序
	* 进行统计学分析
* 事前统计
	* 分析程序源代码，估算复杂度

### 事前统计法

算法 = 控制结构 + 原操作

> 所谓原操作，就是运算耗时同输入无关的操作。，或者说固有数据类型的操作。

因此算法的执行时间 = $\sum$ 原操作的执行次数 × 原操作的执行时间。

很显然，算法的执行时间就同原操作执行次数成正比。

可以认为，算法的运行时间 $f(n)$ 同输入的数据量 $n$ 成一函数关系。

### 数学表记

#### $O$ 表记法

令 $f(n)$ 和 $g(n)$ 是两个定义在自然数集上的函数。

假如 $\exist c > 0, \exist n_0 \gt 0$，使得 $\forall n \ge n_0$，都有 $f(n) \le cg(n)$，那么我们可以说 $f(n)$ 是 $O(g(n))$ 复杂度的。

根据极限的定义，这句话也可以写成：
$$
\lim _{n \to +\infin} \dfrac {f(n)} {g(n)} \ne \infin \implies f(n) = O(g(n))
$$
即，在 $n \to + \infin$ 时，$\dfrac {f(n)} {g(n)}$ 趋于一常数（可以是 0）。

从直觉上来说，意思是在 $n$ 增大时，$f(n)$ 的增长不快于 $g(n)$ 的增长。

#### $\Omega$ 表记法

$$
\lim _{n \to +\infin} \dfrac {f(n)} {g(n)} \ne 0 \implies f(n) = \Omega(g(n))
$$

（$\lim _{n \to +\infin} \dfrac {f(n)} {g(n)} = \infin$ 也算在 $\ne 0$ 的情况里了）。

从直觉上来说，意思是在 $n$ 增大时，$f(n)$ 的增长不慢于 $g(n)$ 的增长。

所以，有下面的式子：
$$
f(n) = \Omega(g(n)) \iff g(n) = O(f(n))
$$

#### $\Theta$ 表记法

$$
\lim _{n \to +\infin} \dfrac {f(n)} {g(n)} = C \ne 0 \implies f(n) = \Theta(g(n))
$$

从直觉上来说，意思是在 $n$ 增大时，$f(n)$ 的增长和 $g(n)$ 的增长基本同步（当然也可能常数级别地成比例）。

根据简单的极限运算法则，可以发现：
$$
f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \and g(n) = O(f(n))
$$

#### 例子

以下式子都是正确的：

* $10n^2 + 20n = O(n^2)$
* $\log {n^2} = O(n)$
* $\log {n^k} = \Omega(\log n)$
* $n! = O((n + k)!)$（$k$ 取任意自然数）

在研究算法复杂度的情况下，我们一般不使用 $\Omega$ 表记法，因为理论上任何算法的复杂度都是 $\Omega(C)$ 级别的（不可能比常数级别增长还慢吧？），我们对最佳情况并不感兴趣。

而用 $\Theta$ 表记法又有些不方便，因为有些算法并不能很好地用一个函数式来表示其复杂度。

事实上我们关心的只是「最坏情况」，即最差的情况下所耗费的时间复杂度。因此一般用 $O$ 表记法即可。

> 注意，尽管 $O$ 表记法并不要求精确逼近，也就是说你用一个增长远远快过原函数的方程式来做表记也是正确的。但是在研究算法复杂度的时候，还是得用最贴近的那个表达式来做 $O$ 表记，否则算错。

### 复杂度表记

#### $o$ 表记

$$
\lim _{n \to +\infin} \dfrac {f(n)} {g(n)} = 0 \implies f(n) = o(g(n))
$$

严格版的 $O$ 表记，排除了 $f(n)$ 和 $g(n)$ 等阶的情况。

#### $\omega$ 表记

$$
\lim _{n \to +\infin} \dfrac {f(n)} {g(n)} = \infin \implies f(n) = \omega(g(n))
$$

严格版的 $\Omega$ 表记，排除了 $f(n)$ 和 $g(n)$ 等阶的情况。

### 复杂度比较

$$
C \prec \log\log n \prec \log n \prec \sqrt{n} \prec n^{\frac 3 4} \prec n \prec n \log n \prec n^2 \prec 2^n \prec n! \prec 2^{n^2}
$$

### 复杂度的性质

#### 传递性

$$
f(n) = \Theta(g(n)) \and g(n) = \Theta(h(n)) \implies f(n) = \Theta(h(n))
$$

$$
f(n) = O(g(n)) \and g(n) = O(h(n)) \implies f(n) = O(h(n))
$$

$$
f(n) = \Omega(g(n)) \and g(n) = \Omega(h(n)) \implies f(n) = \Omega(h(n))
$$

$$
f(n) = o(g(n)) \and g(n) = o(h(n)) \implies f(n) = o(h(n))
$$

$$
f(n) = \omega(g(n)) \and g(n) = \omega(h(n)) \implies f(n) = \omega(h(n))
$$

#### 自反性

$$
f(n) = \Theta(f(n))
$$

$$
f(n) = O(f(n))
$$

$$
f(n) = \Omega(f(n))
$$

$$
f(n) \ne o(f(n))
$$

$$
f(n) \ne \omega(f(n))
$$

#### 对称性

$$
f(n) = \Theta(g(n)) \iff g(n) = \Theta(f(n))
$$

$$
f(n) = O(g(n)) \iff g(n) = \Omega(f(n))
$$

$$
f(n) = o(g(n)) \iff g(n) = \omega(f(n))
$$

#### 特殊情况

有些函数不是可比的。

即，可能存在两个函数 $f(n)$ 和 $g(n)$，存在 $f(n) \ne O(g(n))$，$f(n)$ 也 $\ne \Omega(g(n))$。

### 复杂度的运算

#### 加法准则

两个复杂度函数相加，结果是其中增长较快的那个复杂度函数。
$$
O(f_1(n)) + O(f_2(n)) = O(\max \lbrace f_1(n), f_2(n) \rbrace)
$$

#### 乘法准则

两个复杂度函数相乘，结果是两式直接相乘。
$$
O(f_1(n)) \times O(f_2(n)) = O(f_1(n) \times f_2(n))
$$

### 算法复杂度估计

#### 简单估计

直接估计原操作的个数来估计算法的复杂度。

大部分算法都可以这么处理。

#### 平摊估计

这里是一个特殊的算法例子：

```python
for j in range(n):
    x = A[j]
    List.Add(x)
    if x % 2 == 0:
        for pred in x.Predecessors:
            if pred % 2 == 1:
            	List.Delete(pred)
```

这个算法构造一个双向链表，初始时由一个节点组成。输入 $X$，如果 $X$ 是奇数， 将 $X$ 添加到表中。如果 $X$ 是偶数，将 $X$ 添加到表上，然后移去表中所有在 $X$ 之前的奇数元素。

仅仅考虑「插入节点」和「删除节点」两个原操作，这个算法的复杂度是多少？

似乎如果我们插入的 $n$ 个数全部是奇数，那么复杂度仅仅是 $O(n)$；但如果我们插入的是偶数节点，那么复杂度就是 $O(n^2)$。那么我们直接说这个算法的复杂度是 $O(n^2)$ 就好了吗？

我们应用一下平摊估计：在最坏情况下，每个曾经插入的奇数节点都会被删除。即，最多能执行 $n$ 次插入，最多也只能进行 $n - 1$ 次删除。

因此，对于 $n$ 个数字的输入（无论其奇偶组成为何），原操作的个数最多不可能超过 $2n - 1$ 次。

因此，这是一个 $O(n)$ 复杂度的算法。

### 特殊情况

在我们看到这样一个算法时：

```c
int add_two_numbers(int a, int b) {
    return a + b;
}
```

会毫不犹豫地指出，这是一个 $O(1)$（常数时间）复杂度的算法，即无论给出的输入为何，这个算法都能在常数时间内完成。

这是因为实际上输入的值是有限的；`int` 类型的值不能携带任意长的数字。

但考虑下面这个算法：

```python
def add_two_numbers(a: int, b: int) -> int:
    return a + b
```

在 Python 3 中，`int` 没有任何长度限制。假如我们传入的 `a` 是 $2^{1024} - 42$，`b` 是 $40$，那么显然这时候的加法就不是常数时间的了；按照一般大数加法的实现来看，其复杂度同数字的二进制表示长度成正相关。

也就是说，这个算法的复杂度变成了 $O(\max \lbrace \log a, \log b \rbrace)$。

同理，大整数乘法的复杂度就是 $O(\log a \times \log b)$。

在后面的部分中会有需要用到大数运算的分析。总之，大数字不要把它当作数字，把它当作数位组成的数组对待即可。

## 作业

* 1.5
* 1.9
* 1.13
* 1.16
* 1.17*
* 1.25*
* 1.31
* 1.32*
* 1.33*
* 1.37

> 带有 * 标记的题目较难，是选做题目。

