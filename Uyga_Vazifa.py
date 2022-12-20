#1
# n=11
# k=0
# for i in range(1,n+1):
#     if i%2==1:
#         k=k+i
#         print(k)

#2
# n=11
# k=0
# for i in range(1,n+1):
#     if (i%3 == 0)and(i%9 != 0):
#         k=k+i
# print(k)

#3
# n=5
# k=0
# for i in range(1,n+1):
#         k=k+i*i
#         print(k)

#4?
#5
# n=6
# k=0
# if n//100>=1:
#     k=100*(n%10)+10*((n%100)//10)+(n//100)
#     print(k)
# elif n//10>=1 :
#     k=10*(n%10)+(n//10)
#     print(k)
# else:
#     print(n)

#13
# son=3
# daraja=5
# son1=1
# for i in range(0,daraja):
#     son1=son1*son
# print(son1)

#19
k=0
for i in range(1,9):
    for j in range(i):
        k=k+j*10
    print(k) 