from flask import render_template, Blueprint

from models.country import Country
import repositories.country_repository as country_repository

country_blueprint = Blueprint('countries', __name__)

#index route ('/')
@country_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template('/countries/index.html', countries=countries)

