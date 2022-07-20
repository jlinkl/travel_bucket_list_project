from flask import Flask, render_template, Blueprint, redirect, request
from repositories import city_repository
from repositories import attraction_repository
from repositories import country_repository
from repositories import visit_repository
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
    return render_template('/attractions/new.html', cities=cities)

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
    visit = visit_repository.select_by_attraction_id(id)
    return render_template('attractions/edit.html', attraction=attraction, cities=cities, visit=visit)

@attraction_blueprint.route('/attractions/<id>', methods=['POST'])
def update(id):
    attraction_name = request.form['name']
    city_name = request.form['city']
    city = city_repository.find_by_name(city_name)
    visit = visit_repository.select_by_attraction_id(id)
    visit.visited = request.form['visited']
    visit.wants_to_visit = request.form['wants_to_visit']
    attraction = attraction_repository.select(id)
    attraction.name = attraction_name
    attraction.city = city
    attraction_repository.update(attraction)
    visit_repository.update(visit)
    return redirect(f'/attractions/{city.id}/view')    

@attraction_blueprint.route('/attractions/visited')
def get_visited():
    attractions = attraction_repository.select_visited()
    dictionaries = []
    for attraction in attractions:
        city = city_repository.select(attraction.city.id)
        country = country_repository.select(city.country.id)
        dictionary = {
            'attraction': attraction,
            'city': city.name,
            'country': country.name
        }
        dictionaries.append(dictionary)
    
    return render_template('attractions/visited.html', dictionaries=dictionaries)

@attraction_blueprint.route('/attractions/wants_to_visit')
def get_wants_to_visit():
    attractions = attraction_repository.select_wants_to_visit()
    dictionaries = []
    for attraction in attractions:
        city = city_repository.select(attraction.city.id)
        country = country_repository.select(city.country.id)
        dictionary = {
            'attraction': attraction,
            'city': city.name,
            'country': country.name
        }
        dictionaries.append(dictionary)
    
    return render_template('attractions/wants_to_visit.html', dictionaries=dictionaries)




    

    
