#second largest 
list1=list(map(int, input().split()))
larg=0
sec_larg=0

for i in list1:
  if i>larg:
    sec_larg=larg
    larg=i
  elif i>sec_larg and i!=larg:
    sec_larg=i
print(sec_larg)