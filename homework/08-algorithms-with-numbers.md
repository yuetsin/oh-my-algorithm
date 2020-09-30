# Lecture 2 Homework

## [DPV07]

### 1.8

#### Question

Justify the correctness of the recursive division algorithm given in page 26, and show taht it takes time $O(n^2)$ on $n$-bit inputs.

---

验证 [DPV07] 第 26 页给出的递归除法算法，并验证她对于 $n$ 位的输入，运行时间是 $O(n^2)$ 的。

#### Answer

这个算法改写成计算机语言是这样的：

```python
#  input: two n-bit integers x and y
#         y >= 1
# output: the quotient and remainder
#         of x divided by y
def divide(x: int, y: int) -> (int, int):
    if x == 0:
        return 0, 0
    q, r = divide(x // 2, y)
    q *= 2
    r *= 2
    if x % 2:
        r += 1
    if r >= y:
        r -= y
        q += 1
    return q, r
```

显然，每个 `divide` 中，除去执行流不变部分（9 至 16 行），就是第 8 行有递归了。

然而递归执行的次数呢？看 `x` 能除以多少次 `2`。

因为 `x` 是 $n$ 位长的，所以递归的次数自然也就是 $n$ 次。

再来分析每一次递归内的耗时。

`q *= 2` 和 `r *= 2`，只做一个左移位操作。$O(n)$。

`x % 2` 判断，只要看最後一位。$O(1)$。

`r += 1`、`r -= y`、`q += 1`。都是加法，$O(n)$。

`r >= y` 判断，最坏情况下要检查 $n$ 位。$O(n)$。

综合起来，每一次循环体内的耗时是 $O(n)$。

因此总的时间复杂度就是 $O(n^2)$。完毕。

### 1.20

#### Question

Find the inverse of: $20 \pmod{79}$, $3 \pmod{62}$, $21 \pmod{91}$, $5 \pmod{23}$.

---

找出下面四组模逆：$20 \pmod{79}$、$3 \pmod{62}$、$21 \pmod{91}$、以及 $5 \pmod{23}$。

#### Answer

这个没什么意思…

* 因为 $20 \times 4 \equiv 1 \pmod{79}$，因此在 $\bmod 79$ 的情况下，$20$ 的模逆是 $4$。
* 因为 $3 \times 21 \equiv 1 \pmod{62}$，因此在 $\bmod 62$ 的情况下，$3$ 的模逆是 $21$。
* 因为 $21 = 3 \times 7$，$91 = 3 \times 17$，因此 $21$ 和 $91$ 不互素，模逆不存在。
* 因为 $5 \times 14 \equiv 1 \pmod{23}$，因此在 $\bmod 23$ 的情况下，$5$ 的模逆是 $14$。

### 1.22

#### Question

Prove or disprove: If $a$ has an inverse modulo $b$, then $b$ has an inverse modulo $a$.

---

证明或证伪：如果 $a$ 在某个模下有模逆元 $b$，那么 $b$ 也有模逆元 $a$。

#### Answer

模逆元的定义是 $a b \equiv 1 \pmod{N}$。

互反性显然的。

### 1.31

#### Question

Consider the problem of computing $N! = 1 \times 2 \times 3 \times \dots \times N$.

1. If $N$ is an $n$-bit number, how many bits long is $N$, approximately in $\Theta(·)$ form?
2. Give an algorithm to compute $N!$ and analyze its running time.

---

1. 如果 $N$ 是一个 $n$ 位长的数字，那么估计 $N!$ 的位长大概是多少？用 $\Theta(·)$ 形式表示。
2. 给出一个计算 $N!$ 的算法，并分析其时间复杂度。

#### Answer

$N$ 是一个 $n$ 位长的数字，即 $n = \Theta(\log N)$。

因此，$\log(N!) = \log(1 \times 2 \times 3 \times \dots \times N)$，从而等于 $\log 2 + \log 3 + \dots + \log N$。

