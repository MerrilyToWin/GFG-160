arr = [1,2,1,2,1,3,4,5,1,2]

# testing program - Used in normal coding rounds

def maxi_find(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    max_freq = max(dic.values())
    result = [k for k, v in dic.items() if v == max_freq]
    result.sort()
    return result if len(result) > 1 else result[0]

print(maxi_find(arr))

# GFG code - Used in GFG platform

"""Boyer-Moore Voting Algorithms"""

n = len(arr)

ele1, ele2 = 0,0
count1, count2 = 0,0

for i in arr:
    if i == ele1:
        count1 += 1
    elif i == ele2:
        count2 += 1
    elif count1 == 0:
        ele1 = i
        count1 = 1
    elif count2 == 0:
        ele2 = i
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1
    
res = []
count1 , count2 = 0,0
for i in arr:
    if i == ele1:
        count1 += 1
    if i == ele2:
        count2 += 1

if count1 > n//3:
    res.append(ele1)

if count2 > n//3:
    res.append(ele2)

if len(res) == 2 and res[0] > res[1]:
    res[0], res[1] = res[1], res[0]

print(res)

