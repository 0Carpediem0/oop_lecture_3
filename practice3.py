from decimal import Decimal


class Product:
    def __init__(self, name, price, in_stock, category):
        self.name = name
        self.price = Decimal(str(price))
        self.in_stock = in_stock
        self.category = category

    def add_stock(self, quantity):
        self.in_stock += quantity

    def remove_stock(self, quantity):
        if 0 < quantity <= self.in_stock:
            self.in_stock -= quantity
        else:
            raise ValueError("Недостаточно товара на складе")


class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total(self, discount=0.0, tax=0.22):
        total = self.product.price * self.quantity
        total *= 1 - Decimal(str(discount))
        total *= 1 + Decimal(str(tax))
        return round(total, 2)

    def order_product(self):
        if 0 < self.quantity <= self.product.in_stock:
            self.product.remove_stock(self.quantity)
            return True
        return False


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def place_order(self, product, quantity):
        order = Order(product, quantity)
        if order.order_product():
            self.orders.append(order)
            return f'Заказ на {quantity} шт. товара "{product.name}" оформлен.'
        return 'Недостаточно товара на складе'


class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        if quantity <= 0:
            return 'Количество должно быть положительным'
        for item in self.items:
            if item.product is product:
                if item.quantity + quantity > product.in_stock:
                    return 'Недостаточно товара на складе'
                item.quantity += quantity
                return f'Количество товара "{product.name}" обновлено.'
        if quantity > product.in_stock:
            return 'Недостаточно товара на складе'
        self.items.append(Order(product, quantity))
        return f'Товар "{product.name}" добавлен в корзину.'

    def remove_item(self, product):
        for item in self.items:
            if item.product is product:
                self.items.remove(item)
                return f'Товар "{product.name}" удалён из корзины.'
        return 'Товар не найден в корзине'

    def update_quantity(self, product, quantity):
        for item in self.items:
            if item.product is product:
                if quantity <= 0:
                    return self.remove_item(product)
                if quantity > product.in_stock:
                    return 'Недостаточно товара на складе'
                item.quantity = quantity
                return 'Количество обновлено'
        return 'Товар не найден в корзине'

    def calculate_total(self, discount=0.0, tax=0.22):
        total = Decimal('0.00')
        for item in self.items:
            total += item.calculate_total(discount, tax)
        return round(total, 2)

    def checkout(self):
        if not self.items:
            return 'Корзина пуста'
        if any(item.quantity > item.product.in_stock for item in self.items):
            return 'Недостаточно товара на складе'
        for item in self.items:
            item.order_product()
            self.customer.orders.append(item)
        self.items.clear()
        return 'Заказ оформлен успешно'
