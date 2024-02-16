from flask import Blueprint, request
import controllers

products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def products_add():
    return controllers.products_add(request)


@products.route('/products', methods=['GET'])
def products_get():
    return controllers.products_get()


@products.route('/products/active', methods=['GET'])
def products_active():
    return controllers.products_active()


@products.route('/products/<product_id>', methods=['GET'])
def products_by_id(product_id):
    return controllers.products_by_id(product_id)


@products.route('/products/<product_id>', methods=['PUT'])
def products_update(product_id):
    return controllers.products_update(request, product_id)


@products.route('/product/category', methods=['POST'])
def product_add_category():
    return controllers.product_add_category(request)


@products.route('/product/delete/<product_id>', methods=['DELETE'])
def product_delete(product_id):
    return controllers.product_delete(request, product_id)
