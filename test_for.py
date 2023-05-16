"""import random


def rd(L):
    if len(L) == 1:
        print(L[0])
    else:
        import time
        seed = time.time() % (len(L)-1)
        c = L.pop(int(seed))
        print(c)
        rd(L)


L = [1, 2, 3, 4]
rd(L)"""

"""class Solution:
    def isPowerOfTwo(self, n: int):
        return n > 0 and self.lowbit(n) == n

    def lowbit(self, n):
        return n & -n

c=Solution.isPowerOfTwo(2)
print(c)
"""

"""
class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change(self):
        temp = self.a
        self.a = self.b
        self.b = temp


b = B('a', 'b')  # 创建一个含有两个篮子的对象
b.change()
print(b.a)
print(b.a)
"""


class Solution:
    def sortArray(self, nums):

        def maxHepify(arr, i, end):  # 大顶堆
            j = 2 * i  # j为i的左子节点【建堆时下标1表示堆顶】
            while j <= end:
                if j + 1 <= end and arr[j + 1] > arr[j]:  # i的左右子节点分别为j和j+1
                    j += 1  # 取两者之间的较大者

                if arr[i] < arr[j]:  # 若i指示的元素小于其子节点中的较大者
                    arr[i], arr[j] = arr[j], arr[i]  # 交换i和j的元素，并继续往下判断
                    i = j  # 往下走：i调整为其子节点j
                    j = 2 * i  # j调整为i的左子节点
                else:  # 否则，结束调整
                    break

        n = len(nums)
        nums = [0] + nums  # nums头部添加0，满足从下标1开始建堆

        # 建堆【大顶堆】
        for i in range(n // 2, 0, -1):  # 从第一个非叶子节点n//2开始依次往上进行建堆的调整【注意：此时堆顶为下标1】
            maxHepify(nums, i, n)

        # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
        for j in range(n, 0, -1):
            nums[1], nums[j] = nums[j], nums[1]  # nums[1]为堆顶元素（最大值），将其放置到尾部j
            maxHepify(nums, 1, j - 1)  # j-1变成尾部，并从堆顶1开始调整堆

        return nums[1:]

