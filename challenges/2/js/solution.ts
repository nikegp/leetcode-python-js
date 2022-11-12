import { expect, ListNode, ListNodes } from "../../util";

const f = (l1: ListNode | null, l2: ListNode | null) => {
  let cumulative = 0;
  const dummyHead = new ListNode();
  let current = dummyHead;
  while (l1 || l2 || cumulative) {
    const value1 = l1 ? l1.val : 0;
    const value2 = l2 ? l2.val : 0;
    let total_value = value1 + value2 + cumulative;
    if (total_value >= 10) {
      total_value %= 10;
      cumulative = 1;
    } else {
      cumulative = 0;
    }

    const node = new ListNode(total_value);
    current.next = node;
    current = node;

    l1 = l1 ? l1.next : l1;
    l2 = l2 ? l2.next : l2;
  }

  return dummyHead.next;
};

expect(f(ListNodes([2, 4, 3]), ListNodes([5, 6, 4])), [7, 0, 8]);
expect(f(ListNodes([0]), ListNodes([0])), [0]);
expect(
  f(ListNodes([9, 9, 9, 9, 9, 9, 9]), ListNodes([9, 9, 9, 9])),
  [8, 9, 9, 9, 0, 0, 0, 1]
);
