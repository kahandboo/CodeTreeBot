n = int(input())
mylist = list(map(int,input().split()))

for i in range(1,n):
    j = i-1
    key = mylist[i]

    while j>=0 and mylist[j] > key:
        mylist[j+1] = mylist[j]
        j -= 1
    mylist[j+1] = key

for i in mylist:
    print(i, end=' ') 