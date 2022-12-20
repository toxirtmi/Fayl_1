# car={
#         "brend":"Shevrale",
#         "model":"neksiya",
#         "yil":2000,
#         "yil":2020 ,
#         "yil":2021}
# print(car.get("yil"))
currencies = {
    'Argentine Peso': 118362.205708,
    'Australian Dollar': 1586.232315,
    'Bahraini Dinar': 423.780164,
    'Botswana Pula': 13168.450636,
    'Brazilian Real': 5954.781483,
    'British Pound': 834.954104,
    'Bruneian Dollar': 1520.451015,
    'Bulgarian Lev': 1955.83,
    'Canadian Dollar': 1430.54405,
    'Chilean Peso': 898463.818465,
    'Chinese Yuan Renminbi': 7171.445692,
    'Colombian Peso': 4447741.922165,
    'Croatian Kuna': 7527.744707,
    'Czech Koruna': 24313.797041,
    'Danish Krone': 7440.613895,
    'Emirati Dirham': 4139.182587,
    'Hong Kong Dollar': 8786.255952,
    'Hungarian Forint': 355958.035747,
    'Icelandic Krona': 143603.932438,
    'Indian Rupee': 84241.767127,
    'Indonesian Rupiah': 16187150.010697,
    'Iranian Rial': 47534006.535121,
    'Israeli Shekel': 3569.191411,
    'Japanese Yen': 129149.364679,
    'Kazakhstani Tenge': 489292.515538,
    'Kuwaiti Dinar': 340.959682,
    'Libyan Dinar': 5196.539901,
    'Malaysian Ringgit': 4717.485104,
    'Mauritian Rupee': 49212.933037,
    'Mexican Peso': 23130.471272,
    'Nepalese Rupee': 134850.008728,
    'New Zealand Dollar': 1703.649473,
    'Norwegian Krone': 9953.078431,
    'Omani Rial': 433.360301,
    'Pakistani Rupee': 198900.635421,
    'Philippine Peso': 57574.278782,
    'Polish Zloty': 4579.273862,
    'Qatari Riyal': 4102.552652,
    'Romanian New Leu': 4946.638369,
    'Russian Ruble': 86197.012666,
    'Saudi Arabian Riyal': 4226.530892,
    'Singapore Dollar': 1520.451015,
    'South African Rand': 17159.831129,
    'South Korean Won': 1355490.097163,
    'Sri Lankan Rupee': 228245.645722,
    'Swedish Krona': 10439.125427,
    'Swiss Franc': 1037.792217,
    'Taiwan New Dollar': 31334.286611,
    'Thai Baht': 37436.518169,
    'Trinidadian Dollar': 7636.35428,
    'Turkish Lira': 15078.75981,
    'US Dollar': 1127.074905,
    'Venezuelan Bolivar': 511082584.868731
}
# b=input("davalatni kiriying = ")
# a=currencies.get(b, f"{b}  bunday qiymat yo`q")
# print(a)


# print(list(currencies.keys()))
# print(list(currencies.values()))

d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}

d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}
d1.update(d2)
print(d1)

# for i in range(1000):
#     if i==50 : 
#         print("tugadi")
#         break
# for i in range(1000):
#     if i%2 == 0:
#         continue
#     print(i)
# b=""
# r=""
# niklar={"neo":1,
# "neo1":1}
# k=1
# a=input("nik kiriting = ")
# for i in list(niklar.keys()):
#     if a==i: b=a

# for i in list(niklar.keys()):
#     if a == i:
#         k+=1
#     # a=a+f"{k}"    
# r=b+f"{k}"
# z={b:1}
# niklar.update(z)
# print(b, "ni mavjud" ,"sizning nikingiz",r)


#foydalanuvchilarni qushish 
# n=int(input("Nechta ism kiritasiz? = "))
# niklar={}

# for i in range(n):
#     yangi_ism=input("ismni kiriting=")
#     if yangi_ism not in niklar:
#         niklar[yangi_ism]="foydalanuvchi"
#         print(niklar)
#         continue
#     else:
#         for j in range(1,10):
#             if yangi_ism+f"{j}" not in niklar:
#                 niklar[yangi_ism+f"{j}"]="foydalanuvchi"
#                 print(niklar)
#                 break
            
# uzunligi 6 dan kattasini topish
words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
           'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
           'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
           'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
           'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
           'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
           'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
           'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
           'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']

#ch=0
# n=len(words)
# for i in range(n):
#     if len(words[i])>=6 :
#         ch+=1
#         print(ch ,"-", words[i])

# n=0
# for i in words:
#     n+=1
#     if len(i)>=6:
#         print(n," - ",i)

        
# harf=input("harfni kiriting= ")
# harf=harf.lower()
# suz=input("So'zni kiriting = ")
# list=suz.split()
# for i in list:
#     if harf in i.lower() :
#             print(i)


# print(list)

# n=int(input("sonni kiriting = "))
# k=int(input("Nechanchi darajaga ko`tarasiz = "))
# z=1
# for i in range(k):
#     z*=n
# print(z)

# n=int(input(""))