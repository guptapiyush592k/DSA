def maxSubarraySum(arr):
    max= float('-inf')
    sum = 0
    for num in arr:
        if(num > sum + num):
            sum = num
        else:
            sum += num
            
        if(sum > max):
            max= sum
    return max

print(maxSubarraySum([2,3,-8,7,-1,2,3]))