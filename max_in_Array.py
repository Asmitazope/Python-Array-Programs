# 1 maximum in array
def largest(arr,n):
    max=arr[0]

    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
        return max
arr=[10,22,9,6]
n=len(arr)
ans=largest(arr,n)

print('Maximum number in agiven array is:',ans)
print('\r')

#2 using 'max' method
def largest(arr,n):
    ans=max(arr)
    return ans

if __name__=='__main__':
    arr=[10,20,80,50]
    n=len(arr)
    print("Largest element in array:",largest(arr,n))
    print('\r')

#3 using sort method
def largest(arr,n):
    # sort the array
    arr.sort()

    # since array is sorted the last element of array is the largest
    return arr[n-1]
    # or return arr[-1]

arr=[9,3,8,6]
n=len(arr)
ans=largest(arr,n)
print('Sorted Array is:',arr)
print('\r')
print('Largest element in an array is:',ans)
print('\r')



#4 using reduce method
from functools import reduce
def largest(arr,n):
    ans=reduce(max,arr)
    return ans

arr=[10,324,45,90,9808]
n=len(arr)
ans=largest(arr,n)
print('Largest Element in Array is:',ans)