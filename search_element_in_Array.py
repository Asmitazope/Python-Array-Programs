'''num=8
arr=[4,5,6,2,1]

for i in range(len(arr)):
    if arr[i]==num:
        print(i)
        break
else:
    print('-1')
print('\r')'''


# craete a function
def search(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    else:
        return -1

num=10
arr=[3,4,6,1,9]

ans=search(arr,num)
print(ans)