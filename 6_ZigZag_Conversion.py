class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index = []
        for i in range(numRows) :
            index.append(i)
        if len(index) > 2 :
            for i in index[1 : -1][::-1] :
                index.append(i)
        zigzag = [[] for x in range(numRows)]
        num = len(index) 
        for i in range(len(s)) :
            zigzag[index[i % num]].append(s[i])
        res = ""
        for row in zigzag :
            res += "".join(row)
        return res