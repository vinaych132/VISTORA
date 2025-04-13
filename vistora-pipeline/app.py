from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Product 1", "price": 19.99, "description": "A great product."},
    {"id": 2, "name": "Product 2", "price": 29.99, "description": "An even better product."},
    {"id": 3, "name": "Product 3", "price": 39.99, "description": "The best product ever."}
]

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html', products=products)  # Pass product data to the template

# Route for the billing page
@app.route('/billing')
def billing():
    return render_template('billing.html')

# Route for the checkout page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)