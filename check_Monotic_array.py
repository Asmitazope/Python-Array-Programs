# 1

def isMonotic(a):
    x,y=[],[]
    x.extend(a)
    y.extend(a)
    x.sort(reverse=True)

    if(x==a or y==a):
        return True
    return False

a=[6,5,4,4]

print(isMonotic(a))
print('\r')

