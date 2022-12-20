# s="restartstar"
# b=s[:-2]+"$"+s[-1]
# print(b)

# a="abs"
# b="xyz"
# a1=a[0:2]+b[-1]
# b1=b[0:2]+a[-1]
# s=a1+" " +b1
# print(s)

# s=input("so`z kiriting")
# n=int(input("son kirit="))
# k=len(s)
# a=s[0:n-1]+s[n:k]
# print(a)

#4?
s="salom"
s1=" "
s2=" "
n=len(s)
"s1"=s[0]
s2=s[n-1]
ss=s.replace(s[n-1],s1[0])
ss[0]=s2[0]
print(ss)

#5
# n=float(input("son kiriting="))
# k=0
# if n>100000 :
#     k=n-n/10
#     print(k, "10 foiz skidka")
# elif (n>50000) and (n<100000) :
#     k=n-n/5
#     print(k, "5 foiz skidka")
# else: print(n,"Uzgarmagan narhda")

#6
# savol=int(input("Nechta savol="))
# k=int(input("Nechta echilgan="))
# n=float
# n=(k/savol)*100
# if n >= 60 :
#     print("Imtihonga kiritilsin")
# else: print("Imtihonga kiritilmasin")

# 10
# oylar=[31,28,31,30,31,30,31,31,30,31,30,31]
# oy=int(input("Oyni kiriting="))
# kun=int(input("Kunni kiriting="))
# nechanchi_kun=0
# for i in range(oy-1):
#     nechanchi_kun+=oylar[i]
# nechanchi_kun+=kun
# print(nechanchi_kun)

#11
# oylar=[31,28,31,30,31,30,31,31,30,31,30,31]
# haftalar=["du","se","chor","pay","juma","shan","yakshanba"]
# oy=int(input("Oyni kiriting="))
# kun=int(input("Kunni kiriting="))
# nechanchi_kun=0
# for i in range(oy-1):
#     nechanchi_kun+=oylar[i]
# nechanchi_kun+=kun
# hafta_kuni=nechanchi_kun%7
# print(haftalar[hafta_kuni-1])

#12
# sonlar=["bir","ikki","uch","turt","besh","olti","etti","sakkiz","tuqqiz"]
# ik_sonlar=["o`n","ygirma","uttiz","qirq","ellik","oltmish","yetmish","sakson","tuqson","yuz"]
# n=int(input("sonni kiriting= "))
# if n==0: 
#     print("Nol")
# if n==100 :
#     print("yuz")
# if (n>1)and(n<10) :
#     print(sonlar[n-1])
# if (n>=10)and(n<100):
#     k=n//10
#     z=n%10
#     ss=ik_sonlar[k-1]+" "+sonlar[z-1]
#     print(ss)

#13
# k=0
# for i in range(3):
#     k+=float(input("Sonni kiriting="))
# print(k/3)

#14?

#15
# oylar=[31,28,31,30,31,30,31,31,30,31,30,31]
# haftalar=["du","se","chor","pay","juma","shan","yakshanba"]

# kun=256
# oy=kun//30
# nechanchi_kun=0
# for i in range(oy-1):
#     nechanchi_kun+=oylar[i]
# nechanchi_kun+=kun
# hafta_kuni=nechanchi_kun%7
# print(haftalar[hafta_kuni-1])

#17?
# s=input("So`z kiriting = ")
# if s.() :
#     print("Katta harf bor")
# else:print("Katta harf yuq")
# print(s.lower())