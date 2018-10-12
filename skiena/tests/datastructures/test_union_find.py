from datastructures import UnionFind


class Item:
        pass


def test_union_find():
    items = [Item() for i in range(8)]
    union_find = UnionFind(items)
    for i in range(7):
        for j in range(i+1, 8):
            assert union_find.find(items[i]) is not union_find.find(items[j])
    for i in range(4):
        union_find.union(items[2*i], items[2*i + 1])
    for i in range(7):
        for j in range(i+1, 8):
            if i // 2 == j // 2:
                assert union_find.find(items[i]) is union_find.find(items[j])
            else:
                assert union_find.find(items[i]) is not union_find.find(items[j])
    for i in range(2):
        union_find.union(items[4*i], items[4*i + 2])
    for i in range(7):
        for j in range(i+1, 8):
            if i // 4 == j // 4:
                assert union_find.find(items[i]) is union_find.find(items[j])
            else:
                assert union_find.find(items[i]) is not union_find.find(items[j])
    union_find.union(items[0], items[4])
    for i in range(7):
        for j in range(i+1, 8):
            assert union_find.find(items[i]) is union_find.find(items[j])


def test_union_find_different_group_sizes():
    items = [Item() for i in range(5)]
    union_find = UnionFind(items)
    union_find.union(items[0], items[1])
    union_find.union(items[2], items[3])
    union_find.union(items[2], items[4])
    assert union_find.find(items[0]) is union_find.find(items[1])
    assert union_find.find(items[3]) is union_find.find(items[4])
    assert union_find.find(items[0]) is not union_find.find(items[2])
    union_find.union(items[1], items[3])
    assert union_find.find(items[0]) is  union_find.find(items[2])


def test_union_find_on_same_group():
    items = [Item() for i in range(4)]
    union_find = UnionFind(items)
    for i in range(2):
        union_find.union(items[2*i], items[2*i + 1])
    union_find.union(items[0], items[2])
    union_find.union(items[1], items[3])
    for i in range(3):
        for j in range(i+1, 4):
            assert union_find.find(items[i]) is union_find.find(items[j])
