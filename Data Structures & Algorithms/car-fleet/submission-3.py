class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in fleet:
            time = (target - pos) / spd
            stack.append(time)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)