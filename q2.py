#frequency of one only print
list1=list(map(int, input().split()))
sort=[]
for i in range(len(list1)):
  count=0
  for j in range(len(list1)):
    if list1[i]==list1[j]:
      count+=1
  if count==1:
    sort.append(list1[i])

print(sort)

