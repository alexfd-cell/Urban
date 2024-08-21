class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        pProd = file.read()
        file.close()
        return pProd

    def add(self, *products):
        self.products = products

        GetProduct = self.get_products()
        c, lst, addProd = 0, [], []
        if GetProduct != '\n':            addProd.append(GetProduct)
        lst.append(GetProduct[c:GetProduct.find(',', c)])
        for i in range(GetProduct.count('\n')):
            c = GetProduct.find('\n', c + 1)
            lst.append(GetProduct[c + 1:GetProduct.find(',', c)])

        for item in self.products:
            if lst.count(item.name):
                print(f'Продукт {item.name} уже есть в магазине')
            else:
                addProd.append(item.name + ', ' + str(item.weight) + ', ' + item.category)

        with open(Shop.__file_name, 'w') as file:
            for i in addProd:
                file.write(i + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Orange', 5.5, 'Fruits')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
