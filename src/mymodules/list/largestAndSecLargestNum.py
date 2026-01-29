Numbers=[1,2,5,4,3]
Largest=Sec_largest=float('-inf')
for num in Numbers:
 if num > Largest:
  Sec_largest=Largest
  Largest=num
 elif num > Sec_largest and num!=Largest:
      Sec_largest=num

print(Largest)
print(Sec_largest)

#Another method
print(max(Numbers))
Numbers.remove(Max(Numbers))
print(max(Numbers))

#Using Reverse and slicing methods
Numbers.sort(reverse=True)
print(Numbers[:2])