for i in range(0,9):
	if i==0:
		print('  '+' '*9+'*')
	else:print('  '+' '*(9-i)+'*'*i+'*'+'*'*i)
for i in range(9,0,-1):
       print('  '+' '*(9-i)+'*'*i+'*'+'*'*i)
print('  '+' '*9+'*')