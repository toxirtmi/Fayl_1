# f1=1
# f2=1
# k=[1,1]
# for i in range(2,100):
#     z=k[i-1]+k[i-2]
#     if z>100: break
#     k.append(z)
# print(k)

# s="123salomiu56"
# k=0
# z=0
# n=len(s)
# for i in s:
#     if i.isdigit():
#         k+=1
#     else: z+=1
# print(k , " ta son", z," ta harf")

# s="python@mairu"
# n=len(s)
# k=0
# tek=":?.,>#$%^&*()!%<@"
# tt=0

# for i in tek:
#     if s[0]==i: 
#         print("Xato") 
#         tt=1
#     elif s[n-1]==i: 
#         print("Xato") 
#         tt=1
# if tt==0:
#     for j in s:
#         if j=="@": k+=1
#         elif j==".":k+=1
# if k==2: 
#     print("to`g`ri")

# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"X",j,"=", i*j)

# s="dasturlashahshshgdcbxcbjdcjbd"
# k=""
# n=1
# for i in s:
#     if n%2==1:
#         k=k+i
#         n+=1
#     else: 
#         k=k+i.upper()
#         n+=1
# print(k) 

# n=6
# k=1
# for i in range(1,n):
#     k=i*k
# print(k)

# s="ugftdf"
# k=0
# n=1
# z=""
# for i in range(len(s)):
#     k=s.count(s[i])
#     if k>=n:
#         n=k
#         z=s[i]
# print(z, " harfi ", n ,"martta") 

# s="asgguikghgggggggsalom"
# ss=set(s)
# print(ss)

s="1Assaloms@"
harf="QWERTYUIOPLKJHGFDSAZXCVBNM"
son="0123456789"
belgi="@#$"
h=0
s1=0
b=0
for i in s:
    for j in harf:
        if i==j: h+=1
    for k in son:
        if i==k: s1+=1
    for z in belgi:
        if i==z: b+=1
if b and s1 and h :
    print("tug`ri")
else: print("noto`gri") 




