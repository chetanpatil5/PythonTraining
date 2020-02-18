n=int(input("Enter the no of  elements in the list : "))
list1=[]

for i in range(0,n):
    ele=int(input("Enter the  elements in the list : "))
    list1.append(ele)

list1.sort()
print("Sorted list is: ",list1)
