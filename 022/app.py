from flask import Flask, request, jsonify
from datetime import datetime

from db import db, ma
from stock_code import CODE, SCHEMA, SCHEMAS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ROUTES = {
    'STOCK': '/<string:code>/<string:date>',
    'ALL_STOCK': '/<string:code>'
}


@app.route(ROUTES['ALL_STOCK'], methods=['GET'])
def get_stocks(code):
    table = CODE[code]
    all_stocks = table.query.all()
    result = SCHEMAS.dump(all_stocks)
    return jsonify({f"{code}": result})


@app.route(ROUTES['STOCK'], methods=['GET'])
def get_stock(code, date):
    table = CODE[code]
    date = datetime.strptime(date, '%Y-%m-%d').date()
    stock = table.query.get(date)
    if stock is None:
        return {'message': '404 not found'}, 404
    return SCHEMA.jsonify(stock)


@app.route(ROUTES['ALL_STOCK'], methods=['POST'])
def add_stock(code):
    table = CODE[code]
    date = datetime.strptime(request.json['date'], '%Y-%m-%d').date()
    if table.query.get(date) is not None:
        return {"message": "primary key is not duplicated"}, 400
    price_close = request.json['price_close']
    price_open = request.json['price_open']
    price_high = request.json['price_high']
    price_low = request.json['price_low']
    volume = request.json['volume']
    change = request.json['change']
    new_stock = table(date, price_close, price_open,
                      price_high, price_low, volume, change)
    db.session.add(new_stock)
    db.session.commit()
    return SCHEMA.jsonify(new_stock)


@app.route(ROUTES['STOCK'], methods=['PUT'])
def update_stock(code, date):
    table = CODE[code]
    date = datetime.strptime(date, '%Y-%m-%d').date()
    stock = table.query.get(date)
    if stock is None:
        return {'message': '404 not found'}, 404
    data = request.get_json()
    for key, value in data.items():
        setattr(stock, key, value)
    db.session.commit()
    return SCHEMA.jsonify(stock)


@app.route(ROUTES['STOCK'], methods=['DELETE'])
def delete_product(code, date):
    table = CODE[code]
    date = datetime.strptime(date, '%Y-%m-%d').date()
    stock = table.query.get(date)
    if stock is None:
        return {'message': '404 not found'}, 404
    db.session.delete(stock)
    db.session.commit()
    return SCHEMA.jsonify(stock)


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
