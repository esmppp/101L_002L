import math

def total(l1):
    sum=0
    for i in l1:
        sum+=i
    return float(sum)
def average(l1):
    sum = 0
    counter = 0
    for i in l1:
        counter += 1
        sum += i
    if counter == 0:
        return math.nan
    return float(sum/counter)

def median(l1):
    l1 = sorted(l1)
    if len(l1) == 0:
        raise ValueError
    if len(l1)%2 == 1:
        return l1[len(l1)//2]
    else:
        midpoint = l1[len(l1)//2] + l1[len(l1)//2-1]
        return (midpoint/2)