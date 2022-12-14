// @ts-ignore
import { isEqual } from "lodash";

export const expect = (a: any, b: any) => {
  if (a && a?.constructor === ListNode) {
    a = listNodesToList(a);
  }

  const quoteA = typeof a === "string" || a instanceof String ? "'" : "";
  const quoteB = typeof b === "string" || b instanceof String ? "'" : "";

  if (isEqual(a, b)) {
    console.log(`PASSED ${quoteA}${a}${quoteA} === ${quoteB}${b}${quoteB}`);
  } else {
    console.log(`Mismatch! ${quoteA}${a}${quoteA} !== ${quoteB}${b}${quoteB}`);
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

export const zip = (arrays: any[][]): any[][] => {
  return arrays[0].map(function (_, i) {
    return arrays.map(function (array) {
      return array[i];
    });
  });
};