显然，乘积的位长应该是 $O(N\log N)$ 的，也就是 $O(n ·k^n)$ 的。这是上限。那么下限呢？

由于 $f(x) = \log x$ 是凸函数，因此这个求和的值应该小于 $\dfrac {N \times \log N} 2$。因此还是 $o(N\log N)$，即 $o(n · k^n)$。

从而，$N!$ 的位长大概是 $\Theta(n · k^n)$。

---

我给出的算法…比较无能为力。

```python
def fact(n: int) -> int:
    return n * fact(n - 1) if n > 1 else 1
```

对于函数调用 `frac(M)`，他需要将 `frac(M - 1)` 的结果和 `M` 相乘。

`frac(M - 1)` 的位长是 $\Theta(M \log M)$，也就是 $Theta(m · 2^m)$。因此这个乘法的代价就是 $\Theta(m^2 \times 2^m)$。

一共要进行 `n - 1` 次这样的乘法，因此总的代价是 $\sum_{i = 1}^n i^2 \times 2^i$。

运用错位相减法也好，级数求和手段也好。反正总的时间复杂度就是这样了。

毫无意义的算法。不可能会这么计算的。

### 1.34

#### Question

On page 38, we claimed that since about $\dfrac 1 n$ fraction of $n$-bit numbers are prime, on average it is sufficient to draw $O(n)$ random $n$-bit numbers before hitting a prime. We now justify this rigorously.

Suppose a particular coin has a probability $p$ of coming up heads. How many times must you toss it, on average, before it comes up heads?

> Hint: Method 1: start by showing that correct expression is $\sum_{i = 1}^{\infin} i (1 - p)^{i - 1} p$. Method 2: if $E$ is the average number of coin tosses, show that $E = 1 + (1 - p) E$.

---

在 [DPV07] 的第 38 页，我们说因为在 $n$ 位长的数字之中，大概有 $\dfrac 1 n$ 是质数。平均来说，我们需要 $O(n)$次尝试才能碰上一个。

#### Answer

怎么证明这件事情呢？

因为质数的分布密度是 $\dfrac 1 n$，因此我们随机在 $n$ 位长的数字中挑选一个，大概有 $\dfrac 1 n$ 的机率找到一个质数。

实际上，因为每一次我们都挑选不同的数字进行尝试，即「失败的尝试也可以为我们排除一部分合数」，因此实际的概率要比这个高上一点，可以忽略不计。

因此，可以把「猜质数」这件事情看成是各次独立的 Bernoulli 实验。经过 $k$ 次尝试找到质数，服从几何分布 $G(\dfrac 1 n)$。

概率分布为 $P\{X = k\} = (1 - \dfrac 1 n)^{k - 1} \times \dfrac 1 n$。

于是，其数学期望为 $\sum_{i = 1}^{\infin} i \times P\{X = i\} = \sum_{i = 1}^{\infin} i \times (1 - \dfrac 1 n)^{i - 1} \times \dfrac 1 n$。

容易求出此级数收敛于 $n$。因此预计需要 $O(n)$ 次尝试才能碰到一个质数。

> 几何分布。

### 1.35

#### Question

Wilson's theorem says that a number $N$ is prime if and only if
$$
(N - 1)! \equiv -1 \pmod{N}
$$

1. If $p$ is prime, then we know every number $1 \le x \lt p$ is invertible modulo $p$. Which of these numbers are their own inverse?
2. By pairing up multiplicative inverses, show that $(p - 1)! \equiv -1 \pmod{p}$ for prime $p$.
3. Show that if $N$ is *not* prime, then $(N - 1)! \not\equiv -1 \pmod{N}$. (Hint: Consider $d = \gcd(N, (N - 1)!)$.)
4. Unlike Fermat's Little theorem, Wilson's theorem is an if-and-only-if condition for primality. Why can't we immediately base a primality test on this rule?

---

基于威尔逊（素数判定）定理的出题。

#### Answer

「威尔逊素数判定定理」和「费马小」之流不同。她是「判定素数」的充分必要条件。

