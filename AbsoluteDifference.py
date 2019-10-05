# str=input()
# str=str.split(" ")
testcase=int(input())
ct='YES'
for i in range(testcase):
    n,d=input().split()
    n=int(n)
    d=int(d)
    ar=input()
    ar=ar.split(" ")
    for j in range(n-1):
        h=j+1
        lst=int(ar[h])
        fst=int(ar[j])+d
        if(lst>fst):
            ct='NO'
    print(ct)
            
