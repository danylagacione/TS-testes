import sys
import os
sys.path.append(os.getcwd())

from model_product import Product


name1 = 'mouse'
description1 = 'sem fio'
value1 = 50.55

prod = Product(name=name1, description=description1, value=value1)
prod.name = name1
prod.description = description1
prod.value = value1

assert type(prod) == Product
assert isinstance(prod, Product)

assert prod.name == name1
assert prod.description == description1
assert prod.value == value1

assert isinstance(prod.name, str)
assert isinstance(prod.description, str)
assert isinstance(prod.value, float)
