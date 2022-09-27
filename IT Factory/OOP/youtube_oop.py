import csv


class Item:
    pay_rate = 0.80  # The pay rate after 20% discount
    all = []
    def __init__(self, name, price, quantity=0):
        # Run validation for the received arguments
        assert price >= 0, f"Price{price} must be greater or equal with zero."
        assert quantity >= 0, f"Quantity{quantity} must be greater or equal with zero."

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    # Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        # asa chemam un atribut al Clasei Item.pay_rate
        # putem folosi self.pay_rate pentru a putea modifica mai tarziu discountul unui item
    # decorators
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            # codul va lua datele din csv si-l va face dict
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # for i.e. 5.0, 10.0
        if isinstance(num, float):
            #  Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}' , {self.price}, {self.quantity})"


print(Item.is_integer(7.0))

# print(Item.all) # print o lista cu toate instantele introduse (item1-item5
# for instance in Item.all:
#     print(instance.name) # printeza nnumele instantelor introduse




# print(Item.__dict__) # all the attributes for Class level
# print(item1.__dict__) #  all the attributes for instance level

# item1.apply_discount()
# item2.pay_rate = 0.7 # am modificat discountul itemului 2 de la 20 la 30
# item2.apply_discount()
# print(item1.price) # pentru item1 se va luat valoarea pay_rate din Clasa adica 0.8
# print(item2.price)
