#Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64 Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
"""
#insert elemnts into the list
list1=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    list1.append(e)
"""
print("\n Positive numbers in",list1,"are: ")

for i in list1:   
    if i >= 0:
       print(i, end = " ")
       
print("\n Positive numbers in",list2,"are: ")

for i in list2:   
    if i >= 0:
       print(i, end = " ")
