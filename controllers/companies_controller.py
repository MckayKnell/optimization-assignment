from flask import jsonify

from db import db
from models.companies import Companies, company_schema, companies_schema
from util.reflection import populate_object


def company_add(req):
    post_data = req.form if req.form else req.json

    new_company = Companies.new_company_obj()
    populate_object(new_company, post_data)

    try:
        db.session.add(new_company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "company created", "results": company_schema.dump(new_company)}), 200


def companies_get():
    query = db.session.query(Companies).all()

    return jsonify({"message": "companies found", "results": companies_schema.dump(query)}), 200


def company_by_id(req, company_id):
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id)

    return jsonify({'message': 'company found', 'result': company_schema.dump(company_query)})


def company_update(req, company_id):
    post_data = req.form if req.form else req.json
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id)

    populate_object(company_query, post_data)

    db.session.commit()


def delete_company_by_id(company_id):
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    if not company_query:
        return jsonify({'message': ' company does not exist'}), 400

    try:
        db.session.delete(company_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": 'cannot delete record'}), 400

    return jsonify({'message': 'company deleted'}), 200
