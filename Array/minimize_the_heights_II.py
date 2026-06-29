def getMinDiff(arr, k):
        arr.sort()
        n = len(arr)

        ans = arr[-1] - arr[0]

        for i in range(1, n):

            smallest = min(arr[0] + k, arr[i] - k)
            largest = max(arr[i - 1] + k, arr[-1] - k)
            
            if smallest < 0:
                continue

            ans = min(ans, largest - smallest)

        return ans

print(getMinDiff([2,9,4,8,14,17,11],2))