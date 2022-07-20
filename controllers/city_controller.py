from flask import Flask, render_template, Blueprint, redirect, request
from repositories import city_repository
from repositories import country_repository
from repositories import attraction_repository
from models.city import City

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities=cities)

@city_blueprint.route('/cities/<id>/view')
def show(id):
    city = city_repository.select(id)
    attractions = attraction_repository.select_by_city(city)
    return render_template('cities/view.html', city=city, attractions=attractions)

@city_blueprint.route('/cities/<id>/delete', methods=['POST'])
def delete(id):
    city_repository.delete(id)
    return redirect('/cities')

@city_blueprint.route('/cities/new')
def new():
    countries = country_repository.select_all()
    return render_template('/cities/new.html', countries=countries)

@city_blueprint.route('/cities/new', methods=['POST'])
def create():
    name = request.form['name']
    country_name = request.form['country']
    country = country_repository.find_by_name(country_name)
    city = City(name, country)
    city_repository.save(city)

    return redirect('/cities')

@city_blueprint.route('/cities/<id>/edit')
def edit(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city=city, countries=countries)

@city_blueprint.route('/cities/<id>', methods=['POST'])
def update(id):
    city_name = request.form['name']
    country_name = request.form['country']
    country = country_repository.find_by_name(country_name)
    city = city_repository.select(id)
    city.name = city_name
    city.country = country
    city_repository.update(city)
    return redirect(f'/countries/{country.id}/view')

@city_blueprint.route('/cities/search', methods=['POST'])
def search():
    name = request.form['search']
    city = city_repository.find_by_name(name)
    return render_template('cities/view.html', city=city)
