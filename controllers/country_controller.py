from flask import render_template, Blueprint, request, redirect

from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_blueprint = Blueprint('countries', __name__)

#index route ('/')
@country_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template('/countries/index.html', countries=countries)

@country_blueprint.route('/countries/<id>/view')
def show(id):
    cities = []
    country = country_repository.select(id)
    cities = city_repository.select_by_country(country)
    return render_template('/countries/view.html', country=country, cities=cities)

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

@country_blueprint.route('/countries/search', methods=['POST'])
def search():
    name = request.form['search']
    country = country_repository.find_by_name(name)
    cities = city_repository.select_by_country(country)
    return render_template('countries/view.html', country=country, cities=cities)
