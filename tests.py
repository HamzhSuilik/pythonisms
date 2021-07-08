from pythonisms import Market,Product

def test_str():
    market = Market('market1')
    market.add_goods(Product('p1',10))
    
    actual = market.__str__()
    expected = 'The market name market1 , with capital 10 $'
    assert actual == expected

def test_repr():
    market = Market('market1')
    market.add_goods(Product('p1',10))
    actual = market.__repr__()
    expected = 'Name : market1\ncapital : 10'
    assert actual == expected

def test_len():
    market = Market('market1')
    market.add_goods(Product('p1',10))
    market.add_goods(Product('p2',40))
    market.add_goods(Product('p3',10))
    actual = len(market)
    expected = 3
    assert actual == expected

def test_getitem():
    market = Market('market1')
    market.add_goods(Product('p1',10))
    market.add_goods(Product('p2',40))
    p3 = Product('p3',10)
    market.add_goods(p3)
    actual = market[2]
    expected = p3
    assert actual == expected

def test_reversed():
    market = Market('market1')
    p1=Product('p1',10)
    market.add_goods(p1)
    p2=Product('p2',40)
    market.add_goods(p2)
    p3 = Product('p3',10)
    market.add_goods(p3)
    actual = market.__reversed__()
    expected = [p3,p2,p1]
    assert actual == expected

def test_eq():
    market = Market('market1')
    market.add_goods(Product('p1',10))
    market.add_goods(Product('p2',10))
    market.add_goods(Product('p3',10))

    market2 = Market('market1')
    market2.add_goods(Product('p1',10))
    market2.add_goods(Product('p2',20))


  
    assert market == market2

    market2.add_goods(Product('p3',5))
 
    assert not market == market2

def test_lt():
    market = Market('market1')
    market.add_goods(Product('p1',10))
    market.add_goods(Product('p2',50))
    market.add_goods(Product('p3',10))

    market2 = Market('market1')
    market2.add_goods(Product('p1',10))
    market2.add_goods(Product('p2',20))


    assert market > market2

def test_add():
    m1 = Market('m1')
    p1 = Product('p1',10)
    m1.add_goods(p1)
    m2 = Market('m2')
    p2 = Product('p2',5)
    m2.add_goods(p2)
    mm = m1+m2
    actual = mm.name
    expected = 'm1 and m2'
    assert expected == actual

    actual = mm.capital
    expected = 15
    assert expected == actual

    actual = mm.goods
    expected = [p1,p2]
    assert expected == actual
    

def test_iter():
    market = Market('market1')
    p1=Product('p1',10)
    market.add_goods(p1)
    p2=Product('p2',40)
    market.add_goods(p2)
    p3 = Product('p3',10)
    market.add_goods(p3)

    arr=[]
    for product in market:
        arr.append(product)


    actual = arr
    expected = [p1,p2,p3]
    assert actual == expected

if __name__=="__main__":
    test_add()
    test_eq()
    test_getitem()
    test_iter()
    test_len()
    test_reversed()
    test_repr()
    test_lt()
    test_str()