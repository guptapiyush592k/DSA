def knapsack(W, val, wt):
        n = len(val)
    
        items = []
    
        for i in range(n):
            ratio = val[i] / wt[i]
            items.append((ratio, val[i], wt[i]))
    
        items.sort(reverse=True)
    
        total_value = 0.0
    
        for ratio, value, weight in items:
            if W >= weight:
                total_value += value
                W -= weight
            else:
                total_value += ratio * W
                break
    
        return total_value