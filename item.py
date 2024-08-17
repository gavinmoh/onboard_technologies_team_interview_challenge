class Item:

    def __init__(self, name):
        self.name = name
        self.quantities = []

    def add_quantity(self, quantity):
        self.quantities.append(quantity)

    def get_quantities(self):
        return self.quantities

    def count(self):
        return len(self.quantities)

    def get_min(self):
        return min(self.quantities)

    def get_max(self):
        return max(self.quantities)

    def get_sum(self):
        return sum(self.quantities)

    def get_avg(self):
        return self.get_sum() / self.count()

    def get_median(self):
        n = self.count()
        quantities = sorted(self.quantities)
        mid = n // 2
        return (quantities[mid-1] + quantities[mid]) / 2 if n % 2 == 0 else quantities[mid]

    def get_quantities_between(self, low, high):
        return [quantity for quantity in self.quantities if quantity > low and quantity <= high]
