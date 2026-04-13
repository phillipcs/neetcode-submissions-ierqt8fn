class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': # find delimeter
                j += 1
            length = int(s[i:j])
            i = j + 1 # start of string
            j = i + length # end of string
            res.append(s[i:j])
            i = j
        return res