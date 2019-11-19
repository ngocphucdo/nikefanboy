from mongoengine import *


class Product (Document):
    image = StringField()
    name = StringField()
    price = StringField()
    detail = StringField()
    code = StringField()
    cate_name = StringField()


class Category (Document):
    cate = StringField()
