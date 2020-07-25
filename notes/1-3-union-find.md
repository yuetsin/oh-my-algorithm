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