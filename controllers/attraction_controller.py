from flask import Flask, render_template, Blueprint, redirect, request
from repositories import city_repository
from repositories import attraction_repository
from repositories import country_repository
from models.attraction import Attraction

attraction_blueprint = Blueprint("attractions", __name__)

@attraction_blueprint.route('/attractions')
def attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/index.html", attractions=attractions)

@attraction_blueprint.route('/attractions/<id>/view')
def show(id):
    attraction = attraction_repository.select(id)
    return render_template('attractions/view.html', attraction=attraction)

@attraction_blueprint.route('/attractions/<id>/delete', methods=['POST'])
def delete(id):
    attraction_repository.delete(id)
    return redirect('/attractions')

@attraction_blueprint.route('/attractions/new')
def new():
    cities = city_repository.select_all()
    return render_template('/cities/new.html', cities=cities)

@attraction_blueprint.route('/attractions/new', methods=['POST'])
def create():
    name = request.form['name']
    city_name = request.form['city']
    city = city_repository.select_by_name(city_name)
    attraction = Attraction(name, city)
    city_repository.save(attraction)

    return redirect('/cities')

@attraction_blueprint.route('/attractions/<id>/edit')
def edit(id):
    attraction = attraction_repository.select(id)
    cities = city_repository.select_all()
    return render_template('attractions/edit.html', attraction=attraction, cities=cities)

@attraction_blueprint.route('/attractions/<id>', methods=['POST'])
def update(id):
    attraction_name = request.form['name']
    city_name = request.form['city']
    city = city_repository.find_by_name(city_name)
    attraction = attraction_repository.select(id)
    attraction.name = attraction_name
    attraction.city = city
    attraction_repository.update(attraction)
    return redirect(f'/attractions/{city.id}/view')    

@attraction_blueprint.route('/attractions/visited')
def get_visited():
    attractions = attraction_repository.select_visited()
    # cities = []
    # for attraction in attractions:
    #     city = city_repository.select(attraction.city.id)
    #     if city not in cities:
    #         cities.append(city)
    # countries = []
    # for city in cities:
    #     country = country_repository.select(city.country.id)
    #     if country not in countries:
    #         countries.append(country)
    dictionaries = []
    for attraction in attractions:
        city = city_repository.select(attraction.city.id)
        country = country_repository.select(city.country.id)
        dictionary = {
            'attraction': attraction.name,
            'city': city.name,
            'country': country.name
        }
        dictionaries.append(dictionary)
    
    return render_template('attractions/visited.html', dictionaries=dictionaries)

    

    
