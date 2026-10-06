def linearsearch(ar,target):
  for i in range(len(ar)):
    if ar[i]==target:
      print(f'{target} is found at index {i}')
      return
  print('not found')
  return  -1

a=[23,12,22,45,7,8]
print(linearsearch(a,5))

#Binarysearch

def binarysearch(a,target):
  l=0 
  r=len(a)-1
  m=l+r//2
  while l<r:
    if a[m]==target:
      print(f'{target} is found at index {m}')
      return
    elif a[m]<target:
      l=m
      m=(l+r)//2
    else:
      r=m
      m=(l+r)//2

b=[12,33,45,34,16,17]   
binarysearch(b,17)