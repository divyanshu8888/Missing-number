print("-"*100)
print("This is code for finding missing number between 1 to 100")
print("-"*100)
print("\n")

def missing(list1):
    number=[]
    count=[0 for x in range(100)]
    for i in list1:
        count[i-1]+=1
    for i in range(len(count)):
        if count[i]>0:
            pass
        else:
            number.append(i+1)
    print("Missing number between 1 to 100 are: ", number)


list1=[1,2,4,5,6,7,8,10]
print("Current list by user is: ",list1,"\n")
missing(list1)
# while True:

#     a=int(input("Enter number: "))
#     print("\n")
#     list1.append(a)
#     print("Wants to enter more? Y/N or y/n: ")

#     a=input("Enter your choice: ")
#     if a.upper()=='Y':
#         continue
#     elif a.upper()=='N':
#         missing(list1)
#         break
#     else:
#         print('Type yes/no')
 
