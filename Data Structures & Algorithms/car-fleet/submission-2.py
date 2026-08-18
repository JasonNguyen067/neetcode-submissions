class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = sorted(zip(position, speed), reverse=True)
        stack = []

        for position, speeds in fleet:
            time = (target - position) / speeds
            stack.append(time)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)