#!/usr/bin/env python


class Node:
    value: int
    left: Node
    right: Node

# assume it's a minimized heap


def heap_check(node: Node) -> bool:
    if node == None:
        return True

    if node.left != None and node.left.value > node.value:
        return False

    if node.right != None and node.right.value > node.value:
        return False

    return heap_check(node.left) and heap_check(node.right)
