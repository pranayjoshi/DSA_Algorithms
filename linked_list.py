from itertools import count


class Node:
    def __init__(this, data=None, next=None) -> None:
        this.data = data
        this.next = next

class LinkedList:
    def __init__(this):
        this.head = None

    def insertInBeginning(this, data=None):
        node = Node(data, this.head)
        this.head = node

    def Printer(this):
        itr = this.head
        lList = ""
        while itr:
            lList += str(itr.data)+"--->"
            itr = itr.next
        print(lList)
    def insertinEnding(this, data=None):
        if this.head == None:
            this.head = Node(data, this.head)
            return
        itr = this.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    def insertValues(this, dataList):
        this.head = None
        for i in dataList:
            this.insertinEnding(i)
    
    def length(this):
        itr = this.head
        count=0
        while itr:
            count +=1
            itr = itr.next
        return count
    def removeAt(this, index):
        if index <0 or index >= this.length():
            return("Invalid index")
        if index == 0:
            this.head = this.head.next
            return
        count = 0
        itr = this.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
            print(itr)
    def insertAt(this, index, data):
        if index <0 or index >= this.length():
            return("Invalid index")
        count = 0
        itr = this.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
            count+=1
            itr = itr.next

L = LinkedList()
L.insertInBeginning(82)
L.insertInBeginning(72)
L.insertInBeginning(272)
L.insertinEnding(24)
L.insertValues([10, 20, 30])
L.removeAt(1)
L.insertAt(1,234)
L.Printer()
