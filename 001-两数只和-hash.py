class Solution:
    def twoSum(self,nums,target):
        hashtable=dict()
        for i,num in enumerate(nums):
            if target -num in hashtable:
                return [hashtable[target-num],i]
            hashtable[num]=i
        return []


s=Solution()

test_list=[1,2,3,4,5,6,7,8,9,11]

out=s.twoSum(test_list,20)

print(out)
