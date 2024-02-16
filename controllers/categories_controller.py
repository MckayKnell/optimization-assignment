from flask import jsonify

from db import db
from models.category import Categories, category_schema, Categories_Schema
from util.reflection import populate_object


def category_add(req):
    post_data = req.form if req.form else req.json

    new_category = Categories.new_category_obj()
    populate_object(new_category, post_data)

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400

    return jsonify({'message': 'category created', 'result': category_schema.dump(new_category)}), 201


def category_update(req, category_id):
    post_data = req.form if req.form else req.get_json()
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    populate_object(query, post_data)

    try:
        db.session.commit()
    except:
        return jsonify({'message': 'unable to update record'}), 400

    return jsonify({'message': 'category updated'})


def category_get():
    query = db.session.query(Categories).all()

    return jsonify({"message": "category found", "results": Categories_Schema.dump(query)}), 200


def category_by_id(category_id):
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    return jsonify({'message': 'company found', 'result': category_schema.dump(query)})


def delete_category_by_id(category_id):
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if not category_query:
        return jsonify({'message': ' category does not exist'}), 400

    try:
        db.session.delete(category_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": 'cannot delete record'}), 400

    return jsonify({'message': 'category deleted'}), 200
