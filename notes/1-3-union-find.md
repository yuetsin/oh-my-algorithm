# Lecture 3

> 今日话题：并查集（Union − Find Set）。

## 并查集

### 接口

```cpp
#include <vector>

template <class T>
class union_find_sets
{
public:
    union_find_sets(const std::vector<T> &init_values);
    T &ufs_union(const T &lhs, const T &rhs);
    T &ufs_find(const T &value);
}
```

初始情况下，提供一系列元素；默认他们各自属于独立的集合中，而且这个集合的名字就是初始元素的名字。

只有两个对外可见的方法：

* `Union`，将两个元素所在的并查集合并为一个。
* `Find`，提供一个元素，返回该元素所在的那个集合名称。

> 这个 `union_find_sets` 包含的是**并查集**的集合。

### 简化假设

* 初始并查集集合的元素都是数字，而且依次为 `0` 到 `n - 1`。
* 每个并查集的名字都设定为其中一个元素（`int` 类型）的值。

这样，我们提供一个更加简化的接口：

```python
class UnionFindSets:
    def __init__(self, n: int):
        # do init work
        pass

    def union(self, lhs: int, rhs: int) -> int:
        # do union work
        pass

    def find(self, elem: int) -> int:
        # do find work
        pass
```

### 实现

#### 笨蛋实现

我们可以真的用 `set` 来保存并查集，虽然想想都知道这个实现肯定很慢。

```python
#!/usr/bin/env python3


class UnionFindSets:

    def __init__(self, n: int):
        self.sets = {}
        for i in range(n):
            self.sets.append({i: set(i)})

    def union(self, lhs: int, rhs: int) -> int:
        lhs_set_index = self.find(lhs)
        rhs_set_index = self.find(rhs)

        if lhs_set_index is None or rhs_set_index is None:
            return None

        lhs_set = self.sets[lhs_set_index]
        rhs_set = self.sets[rhs_set_index]

        del self.sets[lhs_set_index]
        del self.sets[rhs_set_index]

        self.sets.update({
            # always use left set name
            lhs_set_index: lhs_set.union(rhs_set)
        })

        return lhs_set_index

    def find(self, elem: int) -> int:
        for k, v in sets:
            if elem in v:
                return k

        return None
```

![image-20200725200327171](1-3-union-find.assets/image-20200725200327171.png)

可以得到正确的结果。

#### 优化实现

我们好像没有必要真的维护 `set` 类型的集合，事实上，鉴于我们的 `id` 始终是 `0` 到 `n - 1` 的数字，因此实际上我们只需要用 `n` 长度的一个数组就能记录 UFS 的状况了。

> 数组的第 `i` 个元素的值代表名为 `i` 的元素所在并查集的名称。

> 初始情况下，`payload` 数组应该记录为 `list(range(n))`，也就是 `[0, 1, 2, ..., n - 1]` 这样的。

这样，`find(i)` 就可以简单地实现为返回 `payload_array[i]` 的值了。

> 时间复杂度是 $O(1)$ 级别的。

而 `merge(m, n)` 可以实现为对每一个满足 `payload_array[k] = n` 的 `k`，将 `payload_array[k] = m`。

> 时间复杂度是 $O(n)$ 级别的。

![image-20200727205826646](1-3-union-find.assets/image-20200727205826646.png)

#### 更优化实现

能否实现得更好呢？我们来试着用「树」的概念来优化一下算法。

将每个集合元素想象为一个树中的节点，属于不同集合的元素对应的节点位于不同的树中，而且每个集合的名字就是该树的根节点对应元素名字。

![image-20200727210652214](1-3-union-find.assets/image-20200727210652214.png)

例如，这棵树就表示一个名为「9」的集合，其中包含了 `[9, 6, 4, 11, 7, 28, 16]` 这些元素。

事实上，要表示这棵二叉树也只需要 `n` 个元素的数组就够了。我们规定：节点 `i` 所索引的数组 `payload_array[i]` 代表其父节点的名字；将根节点的 `payload_array[root]` 设定为一个特殊值（在这里，我们将其设定为 `-size`，即这棵树的节点数量的相反数。）。

![image-20200727211056318](1-3-union-find.assets/image-20200727211056318.png)

