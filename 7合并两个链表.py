class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def initList(data):
    # 创建头结点
    head = ListNode(data[0])
    r = head
    p = head
    # 逐个为 data 内的数据创建结点, 建立链表
    for i in data[1:]:
        node = ListNode(i)
        p.next = node
        p = p.next

    return r


def printList(head):
    if head is None: return
    node = head
    while node is not None:
        print(node.data, end=' ')
        node = node.next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    new_head = ListNode(0)
    # 返回的节点
    cur = new_head
    while l1 and l2:
        if l1.data < l2.data:
            new_head.next = l1
            new_head = new_head.next
            l1 = l1.next
        else:
            new_head.next = l2
            new_head = new_head.next
            l2 = l2.next
    # 如果l1、l2不等长度，那么在new_head后面接入较长的还剩下的链表头结点
    if l1 or l2:
        new_head.next = l1 or l2

    return cur.next


if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [2, 4, 6]
    l1 = initList(data1)
    l2 = initList(data2)
    printList(l1)
    print('\r')
    printList(l2)
    print("\r\n合并：")
    printList(mergeTwoLists(l1, l2))
