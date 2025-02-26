# 912. Sort an Array

# O(nlog n)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def max_heapify(heap_size, index):
            left,right = index * 2 + 1, index * 2 + 2
            largest = index

            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            if largest != index:
                nums[largest],nums[index] = nums[index], nums[largest]
                max_heapify(heap_size, largest)
        n = len(nums)
        print(nums)
        for i in range(n//2, -1, -1):
            max_heapify(n, i)

        for i in range(n-1,0,-1):
            nums[0],nums[i] = nums[i],nums[0]
            max_heapify(i,0)
        return nums


solution = Solution()
print(solution.sortArray(nums = [5,2,3,1]))