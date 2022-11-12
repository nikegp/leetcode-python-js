#!/usr/bin/env python
from typing import List, Optional

from challenges.utils import expect, list_nodes, ListNode


def f(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    cumulative = 0
    dummy_head = ListNode()
    current = dummy_head
    while l1 or l2 or cumulative:
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0
        total_value = value1 + value2 + cumulative
        if total_value >= 10:
            total_value %= 10
            cumulative = 1
        else:
            cumulative = 0

        node = ListNode(total_value)
        current.next = node
        current = node

        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2

    return dummy_head.next


if __name__ == "__main__":
    expect(f(list_nodes([2, 4, 3]), list_nodes([5, 6, 4])), [7, 0, 8])
    expect(f(list_nodes([0]), list_nodes([0])), [0])
    expect(
        f(list_nodes([9, 9, 9, 9, 9, 9, 9]), list_nodes([9, 9, 9, 9])),
        [8, 9, 9, 9, 0, 0, 0, 1],
    )
