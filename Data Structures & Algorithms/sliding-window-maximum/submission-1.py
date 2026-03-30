class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            # r - l + 1 == k -> window size correct
            # l = 0, 1, 2....
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output