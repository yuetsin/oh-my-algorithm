# Lecture 1 Homework

 ## [DPV07]

> 指 Sanjoy **D**asgupta，Christos H. **P**apadimitriou，和 Umesh V. **V**azirani 所著的「Algorithms」。

### 8.3

#### Question

STINGY SAT is the following problem: given a set of clauses (each a disjunction of literals) and an integer $k$, find a satisfying assignment in which at most $k$ variables are `true`, if such an assignment exists. Prove that STINGY SAT is NP-Complete.

---

吝啬可满足问题。即，给出一组变元组成的语句、以及一个整数 $k$。问是否存在一个至多 $k$ 个变元为真的指派，使得原语句为真。

#### Answer

首先这是一个判定问题。

而且，如果能找出一组正例，即「至多 $k$ 个变元为真、且使得原语句为真的指派」，那么就可以在多项式时间内对其进行验证（代入运算即可），并给出肯定的回答。因此，这是一个 NP 问题。

下面，证明「所有 NP 问题都可以规约到这个问题」。因为已知「所有 NP 问题都可以规约为 NP-C 问题」，因此我们只要任意找出一个 NP-C 问题，将其规约到 STINGY-SAT 问题，即可证明此问题是 NP-C 的。下面进行规约。

对于任何一个输入为 $m$ 个 Clauses、$n$ 个变元的任意 SAT 问题，可以将其转化为同样 Clauses、同样 Variables、且 $k = n$ 的吝啬可满足问题，且两个问题同真同假。

这一过程可以在多项式时间内完成。因此，可以说任意 SAT 问题 $\propto_{poly}$ STINGY-SAT 问题。

因此，STINGY-SAT 问题是一个 NP 完全问题。

### 8.7

#### Question

Consider a special case of 3-SAT in which all clauses have exactly three literals, and each variable appears three times. Show that this problem can be solved in polynomial time.

---

考虑一个特殊化的 3-SAT 问题：在这个问题中每个 Clause 都恰好包含三个变元，而且每个变元恰好出现三次。

证明这个问题可以在多项式时间内解决。

#### Answer

先证引理 Hall's Theorem（霍尔婚姻定理）。

> 以下举例全部基于 Heterosexual、Cisgender 的假定（

把所有的女孩放入集合 $F = \{F_1, F_2, \dots, F_N\}$；男孩放入集合 $M = {M_1, M_2, \dots, M_N}$。现在每个女孩选择（任意多个）理想的伴侣，即存在一个「所有女孩」到「所有男孩集合」的映射（$\Phi: F \rightarrow 2^M$）。

> $2^M$ 指所有「男孩的子集合」的集合。显然其中一共有 $2^N$ 个元素。

那么，问是否存在一个两两的配对，使得所有女孩的愿望都能得到满足？

Hall 说：如果对所有的 $F$ 的子集合，都存在
$$
\left|\bigcup_{F_{i} \in S} \Phi\left(F_{i}\right)\right| \geq|S|
$$
即，对任何一个包含 $S$ 个女孩的「女孩 子集合」，如果将她们的理想伴侣名单合并、除去重复项後的数量都大于 $S$，那么就一定存在一个「完美配对」。

> 其否命题是显然正确的。

抽象一点说，给出一幅二分图，其中的独立集分别名为 $U$ 和 $V$。如果任何一个 $U$ 的子集合（其中包含 $S$ 个节点）所连接到的 $V$ 节点数量都不小于 $S$，则一定存在一个完美配对。

这就是 Hall's Theorem。注意它只能告诉我们「存在与否」，但不能构造出实际配对。

> 这里不证明了。

现在，我们按照 3-SAT（AT MOST 3 OCCURRENCES）的问题来构造二分图。

假设存在 $n$ 个变元。那么，他们在整个谓词逻辑中一共应当出现 $3n$ 次；又因为每个语句都应该包含 3 个变元，因此也应当有 $n$ 个语句。

这样，把所有的 $n$ 个语句都作为节点构造为一个独立集 $U$；把所有的 $n$ 个变元都作为节点构造为另一个独立集 $V$。每个语句之中出现的变元都用边来连接。

由于是 3-SAT 问题，因此每一个语句节点都一定连接到恰好 3 个变元节点上。又因为 AT MOST 3 OCCURENCES 条件，每个变元也连接到三个语句上。

因此，任意从 $U$ 中挑选 $k$ 个节点，即存在了 $3k$ 条边；但是，由于 $V$ 中每个节点的边数都不超过 $3$，因此这 $3k$ 条边一定不会连接到少于 $k$ 个节点。因此，Hell's Theorem 条件得以满足，即存在一个配对。

即，原问题可在多项式时间内解出（可以回答是或否，但是没有办法找出一个确定的值）。

## [Als99]

