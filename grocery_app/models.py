from grocery_app.extensions import db
from grocery_app.utils import FormEnum
from flask_login import UserMixin
from grocery_app.extensions import db

shopping_list_table = db.Table(
    'shopping_list',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('grocery_item.id'))
)

class User(UserMixin, db.Model):
    id = db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    shopping_list_items = db.relationship(
        'GroceryItem',
        secondary=shopping_list_table,
        backref='user_who_want'
    )


class ItemCategory(FormEnum):
    """Categories of grocery items."""
    PRODUCE = 'Produce'
    DELI = 'Deli'
    BAKERY = 'Bakery'
    PANTRY = 'Pantry'
    FROZEN = 'Frozen'
    OTHER = 'Other'


class GroceryStore(db.Model):
    """Grocery Store model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user_id'))
    created_by = db.relationship('User')
    # items = db.relationship('GroceryItem', back_populates='store')


class GroceryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    photo_url = db.Column(db.String(200))
    store_id = db.Column(db.Integer, db.ForeignKey('grocery_store.id'))
    store = db.relationship('GroceryStore', backref='items')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')