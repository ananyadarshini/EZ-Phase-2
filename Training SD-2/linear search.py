"""n=int(input("enter size of array:"))
for i in range(0,n):
    x=int(input("enter the elements:"))
s=int(input("enter search element:"))
for i in range(0,n):
    c=0
    if s==i:
        c=1
        break
if c==1:
    print("search element found:",s)
else:
    print("search element not found")"""

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
numbers=[5,9,2,7,1,8,3]
target=1
index=linear_search(numbers,target)
print(f"target found at index:{index}")
