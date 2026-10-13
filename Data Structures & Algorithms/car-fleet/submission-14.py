class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # For this problem you are not able to have another car pass another even if it starts behind 
        # and catches up

        # We want to count the amount of different car fleets 

        fleet = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        result = []

        for pos, spd in fleet:
            timeNeeded = (target - pos) / spd
            result.append(timeNeeded)

            while len(result) >= 2 and result[-1] <= result[-2]:
                result.pop()

        
        return len(result)