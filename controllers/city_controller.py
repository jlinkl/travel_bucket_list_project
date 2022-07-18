from flask import Flask, render_template, Blueprint, redirect
from repositories import city_repository
from repositories import country_repository
from models.city import City

city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities=cities)