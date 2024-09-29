import time
import math

# geek for geeeks finding missing number startegy
def missing_num_naive(arr, limit):
    temp_arr = [0] * (limit+1)
    for n in arr:
        temp_arr[n] += 1
    for m in range(1, limit+1):
        if temp_arr[m] == 0:
            return m
    return -1

# using the summation of first n numbers formula
def missing_num_sumn(arr, limit):
    max_sum = (limit*(limit+1)) // 2
    for n in arr:
        max_sum -= n
    return max_sum


if __name__ == '__main__':
    print(missing_num_naive([1, 2, 4, 6, 3, 7, 8],8))
    print(missing_num_sumn([1, 2, 4, 6, 3, 7, 8],8))