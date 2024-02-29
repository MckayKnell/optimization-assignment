from flask import Blueprint, request
import controllers

products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def product_add():
    return controllers.product_add(request)


@products.route('/products', methods=['GET'])
def products_get():
    return controllers.products_get()


@products.route('/products/active', methods=['GET'])
def products_active():
    return controllers.products_active()


@products.route('/products/<product_id>', methods=['GET'])
def product_by_id(product_id):
    return controllers.product_by_id(product_id)


@products.route('/products/<product_id>', methods=['GET'])
def product_by_company_id(company_id):
    return controllers.company_by_id(company_id)


@products.route('/products/<product_id>', methods=['PUT'])
def product_update(product_id):
    return controllers.product_update(request, product_id)


@products.route('/product/category', methods=['POST'])
def product_add_category():
    return controllers.product_add_category(request)


@products.route('/product/<product_id>', methods=['DELETE'])
def product_delete(product_id):
    return controllers.product_delete(request, product_id)
