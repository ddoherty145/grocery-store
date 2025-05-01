from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

def store_query():
    from models import GroceryStore
    return GroceryStore.query

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField(
        'Store Name',
        validators=[DataRequired(), Length(max=100)]
    )
    address = StringField(
        'Address',
        validators=[DataRequired(), Length(max=200)]
    )
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

name = StringField(
    'Item Name',
    validators=[DataRequired(), Length(max=100)]
)
price = StringField(
        'Price',
        validators=[DataRequired()]
    )
category = SelectField(
        'Category',
        choices=[
            ('Produce', 'Produce'),
            ('Deli', 'Deli'),
            ('Bakery', 'Bakery'),
            ('Pantry', 'Pantry'),
            ('Frozen', 'Frozen'),
            ('Other', 'Other')
        ],
        validators=[DataRequired()]
    )
photo_url = StringField(
        'Photo URL',
        validators=[URL(), Length(max=200)]
    )
store_id = QuerySelectField(
        'Store',
        query_factory=lambda: GroceryStore.query.all(),
        get_label='title',
        allow_blank=True,
        validators=[DataRequired()]
    )
submit = SubmitField('Submit')
