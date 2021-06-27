from enum import unique
from peewee import (CharField, Check, DateField, DecimalField,
                    ForeignKeyField, IntegerField, ManyToManyField, Model,
                    SqliteDatabase)

database = SqliteDatabase('betsy_workshop.db')

class BaseModel(Model):
    class Meta:
        database = database
#if no primary key is defined an implicit primary key is added

class User(BaseModel):
    first_name = CharField(unique=True)
    last_name = CharField()
    street = CharField()
    city = CharField()

class Product(BaseModel):
    product_name = CharField()
    description = CharField()
    price_per_unit = DecimalField(decimal_places=2, auto_round=True)
    owner = ForeignKeyField(User, backref='products')

class Tag(BaseModel):
    name = CharField(unique=True)

class ProductTags(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)

class Transaction(BaseModel):
    buyer_id = ForeignKeyField(User, backref='transactions')
    product_id = ForeignKeyField(Product, backref='products')
    number = IntegerField(constraints=[Check('number>0')])
    sell_date = DateField()
    sell_price = DecimalField(8, 2, True)

def create_tables():
    with database:
        database.create_tables(
            [User, Product, Transaction]
        )

       