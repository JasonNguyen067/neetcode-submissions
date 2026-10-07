class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        one = 1
        two = 1

        # Think of 226 test case 

        # Iteration one 22 2 != 0 curr += two ( 0 + 1 = 1)
        # 22 inbounds 1 + one = 2

        # one = 1
        # two = 2
        
        # cuz two has 2 possible ways
        # then 26 has one possibly way + the 2 before hand is 1 
        # so 2 + 1 = 3 

        for i in range(1, len(s)):
            curr = 0

            if s[i] != "0":
                curr += two
            
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                curr += one

            one = two
            two = curr

        return two 

        # TIme complexity is O(N
        # Space complexity i sO(1)