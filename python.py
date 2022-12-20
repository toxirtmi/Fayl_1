a=1
b=5
c=4
#print( " Kvadrat tenglamada a b va c ni kiriting" )
if (b*b-4*a*c)<0 : print("Tenglamani echimi yo`q")
elif (b*b-4*a*c)==0 : print(-2*b/(2*a))
elif (b*b-4*a*c)>0 : 
    print("x1=", (-b+(b*b-4*a*c)**(0.5))/(2*a)) 
    print("x2=", (-b-(b*b-4*a*c)**(0.5))/(2*a))
 
#a="12 32 14 12 65"    
a=input("istalgancha sonlarni kiriting = ")
list=a.split()
n=len(list)
list1=[]
for i in range(0,n):
    list[i]=int(list[i])
#print(list)
#list1=list
k=0
#print(list1)
for i in range(0,n):
    for j in range(0,n-1):
        if list[j]<list[j+1] :
            k=list[j+1]
            list[j+1]=list[j]
            list[j]=k
print(list)

for i in range(0,n):
    for j in range(0,n-1):
        if list[j]>list[j+1] :
            k=list[j+1]
            list[j+1]=list[j]
            list[j]=k
print(list)


