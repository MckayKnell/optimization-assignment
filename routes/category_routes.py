from flask import Blueprint, request
import controllers

categories = Blueprint('categories', __name__)


@categories.route('/category', methods=['POST'])
def category_add():
    return controllers.category_add(request)


@categories.route('/category/<category_id>', methods=['PUT'])
def category_update(category_id):
    return controllers.category_update(request, category_id)


@categories.route('/categories', methods=['GET'])
def categories_get_all():
    return controllers.categories_get_all()


@categories.route('/category/<category_id>', methods=['GET'])
def category_by_id(category_id):
    return controllers.category_by_id(category_id)


@categories.route('/category/delete/<category_id>', methods=['DELETE'])
def delete_category_by_id(category_id):
    return controllers.delete_category_by_id(category_id)
