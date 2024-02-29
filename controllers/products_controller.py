from flask import jsonify

from db import db
from models.products import Products, product_schema, products_schema
from models.categories import Categories
from util.reflection import populate_object


def product_add(req):
    post_data = req.form if req.form else req.json

    new_product = Products.new_product_obj()
    populate_object(new_product, post_data)
    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "product created", "results": product_schema.dump(new_product)}), 200


def products_get():
    query = db.session.query(Products).all()

    return jsonify({"message": "products found", "results": products_schema.dump(query)}), 200


def products_active():
    query = db.session.query(Products).filter(Products.active == True).all()

    return jsonify({"message": "products found", "results": products_schema.dump(query)}), 200


def product_by_id(product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).all()

    return jsonify({"message": "product found", "results": products_schema.dump(query)}), 200


def product_by_id(company_id):
    query = db.session.query(Products).filter(Products.company_id == company_id).all()

    return jsonify({"message": "product found", "results": products_schema.dump(query)}), 200


def product_update(req, product_id):
    post_data = req.form if req.form else req.json

    new_product = Products.new_product_obj()
    populate_object(new_product, post_data)

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "product created", "results": product_schema.dump(new_product)}), 200


def product_add_category(req):
    post_data = req.form if req.form else req.json

    product_id = post_data.get('product_id')
    category_id = post_data.get('category_id')

    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    product_query.categories.append(category_query)

    db.session.commit()
    return jsonify({"message": 'category added', 'results': product_schema.dump(product_query)})


def product_delete(req, product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not query:
        return jsonify({"message": 'product could not be found'}), 404

    try:
        db.session.delete(query)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete product"})

    return jsonify({'message': 'record has been deleted'})
