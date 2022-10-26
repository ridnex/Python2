class Product():
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, n):
        if n<10:
            return self.price
        elif n<100:
            return self.price*0.9
        else:
            return self.price*0.8
    
    def get_name(self):
        return self.name
        
    def make_purchase(self, m):
        if m<=self.amount:
            self.amount = self.amount - m
            return self.get_price(m)*m
        else:
            return 0
            

apple = Product('apple', 20, 400 )
banana = Product('banana', 50, 700)
tomato = Product('tomato', 40, 350)
carrot = Product('carrot', 40, 200)
arr = [apple, banana, tomato, carrot]

output = []
total = 0
for i in arr:
    names = i.get_name()
    print(names)
    b = int(input(" amount: "))
    price = i.get_price(int(b))
    all_price = i.make_purchase(int(b))
    str = f'{names}, {b}kg for {price} all {all_price}'
    total += all_price
    output.append(str)
output.append(total)
for i in output:
    print(i)
    
