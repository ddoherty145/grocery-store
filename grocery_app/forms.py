from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, Optional
from grocery_app.models import GroceryStore

# Proper query factory using app-level model path
def store_query():
    return GroceryStore.query

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField(
        "Store Title", 
        validators=[DataRequired(), Length(max=100)]
    )
    address = StringField(
        "Address", 
        validators=[DataRequired(), Length(max=200)]
    )
    submit = SubmitField("Submit")

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField(
        "Item Name", 
        validators=[DataRequired(), Length(max=100)]
    )
    price = FloatField(
        "Price ($)", 
        validators=[DataRequired()]
    )
    category = SelectField(
        "Category",
        choices=[
            ('PRODUCE', 'Produce'),
            ('DAIRY', 'Dairy'),
            ('BAKERY', 'Bakery'),
            ('MEAT', 'Meat'),
            ('PANTRY', 'Pantry'),
            ('FROZEN', 'Frozen'),
            ('OTHER', 'Other')
        ],
        validators=[DataRequired()]
    )
    photo_url = StringField(
        "Photo URL", 
        validators=[Optional(), URL()]
    )
    store = QuerySelectField(
        "Store", 
        query_factory=store_query, 
        allow_blank=False, 
        get_label="title",
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit")
