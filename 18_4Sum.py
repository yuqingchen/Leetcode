class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sumdic = {}
        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)) :
                sum1 = nums[i] + nums[j]
                if sum1 not in sumdic :
                    sumdic[sum1] = [(i, j)]
                else :
                    sumdic[sum1].append((i, j))
        res = set()
        for key in sumdic.keys() :
            temp = target - key
            if temp in sumdic :
                for (i, j) in sumdic[key] :
                    for (k, l) in sumdic[temp] :
                        if i != k and i != l and j != k and j != l :
                            reslist = [nums[i], nums[j], nums[k], nums[l]]
                            reslist.sort()
                            res.add(tuple(reslist))
        result = []
        for e in res :
            result.append(list(e))
        return result