### 10.3

#### Question

对 10.2 节中定义的 2 着色问题设计一个多项式时间的算法。

#### Answer

首先，如果图有多个不相连的子图构成，那么可以对其中每一个子图运用 2 着色算法，得到一组着色方式。因此这里只考虑连通图的情况。

给出一个连通图，任取一个点开始着色。假设调色盘中仅有黑白两色。于是给该点直接相连的点给予不同于起始点的颜色。如果同时和多个点相连，直接失败（无法着色）。

> 相当于一个深度优先算法。

```python
def assign_color(node, color) -> bool:
    nodes = node.get_neighbors()
    if len(nodes) > 1:
        return False
    elif len(nodes) == 0:
        return True
    target_node = nodes[0]
    if target_node.is_assigned:
        return target_node.assign_color != color
    else:
        return assign_color(target_node, !color)
```

### 10.5

#### Question

设 $I$ 是着色问题的一个实例，并设 $s$ 被宣称是 $I$ 的一个着色解。描述一个确定性的算法来试验 $s$ 是否真是 $I$ 的一个解。

#### Answer

这个简单。

```python
def validate_colors(graph) -> bool:
    if graph.colors > k:
        return False
    
    for edge in graph:
        if edge.node_a.color == edge.node_b.color:
            return False
    return True
```

检查总颜色的个数，再检查每条边是否连接到了同色节点，就好了。

### 10.9

#### Question

设 $\Pi_1$ 和 $\Pi_2$ 是两个问题，且 $\Pi_1 \propto_{poly} \Pi_2$。假设问题 $\Pi_2$ 可以在 $O(n^k)$ 时间内解出，且规约可以在 $O(n^j)$ 时间内完成。证明：问题 $\Pi_1$ 可以在 $O(n^{jk})$ 时间内解出。

#### Answer

假设算法 $A$ 是将 $\Pi_1 \propto_{poly} \Pi_2$ 的算法，算法 $B$ 是求解 $\Pi_2$ 的算法。$A$ 的时间复杂度是 $O(n^j)$。$B$ 的时间复杂度是 $O(n^k)$。

> 但是，千万不能认为整个过程的时间复杂度就是 $O(n^j + n^k)$ 了。因为经过规约之後，不能保证问题的规模不扩大（规模还是 $n$ 吗？不一定！）。

假设最初给问题 $\Pi_1$ 的输入规模是 $n$。由于 $A$ 的时间复杂度是 $O(n^j)$，因此算法 $A$ 完成的输出（也就是规约之後 $\Pi_2$ 问题的输入）规模不会超过 $O(n^j)$。

> 不可能以少于 $O(n)$ 的代价生成 $n$ 规模的数据。

即，最坏情况下，算法 $B$ 的耗时是 $O((n^j)^k)$，即 $O(n^{jk})$。完毕。

### 10.19

#### Question

在第 7 章中已经证明背包问题可以在 $\Theta(nC)$ 时间内解决，这里 $n$ 是物品项数，$C$ 是背包容量。但是在这一章里提到，这是一个 NP 完全的问题。是否存在矛盾？请解释。

#### Answer

不矛盾。因为 $C$ 和问题的输入大小不成线性关系。实际上，问题的规模应该理解成其占用的比特数，即 $C = 2 ^ c$。即，这个问题仍然是 $O(n \times 2^c)$，即指数规模的。

### 10.22

#### Question

证明「NP = P」是「某个 NP 完全问题 $\Pi \in P$」的充分必要条件。

#### Answer

「NP = P」的充要条件是「P $\subseteq$ NP 且 NP $\subseteq$ P」。

根据 P 和 NP 的定义可知，P 天然地 $\subseteq$ NP。

> 既然都可以在多项式时间内求解，自然可以在多项式时间内验明结果的正确性。我直接把结果求出来不就是了？

可以作为恒为真的重言式。不必参与证明。

即，要证明「NP = P」等价于证明「NP $\subseteq$ P」。

即，原问题转变为证明「NP $\subseteq$ P」和「某个 NP 完全问题 $\Pi \in P$」的充要性。

先证明充分性。

如果「NP $\subseteq$ P」，即是说所有的 NP 问题都存在一个多项式时间的解。而根据定义，NP 完全问题是 NP 问题的一类。因此任意一个 NP 完全问题（包括 $\Pi$）都是属于 P 的。

> 充分性显然。

再证明必要性。

如果「某个 NP 完全问题 $\Pi \in P$」，那么根据 NP-C 问题的定义，任何 NP 问题都可以被多项式规约到这个问题 $\Pi$ 上。又根据 10.9 的结论，可知任何 NP 问题（当然也包括其中的任何 NP-C 问题）都可以在多项式时间内解出。

换言之，NP $\subseteq$ P。

因此，原命题成立。