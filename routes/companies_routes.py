from flask import Blueprint, request
import controllers

companies = Blueprint('companies', __name__)


@companies.route('/company', methods=['POST'])
def company_add():
    return controllers.company_add(request)


@companies.route('/companies', methods=['GET'])
def companies_get():
    return controllers.companies_get()


@companies.route('/company/<company_id>', methods=['GET'])
def company_by_id(company_id):
    return controllers.company_by_id(company_id)


@companies.route('/company/<company_id>', methods=['PUT'])
def company_update(company_id):
    return controllers.company_update(request, company_id)


@companies.route('/company/delete/<company_id>', methods=['DELETE'])
def delete_company_by_id(company_id):
    return controllers.delete_company_by_id(company_id)
