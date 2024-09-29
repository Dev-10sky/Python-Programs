import time
import math



# the naive approach is the use O(n^2) strategy
def max_subarr_sum_naive(arr):
    final_sum = arr[0]
    max_sum = 0
    for n in range(len(arr)):
        max_sum = 0
        for m in range(n,len(arr)):
            max_sum += arr[m]
            final_sum = max(final_sum, max_sum)
    return final_sum

# max subarray problem using kadane's algorithm
def max_subarr_sum_kadane(arr):
    max_end = arr[0]
    final_sum = arr[0]
    for f in range(1,len(arr)):
        if max_end >= 0:
            max_end += arr[f]
        else:
            max_end = arr[f]
        final_sum = max(final_sum, max_end)
    return final_sum




if __name__ == '__main__':
    arrOne = [2, 3, -8, 7, -1, 2, 3]
    print(max_subarr_sum_naive(arrOne))
    print(max_subarr_sum_kadane(arrOne))
