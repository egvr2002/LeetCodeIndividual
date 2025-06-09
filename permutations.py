class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
    
        permutations = []

        for i in range(len(nums)):
            element = nums[i]
            remaining = nums[:i] + nums[i+1:]

            sub_permutations = self.permute(remaining)

            for perm in sub_permutations:
                permutations.append([element] + perm)

        return permutations
