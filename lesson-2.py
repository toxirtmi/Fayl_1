# b2 = 0
# b3 = 0
# b5 = 0
# for i in range(10):
#     if i%2 == 0:
#         b2 +=1
#     if i%3 == 0:
#         b3 += 1
#     if i % 5 == 0:
#         b5 +=1
# print(b2, b3, b5)


# faktorial
# a = 1
# n = 1
# while n < 1000:
#     # n = a * n
#     n *= a
#     a += 1
#     print(n)
#     print(a)

# a = "20 21 22"
# a, b, c = a.split()
# print(a, b, c)

# list = list(range(1, 10))
# lyuboy_nom = [1,2 , 3]
# list.append(55)
# list.append(75)
# list.append("5dee5")

# print(list[5:-1])


# for i in list:
#     print(i)

# list2d = [
#     [1,2,3],
#     [4,5,6]
# ]
# print(list2d[1][2])


a = input("sonlar kiriting")
list = a.split()
print(a)
print(list)
a = 0
for i in int(list):
    a +=i
print(a)