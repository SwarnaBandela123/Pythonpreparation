def reverlist():
 Numbers=[1,2,3,4,5]
 #Using slicing
 print(Numbers[::-1])

#Using while loop
 i, j = 0, len(Numbers) - 1
 while i < j:
     Numbers[i], Numbers[j] = Numbers[j], Numbers[i]
     i += 1
     j -= 1
 print(Numbers)

reverlist()