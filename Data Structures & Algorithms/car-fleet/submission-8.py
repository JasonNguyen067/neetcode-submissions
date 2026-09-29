class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = sorted(zip(position, speed), reverse=True)
        fleetstack = []

        for pos, spd in fleet:
            time = (target - pos) / spd 
            fleetstack.append(time)

            if len(fleetstack) >= 2 and fleetstack[-2] >= fleetstack[-1]:
                fleetstack.pop()

        return len(fleetstack)