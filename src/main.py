class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        amount = 0
        remove_array = []
        for i in range(len(nums)):
            if nums[i] == val:
                remove_array.append(i)
            else:
                amount += 1
        for i in reversed(remove_array):
            nums.pop(i)
        return amount


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution.removeElement(nums, val))
