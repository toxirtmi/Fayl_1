# def kvadrat_tenglama(a,b,c):
#     d=b*b-4*a*c
#     if d<0 : 
#         print("echim yo`q")
#     elif d==0: 
#         x=(-b)/(2*a)
#         print("Echim bitta x=",x)
#     else: 
#         x1=(-b-(d**(1/2)))/(2*a)
#         x2=(-b+(d**(1/2)))/(2*a)
#         print("Tchim 2 ta X1 = ",x1,"  X2 = ",x2)
# kvadrat_tenglama(1,0,1)

# def daraja(a,n):
#     k=1
#     for i in range(1,n+1):
#         k=k*a
#     return round(k,2)
# a=float(input("Sonni kiriting ="))
# n=int(input("Darajani kirting = "))
# print(daraja(a,n))

#3
# def mane(a,b,c,d):
#     ab=(a+b)/2
#     ac=(a+c)/2
#     ad=(a+d)/2
#     ab1=(a**2+b**2)**(1/2)
#     ac1=(a**2+c**2)**(1/2)
#     ad1=(a**2+d**2)**(1/2)
#     return ab , ac ,ad,round(ab1,1),round(ac1,1),round(ad1,1) 
# print(mane(1,5,3,4))

#4
# def trengl(a,s,p):
#     s=(a*3**(1/2)*a)/(2*2)
#     p=3*a
#     return s,p
# u=1.2
# f=9.2
# u,f=trengl(3,u,f)
# print(u,f)

#5
# def rect(x1,y1,x2,y2):
#     a=abs(x2-x1)
#     b=abs(y2-y1)
#     s=a*b
#     p=2*(a+b)
#     return s,p
# s , p = rect(1,1,5,6)
# print(s,p)

# 6 Ixtiyoriy sonning raqamlari soni va yig`indisi`
# def digd(a):
#      n=len(str(a))
#      yi=0
#      for i in range(n):
#          yi=yi+a%10
#          a=a//10
#      return n,yi
# print(digd(0))

# 7 Ixtiyoriy sonning raqamlari teskarisi`
# def digd(a):
#      n=len(str(a))
#      yi=0
#      for i in range(1,n+1):
#          print(a%10)
#          yi=yi+(a%10)*10**(n-i)
#          a=a//10
#      return n,yi
# print(digd(123)) 

# #8
# def addright(son,raqam):
#     n=len(str(son))
#     k=raqam + 10*son
#     return k
# print(addright(1356363,6))

#9
# def addright(son,raqam):
#     n=len(str(son))
#     k=10**(n)*raqam + son
#     return k
# print(addright(-12,6))

#21
def samreng(a,b):
    if a>b:
        return 0
    k=0
    for i in range(a+1,b):
        k+=i
    return k
print(samreng(4,8))



# 23
# def chorak(x,y):
#     if (x==0)and(y==0):
#         return "Oxx nuqta"
#     elif (x>=0)and(y>=0):
#         return "Birinchi chorak"
#     elif (x<=0)and(y<=0):
#         return "Uchinchi chorak"
#     elif (x>=0)and(y<=0):
#         return "Turtinchi chorak"
#     elif (x<=0)and(y>=0):
#         return "ikkinchi chorak"
# print(chorak(1,-30))


#24
# def juft_toq(son):
#     if son%2==0:
#         return "son juft"
#     else: return "son toq"
# print(juft_toq(121))

#25
# def sonning_kvadrati(son):
#     son=son**(1/2)
#     if son%1==00 :
#         return True
#     else:return False
# print(sonning_kvadrati(36))

#26
# k=23
# def skre(son):
#     n=len(str(son))
#     for i in range(n*n+1):
#         if son==5**(i):
#             return True
#     return False
# print(skre(525))

