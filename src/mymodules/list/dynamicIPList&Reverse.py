#Dynamic input to list and list reverse using for loop with slicing
def lstreversedynamic():
 lst=list()
 List_lenght=int(input("Enter the length of the list: "))
 for i in range(List_lenght):
     item=int(input("Enter the list items"))
     lst.append(item)
     if i == 3:
         break
 print(lst)
 for num in lst[::-1]:
    print(num)
lstreversedynamic()