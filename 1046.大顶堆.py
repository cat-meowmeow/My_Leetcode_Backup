class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]  #用负值将大顶堆转为小顶堆
        heapq.heapify(heap)   #将堆 小顶堆化

        while len(heap) > 1:
            x = heapq.heappop(heap)  #取出堆顶最小值
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,x-y)  # 将remain入堆 0就不写了
        if heap: return -heap[0]  #堆顶值
        return 0    #全是0很好直接0


#普通写法
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            remain = x - y
            stones.append(remain)
        return stones[0]
