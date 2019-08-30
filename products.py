import os
products = []
if os.path.isfile('products.csv'):
	print('yes, there is a csv file')
	with open('products.csv','r', encoding='utf-8') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('there is NO such file')


while True:
	name = input('please insert name')
	if name == 'q':
		break
	price = input('please insert price')
	price = int(price)
	products.append([name,price])
print(products)
for p in products:
	print('the price of',p[0],'is',p[1])

with open('products.csv','w',encoding='utf-8') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0]+','+str(p[1])+'\n')