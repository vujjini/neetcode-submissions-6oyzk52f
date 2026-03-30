class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix: Product of all the ele before each ele
        # suffix: vice - versa
        pre = []
        suff = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                pre.append(1)
            else:
                pre.append(pre[i - 1]*nums[i - 1])

        nums.reverse()
        for i in range(n):
            if i == 0:
                suff.append(1)
            else:
                suff.append(suff[i - 1]*nums[i - 1])
        suff = suff[::-1]
        # print(pre)
        # print(suff)

        res = [pre[i]*suff[i] for i in range(n)]

        return res

