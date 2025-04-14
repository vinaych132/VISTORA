from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Dynamic category route
@app.route('/category/<category_name>')
def category(category_name):
    # Ensure the category name is valid (could add checks here if needed)
    return render_template('category.html', category_name=category_name)

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/')
def home():
    categories = [
        {'name': 'T-Shirts', 'image': 'tshirts.jpg'},
        {'name': 'Track Pants', 'image': 'trackpants.jpg'},
        {'name': 'Caps', 'image': 'caps.jpg'},
        {'name': 'Hoodies', 'image': 'hoodies.jpg'},
        {'name': 'Underwear', 'image': 'underwear.jpg'}
    ]
    return render_template("home.html", categories=categories)