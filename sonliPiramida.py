for i in range(0,9):
	if i==0:
		print('  '+' '*9+str(i))
	else:print('  '+' '*(9-i)+str(i)*i+str(i)+str(i)*i)
for i in range(9,0,-1):
       print('  '+' '*(9-i)+str(i)*i+str(i)+str(i)*i)
print('  '+' '*9+str(0))