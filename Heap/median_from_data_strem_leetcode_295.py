from heapq import *


class MedianFinder:

    def __init__(self):
        self.max_heap_for_small = []
        self.min_heap_for_large = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap_for_small) == 0 or self.max_heap_for_small[0] > num:
            heappush(self.max_heap_for_small, -num)

        elif self.max_heap_for_small[0] <= num:
            heappush(self.min_heap_for_large, num)

        if len(self.max_heap_for_small) > len(self.min_heap_for_large) + 1:
            heappush(self.min_heap_for_large, -(heappop(self.max_heap_for_small)))

        if len(self.min_heap_for_large) > len(self.max_heap_for_small):
            heappush(self.max_heap_for_small, -(heappop(self.min_heap_for_large)))

    def findMedian(self) -> float:
        if len(self.max_heap_for_small) == len(self.min_heap_for_large):
            return (-(self.max_heap_for_small[0]) + self.min_heap_for_large[0]) / 2

        else:
            return -(self.max_heap_for_small[0])


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(6)
    print(obj.findMedian())

    obj.addNum(10)
    print(obj.findMedian())

    obj.addNum(2)
    print(obj.findMedian())

    obj.addNum(6)
    print(obj.findMedian())

    obj.addNum(5)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
