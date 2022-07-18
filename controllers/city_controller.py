from flask import Flask, render_template, Blueprint, redirect, request
from repositories import city_repository
from repositories import country_repository
from models.city import City
from models.country import Country

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities=cities)

@city_blueprint.route('/cities/<id>/view')
def show(id):
    city = city_repository.select(id)
    return render_template('cities/view.html', city=city)

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