class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #a car can only form a fleet with another car that is ahead of it
        #descending order
        cars = sorted(zip(position, speed), reverse = True)

        stack = []
        res = 0

        for p, s in cars:
            time = (target - p) / s
            if stack and time <= stack[-1]: #latter in faster
                continue                    #become a fleet->no push to stack
            
            stack.append(time)
            res += 1

        return res


