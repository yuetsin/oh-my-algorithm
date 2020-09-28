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

怎么证明这件事情呢？

#### Answer

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

