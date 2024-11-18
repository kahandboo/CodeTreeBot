n = int(input())
mylist = list(map(int,input().split()))

for i in range(n):
    min = i
    for j in range(i+1,n):
        if mylist[min] > mylist[j]:
            min = j
    tmp = mylist[i]
    mylist[i] = mylist[min]
    mylist[min] = tmp
    

for i in mylist:
    print(i,end=' ')