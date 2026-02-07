#Pair sum counter
list1=list(map(int, input().split()))
k=int(input())
count=0
n=len(list1)
for i in range(n):
  for j in range(i+1,n):
    if list1[i]+list1[j]==k and i<j:
      count+=1
print(count)