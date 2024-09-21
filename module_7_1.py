class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        try:
            with open(self.__file_name, 'r') as file:
                products = file.readlines()
                file.close()
                return ''.join(product.strip() + '\n' for product in products)
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products: Product):
        existing_products = set()

        try:
            with open(self.__file_name, 'r') as file:
                existing_products = {line.split(', ')[0] for line in file}
                file.close()
        except FileNotFoundError:
            pass

        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
                    file.close()
                print(f'Продукт {product.name} добавлен в магазин')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
