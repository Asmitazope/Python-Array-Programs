# 1
def sum_Arr(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return(sum)
arr=[12,3,4,15]

print('Sum of Array Elements is:', sum_Arr(arr))

# 2 using sum method

arr=[1,2,3,4]

ans=sum(arr)
print('Sum of array is:',ans)

#3 using reduce method

from functools import reduce
def sum_arr(arr):
    sum=reduce(lambda a,b:a+b,arr)
    return(sum)
arr=[1,2,3,4,5]

answ=sum_arr(arr)

print('Sum of Array :',answ)