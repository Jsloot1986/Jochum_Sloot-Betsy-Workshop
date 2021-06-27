from peewee import *

from models import *

database = SqliteDatabase('betsy_workshop.db')

def add_tag(product, tag_name):
    tag = Tag.get(Tag.name == tag_name)
    if tag in product.tags:
        None
    else:
        product.tags.add([tag])

def make_records():
    User.get_or_create(first_name='Jochum', last_name='Sloot', defaults={ 'street': 'J. de Vriesstraat 1', 'town' : 'Amsterdam'})
    User.get_or_create(first_name="David", last_name="Hello", defaults={ 'street' : 'Maria Anthoinetstraat 1', 'town' : 'Amsterdam'})
    User.get_or_create(first_name="Mirjam", last_name="Sloot", defaults={'street':'Friese tuinen 1', 'town':'Dokkum'})
    User.get_or_create(first_name="Sabrina", last_name="Boonstra", defaults= {'street':'Antwerpenstraat 1', 'town':'Rotterdam'})
    Tag.get_or_create(name="Domestic")
    Tag.get_or_create(name="Tool")
    Tag.get_or_create(name="Garden")
    Tag.get_or_create(name="Clothes")
    Tag.get_or_create(name="Games")
    Product.get_or_create(
        product_name="Sweater",
        defaults={
            'description': 'Sweater New-York',
            'price_per_unit': 50.95,
            'tags':[],
            'catlog_id': 1
        })
    sweater = Product.get(Product.product_name == "Sweater")
    add_tag(sweater, "Domestic")
    add_tag(sweater, "Clothes")
    Product.get_or_create(
        product_name="Trouser",
        defaults={
            'description':'Trouser Levi',
            'price_per_unit': 40.95,
            'tags':[],
            'catalog_id': 1
        })
    add_tag(sweater, "Domestic")
    add_tag(sweater, "Clothes")
    Product.get_or_create(
        product_name="Cluedo",
        defaults={
            'description': 'Cluedo the New-York edition',
            'price_per_unit': 21.95,
            'tags':[],
            'catalog_id':1
        })
    add_tag(sweater, "Games")
    UserProduct.get_or_create(
            user_id=1, 
            defaults={
                'product_id': 1, 
                'number': 2})
    UserProduct.get_or_create(
            user_id=1, 
            defaults={
                'product_id':2, 
                'number': 2})
    UserProduct.get_or_create(
            user_id=2, 
            defaults={
                'product_id':1, 
                'number':2})
    UserProduct.get_or_create(
            user_id=2, 
            defaults={
                'product_id':2, 
                'number':3})
    Product.get_or_create(
            product_name="T-shirt",
            defaults={
                'description': 'T-shirt from Garfield',
                'price_per_unit': 10.9496,
                'tags':[],
                'catalog_id':1
            })
    
    tshirt_id = Product.get(Product.product_name == "T-shirt")
    if UserProduct.select().where(UserProduct.user_id == 4 and UserProduct.product_id == tshirt_id):
        None
    else:
        UserProduct.get_or_create(user_id = 4, product_id = tshirt_id, number = 10)