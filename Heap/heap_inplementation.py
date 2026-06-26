'''
Heap is a data structure that is build on top of array. it is usefull to reduce time complexity
  In Heap we can:
        Add in log(n) Time complexity
        Remove in log(n) Time complexity
        get highest priority element in o(1) time complexity

Heap need to satisfy two conditions:
    Imagine heap as a tree (just for reference)
    1. Heap Order Property(HOP): it says the parent element should be smallest then its child element and here we dont have any idea that which child is smaller
    2. Complte Binary Tree(CBT): it says tree should be full at height -1 level and we will only add data from left to right

heap_array = [10,20,30,40,35,45,42,55,30]
    relations:
        left child = 2*pi + 1  pi=parent index
        right child = 2*pi + 2 
        from child to parent = (ci-1)/2   ci=child index

Note: Priority queue is implemented using heap 

add: -> we always add at the end and then do upheapify
remove: -> we swap first with the last and then remove last and then downheapify
'''


class MinHeap:

    def __init__(self):
        self.heap = []

    def size(self):
       return len(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def add(self, value):
        self.heap.append(value)
        self._heapify_up()

    def remove(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        # Move last element to root
        self.heap[0] = self.heap.pop()

        self._heapify_down()

        return root

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] <= self.heap[index]:
                break

            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent],
            )
            index = parent

    def _heapify_down(self):
        index = 0

        while True:

            left = 2 * index + 1
            right = 2 * index + 2

            smallest = index

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )

            index = smallest


#Run
heap = MinHeap()
heap.add(10)
heap.add(12)
heap.add(2)
heap.add(6)
print(heap.heap)
heap.remove()
print(heap.heap)
heap.add(1)
print(heap.heap)