from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)

# create a route decorator

@app.route('/')
# def index():
#     return "<h1>hello world</h1>"

def index():
    first_name = "Darren"
    stuff = "this is bold text"
    FAVORITE_PIZZA = ["pepperoni", "cheese", "mushrooms", 41]
    return render_template("index.html", 
        first_name=first_name,
        FAVORITE_PIZZA = FAVORITE_PIZZA,
        stuff=stuff)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


#create custom error pages
#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

app.run()