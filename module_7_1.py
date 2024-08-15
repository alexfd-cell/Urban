
class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products():
        file = open(Shop.__file_name, 'r')
        pProd = file.read()
        file.close()
        return pProd

    def add(*products):
        Shop.products = products
        print(products)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# print(p2) # __str__
print(Shop.get_products())
Shop.add()