下面一题一题看。

1. 如果 $p$ 是质数，那么 $[1, p)$ 内的任何整数，都可以在 $\pmod{p}$ 下取逆元。哪些数字的逆元等于他们自己呢？

按照定义来…逆元等于自己的数字 $x$ 一定满足：
$$
x \times x \equiv 1 \pmod{p}
$$
即，$x^2 \equiv 1 \pmod{p}$，即 $x^2 = kp + 1$ 的整数解。

回答：满足 $x = \sqrt{kp + 1}$ 且为整数的 $x$。一定凑出 $x = \sqrt{(np + 1)^2} = np + 1$ 这样的形式。（固定了零次项的结果。）

因此，最後 $x \bmod p$ 只能等于 $1$ 或者 $p - 1$；当 $n \ge 0$ 时 $x \equiv 1 \pmod{p}$；当 $n \lt 0$ 时 $x \equiv p - 1 \pmod{p}$。

因此，在 $\bmod p$ 的情况下，只有 $1$ 和 $p - 1$ 两个数字的逆元是他们自己。

---

2. 证明对素数 $p$ 来说，$(p - 1)! \equiv -1 \pmod{p}$。

证明：先考虑 $p \gt 2$ 的非平凡情况。

因为是素数，因此 $(p - 1)!$ 内没有任何 $p$ 的因子，即 $(p - 1)!$ 和 $p$ 互素。$(p - 1)!$ 存在 $\pmod{p}$ 下的模逆。

同样，因为对于任何 $[1, p)$ 内的整数，都在 $\pmod{p}$ 下取逆元，且逆元仍然落在 $[1, p)$ 内。

同时，$1$ 和 $p - 1$ 特别地，模逆元是自己。其他的 $p - 3$ 个数字，彼此对应为模逆。

> 因为大于 2 的素数全部都是奇数，因此这 $p - 3$ 个数字一定是可以两两对应的。

即，存在这样的一大堆关系：

* $1 \times 1 \equiv 1 \pmod{p}$
* $2 \times I_2 \equiv 1 \pmod{p}$。
* $\dots$
* $(p - 1) \times (p - 1) \equiv 1 \pmod{p}$

除去最後一个式子、左右两边全部乘起来，得到：
$$
(p - 2)! \equiv 1 \pmod{p}
$$
最後两边乘以 $p - 1$，得到：
$$
(p - 1)! \equiv p - 1 \equiv -1 \pmod{p}
$$
最後讨论 $p = 2$ 的平凡情况；$(2 - 1)! \equiv -1 \pmod{2}$ 显然。

证完。

---

3. 证明：对于合数 $N$，一定有 $(N - 1)! \not\equiv -1 \pmod{N}$。

既然 $N$ 是合数，那么对其进行质因数分解，所有的因数都一定落在 $\{1, 2, \dots, N\}$ 之中。

即，存在一个大于 1 的整数 $d = \gcd(N, (N - 1)!)$。

因此，$(N - 1)!$ 在 $\pmod{N}$ 下不存在逆元。即，不存在一个 $k$ 使得
$$
k (N - 1)! \equiv 1 \pmod{N}
$$
现在用反证法。假设对于某个合数有 $(N - 1)! \equiv -1 \pmod{N}$ 存在，那么两边同乘 $N - 1$ 有

$(N - 1) \times (N - 1)! \equiv - (N - 1) \equiv 1 - N \equiv 1 \pmod{N}$ ，即得到了 $(N - 1)!$ 存在模逆 $N - 1$。

这和模逆基本定理矛盾，因此对任何一个合数都应该有 $(N - 1)! \not\equiv -1 \pmod{N}$。

证完。

---

4. 既然 Wilson 的判定定理是 iff 的，那我们为什么还是无法得到一个「有效的」素数判定算法呢？

这还用说…去看 1.34，算 $(N - 1)!$（即便是在 $\pmod{N}$ 下）复杂度都要上天了。

