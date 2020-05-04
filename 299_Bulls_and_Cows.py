class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = {}
        g = {}
        bull = 0
        for i in range(len(guess)) :
            if secret[i] == guess[i] :
                bull += 1 
            else :
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
        cow = 0
        for key in g :
            if key in s :
                cow += min(g[key], s[key])
        return str(bull) + 'A' + str(cow) + 'B'