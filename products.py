products = []
while True:
	name = input('please insert name')
	if name == 'q':
		break
	price = input('please insert price')
	products.append([name,price])
print(products)