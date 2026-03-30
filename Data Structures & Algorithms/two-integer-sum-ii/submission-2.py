class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = 0
        t = len(numbers) - 1

        while h < t:
            if numbers[h] + numbers[t] > target:
                t -= 1
            elif numbers[h] + numbers[t] < target:
                h += 1
            else:
                return [h + 1,t + 1]