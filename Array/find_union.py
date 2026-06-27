def findUnion(a, b):
    seen = set()
    result = []

    for num in a:
        if num not in seen:
            seen.add(num)
            result.append(num)

    for num in b:
        if num not in seen:
            seen.add(num)
            result.append(num)

    print(result) 

findUnion([1,2,6,3,4,8], [2,4,6,55,7,3,9,11])