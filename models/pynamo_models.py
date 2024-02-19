import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

table = os.environ.get('TABLE_NAME')

#Model for Clients
class Client(Model):
    class Meta:
        table_name = table

    PK = UnicodeAttribute(hash_key=True)
    SK = UnicodeAttribute(range_key=True)
    email = UnicodeAttribute(default='')
    full_name = UnicodeAttribute(default='')
    mobile = UnicodeAttribute(default='')

class Seller(Model):
    class Meta:
        table_name = table

    PK = UnicodeAttribute(hash_key=True)
    SK = UnicodeAttribute(range_key=True)
    email = UnicodeAttribute(default='')
    full_name = UnicodeAttribute(default='')

class Product(Model):
    class Meta:
        table_name = table

    PK = UnicodeAttribute(hash_key=True)
    SK = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute(default='')
    price = UnicodeAttribute(default='')
    category = UnicodeAttribute(default='')

class Purchase(Model):
    class Meta:
        table_name = table

    PK = UnicodeAttribute(hash_key=True)
    SK = UnicodeAttribute(range_key=True)
    client_name = UnicodeAttribute(default='')
    seller_name = UnicodeAttribute(default='')
    product_name = UnicodeAttribute(default='')
    prize = UnicodeAttribute(default='')
    purchase_date = UnicodeAttribute(default='')