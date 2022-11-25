a=[3,2,1,8,4]
for i in range(len(a)):
 for j in range (len(a)-i-1):
        print(j, end=' ')
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a) 



