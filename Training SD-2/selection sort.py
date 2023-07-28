n=int(input("enter length of array:"))
print("enter array elements:")
li=[]
for i in range (n):
    num=int(input())
    li.append(num)

for  i in range(n):
    min=i
    for j in range(i+1,n):
       if li[min]>li[j]:
            min=j
    li[i],li[min]=li[min],li[i]
print("sorted array is",li)
