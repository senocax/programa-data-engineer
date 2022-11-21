from flask_pymongo import PyMongo
import flask
from flask import render_template

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/Unit18")
db = mongodb_client.db


@app.route('/')
def home():
    """Display options to use app.

    Returns:
        List: app html home
    """
    return render_template('index.html')


@app.route("/create_collection")
def create_collections() -> flask.json.provider.JSONProvider.response:
    """Create collections customer and products.

    Returns:
        flask.json.provider: json response create colections.
    """
    customer = db.customer
    products = db.products

    return flask.jsonify(message="Collection customer and products create")


@app.route("/add_one")
def add_one() -> flask.json.provider.JSONProvider.response:
    """Add one record to customer an products.

    Returns:
        flask.json.provider: json msg add collections
    """
    db.customer.insert_one({'_id': 1,
                            'FullName': 'gerald one',
                            'Level': 1,
                            'Age': 25,
                            'City': 'Illinois',
                            'Zip': 61061})
    db.products.insert_one(
        {'_id': 1, 'ProductName': 'Iphone 8', 'Price': 999, 'stock': 10})

    return flask.jsonify(message="Add collection success")


@app.route("/add_many")
def add_many() -> flask.json.provider.JSONProvider.response:
    """Add many records to customer and products.

    Returns:
        class: msg Add many msg collections
    """
    db.customer.insert_many([{'_id': 2,
                              'FullName': 'Richard Doe',
                              'Level': 1,
                              'Age': 25,
                              'City': 'Illinois',
                              'Zip': 61061},
                             {'_id': 3,
                              'FullName': 'Mike Joe',
                              'Level': 1,
                              'Age': 32,
                              'City': 'New York City',
                              'Zip': 99999},
                             {'_id': 4,
                              'FullName': 'Arnold Stinson',
                              'Level': 2,
                              'Age': 29,
                              'City': 'California',
                              'Zip': 31061}])

    db.products.insert_many([
        {'_id': 2, 'ProductName': 'Sangsung Galaxy 10', 'Price': 800, 'stock': 5},
        {'_id': 3, 'ProductName': 'Motorola Moto E20', 'Price': 500, 'stock': 3},
        {'_id': 4, 'ProductName': 'Samsung Galaxy A13', 'Price': 399, 'stock': 2}])

    return flask.jsonify(message="Add many collections success")


@app.route("/display_collection")
def display() -> flask.json.provider.JSONProvider.response:
    """Display customer and products colections.

    Returns:
        flask.json.provider: Display collections
    """
    customer = db.customer.find()
    products = db.products.find()
    document_customer = [todo for todo in customer]
    document_products = [todo for todo in products]

    return flask.jsonify(
        "customer:",
        [document_customer],
        "products:",
        [document_products])


@app.route("/display_one/<int:todoId>")
def display_one(todoId) -> list:
    """Display one id colecction.

    Args:
        todoId (int): id collection to display

    Returns:
        class: display one id collection
    """
    display_one_customer = db.customer.find_one({"_id": todoId})
    display_one_product = db.products.find_one({"_id": todoId})
    return [
        "customer:",
        display_one_customer,
        "products:",
        display_one_product]


@app.route("/update_one")
def update_one() -> list:
    """Updat one colection of customer and products.

    Returns:
        class: list one update collection
    """
    update_customer = db.customer.find_one_and_update({'_id': 2}, {'$set': {
                                                      'FullName': 'Robert Smith', 'Level': 1, 'Age': 33, 'City': 'Illinois', 'Zip': 61061}})
    update_product = db.products.find_one_and_update(
        {'_id': 2}, {'$set': {'Price': 799}})

    return ["customer:", update_customer, "products:", update_product]


@app.route('/update_many')
def update_many() -> list:
    """Update many collections customer and products.

    Returns:
        class: list update collections
    """
    update_customer = db.customer.update_many(
        {'_id': {'$lte': 2}}, {'$set': {'Level': 3}})
    update_products = db.products.update_many(
        {'_id': {'$gte': 1}}, {'$set': {'stock': 2}})
    return [
        "customer:",
        update_customer.raw_result,
        "products:",
        update_products.raw_result]


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
