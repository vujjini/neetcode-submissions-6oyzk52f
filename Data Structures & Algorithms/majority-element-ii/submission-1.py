class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        majority = defaultdict(int)
        freq = defaultdict(int)
        res = []

        for num in nums:
            if num in majority:
                majority[num]+=1
            elif len(majority) < 2:
                majority[num]+=1
            else: #{3: 0, 1: 0}
                if len(majority) == 2: 
                    for curr_num in list(majority.keys()):
                        majority[curr_num]-=1
                        if majority[curr_num] == 0:
                            majority.pop(curr_num)
                else:
                    majority[num] = 1
        
        for curr_num in majority:
            for num in nums:
                if num == curr_num:
                    freq[curr_num]+=1
            if freq[curr_num] > len(nums) // 3:
                res.append(curr_num)
        
        return res
