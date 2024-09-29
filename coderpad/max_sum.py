
def maxSum(nums,k):

    if len(nums) == 0 or k == 0:
        return 0
    max_sum = 0
    for n in range(len(nums)):
        curr_sum = sum(nums[n:n+k])
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    print(maxSum([-5,1,2,3,-4,5,2], 2))