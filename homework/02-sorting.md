# Lecture 2 Homework

## 4.5

### Question

写一个有效算法来测试一个给定的数组是否是一个堆（Heap）。该算法的时间复杂度是多少？

## 4.15

### Question

给出一个整数数组 $A$（$\lbrack 1 \dots n\rbrack$），可以按照下面的方法建立一个堆 $B$：

> 从空堆开始，反复将 $A$ 中元素插入 $B$，每次都通过 SIFT-UP 方法调整堆，直至 $B$ 中包含 $A$ 中所有元素。

证明：在最坏的情况下，算法的运行时间是 $\Theta(n \log n)$。

## 6.31

### Question

对于数组 `[27, 13, 31, 18, 45, 16, 17, 53]`，应用算法 SPLIT。

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