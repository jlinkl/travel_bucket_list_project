from flask import Flask, render_template
from controllers.country_controller import country_blueprint
from controllers.city_controller import city_blueprint
from controllers.attraction_controller import attraction_blueprint

app = Flask(__name__)

app.register_blueprint(country_blueprint)
app.register_blueprint(city_blueprint)
app.register_blueprint(attraction_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)