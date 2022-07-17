from email.errors import CloseBoundaryNotFoundDefect
from flask import render_template, Blueprint, request, redirect

from models.country import Country
import repositories.country_repository as country_repository

country_blueprint = Blueprint('countries', __name__)

#index route ('/')
@country_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template('/countries/index.html', countries=countries)

@country_blueprint.route('/countries/<id>/view')
def show(id):
    country = country_repository.select(id)
    return render_template('/countries/view.html', country=country)

@country_blueprint.route('/countries/new')
def new():
    return render_template('/countries/new.html')

@country_blueprint.route('/countries/new', methods=['POST'])
def create():
    name = request.form['name']
    country = Country(name)
    country_repository.save(country)

    return redirect('/countries')

@country_blueprint.route('/countries/<id>/edit')
def edit(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country=country)

@country_blueprint.route('/countries/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    country = country_repository.select(id)
    country.name = name
    country_repository.update(country)
    return redirect(f'/countries/{id}/view')

@country_blueprint.route('/countries/<id>/delete', methods=['POST'])
def delete(id):
    country_repository.delete(id)
    return redirect('/countries')
