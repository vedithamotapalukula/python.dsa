def selectionsort(a):
   for i in range(len(a)):
     min=a[i]
     for j in range(i+1,len(a)):
       if a[j]<min:
          min=a[j]
          a[i],a[j]=a[j],a[i]
     return a




a=[5,4,3,2,1]
print(selectionsort(a))

def bubblesort(a):
  for i in range(len(a)):
    min=a[i]
    for j  in range(i+1,len(a)):
       if a[j]<min:
         min=a[j]
         a[i],a[j]=a[j],a[i]
       else:
         a[i]<=a[j]
  return a
a=[9,7,6,5,2,16]
print(bubblesort(a))