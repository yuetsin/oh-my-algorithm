# Lecture 3 Homework

## [DPV07]

### 7.6

#### Question

#### Answer

### 7.7

#### Question

Find necessary and sufficient conditions on the reals $a$ and $b$ under which the linear program...
$$
\begin{gather*}
\max x + y \\
ax + by \le 1 \\
x, y \ge 0
\end{gather*}
$$

* ...is infeasible.
* ...is unbounded.
* ...has a unique optimal solution.

#### Answer

要找到的是「充分必要」条件。因此单一特值是不够的。

#### Infeasible

先讨论 Infeasible 的情况。Infeasible 等价于可行域是空集。

除去平凡的 $b = 0$ 情况，区域和坐标轴的交点在 $(0, \dfrac 1 b)$ 和 $(\dfrac 1 a, 0)$。

### 7.8

#### Question

You are given the following points in the plane:
$$
(1, 3), (2, 5), (3, 7), (5, 11), (7, 14), (8, 15), (10, 19)
$$
You want to find a line $ax + by = c$ that approximately passes through these points (no line is a perfect fit). Write a linear program (you don't need to solve it) to find the line that minimizes the *maximum absolute error*,
$$
\max_{1 \le 1 \le 7} \lvert ax_i + by_i - c \rvert
$$

#### Answer

### 7.13

#### Question

*Matching pennies*. In this sample two-player game, the players (call them $R$ and $C$) each choose an outcome, *heads* or *tails*. If both outcomes are equal, $C$ gives a dollar to $R$; if the outcome are different, $R$ gives a dollar to $C$.

* Represent the payoffs by a $2 \times 2$ matrix.
* What is the value of this game, and what are the optimal strategies for the two players?

#### Answer

### 7.21

#### Question

An edge of a flow network is called *critical* if decreasing the capacity of this edge results in a decrease in the maximum flow. Give an efficient algorithm that finds a critical edge in a network.

#### Answer

### 7.23

#### Question

A *vertex cover* of an undirected graph $G = (V, E)$ is a subset of the vertices which touches every edge — that is, a subset $S \subset V$ such that for each edge $\{u, v\} \in E$, one or both of $u$, $v$ are in $S$.

Show that the problem of finding the minimum vertex cover in a *bipartite* graph reduces to maximum flow.

> Hint: Can you relate this problem to the minimum cut in an appropriate network?

#### Answer

