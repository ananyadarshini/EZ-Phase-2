arr=[56,32,73,43,36,67,89]
for i in range(1,len(arr)):
    j=1
    while arr[j-1]>arr[j] and j>0:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=i
print(arr)
