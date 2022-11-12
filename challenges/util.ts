// @ts-ignore
import { isEqual } from "lodash";

export const expect = (a: any, b: any) => {
  if (a && a?.constructor === ListNode) {
    a = listNodesToList(a);
  }
  if (isEqual(a, b)) {
    console.log(`PASSED ${a} === ${b}`);
  } else {
    console.log(`Mismatch! ${a} !== ${b}`);
  }
};

export class ListNode {
  val: any;
  next: ListNode | null;

  constructor(val = undefined, next = undefined) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

export const ListNodes = (values: any[]) => {
  const dummyHead = new ListNode();
  let current = dummyHead;
  for (const value of values) {
    const node = new ListNode(value);
    current.next = node;
    current = node;
  }

  return dummyHead.next;
};

const listNodesToList = (l: ListNode | null): any[] => {
  const result = [];
  while (l) {
    result.push(l.val);
    l = l.next;
  }
  return result;
};
