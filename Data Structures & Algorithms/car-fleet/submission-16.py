class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We want to sort position from highest to lowest, the reason for this being due to the fact
        # that for position based things we want to be able to keep track of which one arrives first
        # This is so we can track the lowest amount of time as it goes up and can track any 
        # convoys in between that, so we will sort in reverse from highest to low, 
        # and also zip the positions with their respective speeds

        sortedPairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleet = []

        for pos, spd in sortedPairs:
            timeExpected = (target - pos) / spd # yo to divide by spd this is decimal based right and int brings 
            # closer to 0 while floor divison just brings both positive rounded down but also negative is also rounded down aswell 
            # like -3.3 is -4

            fleet.append(timeExpected)

            while len(fleet) >= 2 and fleet[-1] <= fleet[-2]: 
                fleet.pop()

        return len(fleet)


            #because think 2 3 5 all separate fleets but 2 1 pop 1 
            # cuz thats a fleet

        # Time complexity is O(NLOGN) for timsort
        # Space compelxity is O(N) worst case N for n times expected all are fleets appended and stored