class Product ():
    def __init__(self,name,price) :
        self.name = name
        self.price = price

class Market ():
    def __init__(self,name) :
        self.name = name
        self.goods = []
        self.capital = 0

    def add_goods(self,product):
        self.goods.append(product)
        self.capital = self.capital + product.price

    def __str__(self) :
        return f"The market name {self.name} , with capital {self.capital} $"

    def __repr__(self):
        return f"Name : {self.name}\ncapital : {self.capital}"

    def __len__(self):
        return len(self.goods)

    def __getitem__(self,index):
        return self.goods[index]

    def __reversed__(self):
        return self.goods[::-1]

    def __eq__(self, other):
        return self.capital == other.capital

    def __lt__(self, other):
        return self.capital < other.capital

    def __add__(self, other):
        new_market = Market(f"{self.name} and {other.name}")
        new_market.capital = self.capital + other.capital
        new_market.goods = self.goods + other.goods
        return new_market

    def __iter__(self):
        for product in self.goods:
            yield product

    

if __name__=="__main__":
    m1 = Market('m1')
    m1.add_goods(Product('p1',10))
    m2 = Market('m2')
    m2.add_goods(Product('p2',5))

    mm = m1+m2

    print(mm.goods)

