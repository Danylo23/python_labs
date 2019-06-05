from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Components(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=100), unique=False)
    price = db.Column(db.Integer, unique=False)
    power_consumption = db.Column(db.Integer, unique=False)
    product_year = db.Column(db.Integer, unique=False)

    def __init__(self, name, price, power_consumption, product_year):
        self.name = name
        self.price = price
        self.power_consumption = power_consumption
        self.product_year = product_year


class ComponentsSchema(ma.Schema):
    class Meta:
        fields = ("name", "price", "power_consumption", "product_year")


component_schema = ComponentsSchema()
components_schema = ComponentsSchema(many=True)


@app.route("/component", methods=["POST"])
def add_component():
    name = request.json['name']
    price = request.json['price']
    power_consumption = request.json['power_consumption']
    product_year = request.json['product_year']
    new_component = Components(name, price, power_consumption, product_year)
    db.session.add(new_component)
    db.session.commit()
    results = component_schema.dump(new_component)
    return jsonify(results.data)


@app.route("/component", methods=["GET"])
def get_components():
    all_components = Components.query.all()
    results = components_schema.dump(all_components)
    return jsonify(results.data)


@app.route("/component/<id>", methods=["GET"])
def get_component_by_id(id):
    component = Components.query.get(id)
    return component_schema.jsonify(component)


@app.route("/component/<id>", methods=["PUT"])
def update_component(id):
    component = Components.query.get(id)
    name = request.json['name']
    price = request.json['price']
    power_consumption = request.json['power_consumption']
    product_year = request.json['product_year']
    component.name = name
    component.price = price
    component.power_consumption = power_consumption
    component.product_year = product_year
    db.session.commit()
    return component_schema.jsonify(component)


@app.route("/component/<id>", methods=["DELETE"])
def delete_component(id):
    component = Components.query.get(id)
    db.session.delete(component)
    db.session.commit()
    return component_schema.jsonify(component)


if __name__ == '__main__':
    app.run(debug=True)
