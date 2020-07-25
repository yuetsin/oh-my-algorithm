#include <vector>

template <class T>
class union_find_sets
{
public:
    union_find_sets(const std::vector<T> &init_values);
    T &ufs_union(const T &lhs, const T &rhs);
    T &ufs_find(const T &value);
}