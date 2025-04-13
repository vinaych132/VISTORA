from flask import Flask, render_template

app = Flask(__name__)

# Sample product data for categories
products = {
    "t-shirts": [
        {"id": 1, "name": "Basic White T-shirt", "price": 15.99, "description": "Classic white T-shirt for everyday wear."},
        {"id": 2, "name": "Graphic T-shirt", "price": 18.99, "description": "Stylish graphic design on a soft cotton T-shirt."}
    ],
    "polo-t-shirts": [
        {"id": 1, "name": "Red Polo", "price": 25.99, "description": "Comfortable red polo shirt for a smart look."},
        {"id": 2, "name": "Blue Polo", "price": 22.99, "description": "Casual yet elegant blue polo shirt."}
    ],
    "track-pants": [
        {"id": 1, "name": "Jogger Track Pants", "price": 20.99, "description": "Perfect for workouts and casual wear."},
        {"id": 2, "name": "Fitness Track Pants", "price": 24.99, "description": "Comfortable track pants for a workout-ready look."}
    ],
    "caps": [
        {"id": 1, "name": "Baseball Cap", "price": 12.99, "description": "Classic baseball cap in black."},
        {"id": 2, "name": "Snapback Cap", "price": 14.99, "description": "Modern snapback cap in various colors."}
    ],
    "international-styles": [
        {"id": 1, "name": "Japanese Kimono Shirt", "price": 35.99, "description": "Traditional Japanese-style shirt."},
        {"id": 2, "name": "Korean Streetwear Hoodie", "price": 42.99, "description": "Stylish hoodie with Korean street style designs."}
    ],
    "innerwear": [
        {"id": 1, "name": "Comfortable Boxer Shorts", "price": 9.99, "description": "Soft and breathable innerwear."},
        {"id": 2, "name": "Cotton Briefs", "price": 8.99, "description": "Comfortable cotton briefs for everyday use."}
    ]
}

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html', categories=products.keys())  # Pass categories to the homepage

# Route for individual category pages
@app.route('/category/<category_name>')
def category_page(category_name):
    if category_name in products:
        return render_template('category.html', category_name=category_name, products=products[category_name])
    else:
        return "Category not found", 404

if __name__ == '__main__':
    app.run(debug=True)