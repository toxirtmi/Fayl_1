# n=int(input("Istalgan sonni kiriting = "))
# for i in range(1,n+1):
#     if i%3==0 and i%5==0 : print("Fin Tech")
#     if i%3==0 :print("Fin")
#     if i%5==0 :print("Tech")

# list=[]
# for i in range(0,77):
#     list.append(1)
# print(list)
# list=[]
# list1=[]
# for i in range(7):
#     for j in range(7):
#         list.append(1)
#     list1.append(list)
# print(list1)

list=[]
list1=[]
for i in range(1,4):
    if i==1 :
        for j in range(1,4):
            list.append(j)
        list1.append(list)
        list=[]
    if i==2 :
        for j in range(4,7):
            list.append(j)
        list1.append(list)
        list=[]
    if i==3 :
        for j in range(7,10):
            list.append(j)
        list1.append(list)
        list=[]
print(list1)