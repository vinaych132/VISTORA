from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Home Route
@app.route('/')
def home():
    items = [
        {'name': 'T-Shirt',     'price': 499, 'image': 'tshirt.jpg'},
        {'name': 'Track Pants', 'price': 799, 'image': 'trackpants.jpg'},
        {'name': 'Caps',        'price': 299, 'image': 'caps.jpg'},
        {'name': 'Hoodies',     'price': 999, 'image': 'hoodie.jpg'},
        {'name': 'Underwear',   'price': 199, 'image': 'underwear.jpg'},
    ]
    cart_data = session.get('cart', [])
    return render_template('home.html', items=items, cart_data=cart_data)

# Cart Route
@app.route('/cart')
def cart():
    cart_data = session.get('cart', [])
    return render_template('cart.html', cart_data=cart_data)

# Add to Cart
@app.route('/add_to_cart/<item_name>', methods=['POST'])
def add_to_cart(item_name):
    item_catalog = {
        'T-Shirt':     {'name': 'T-Shirt',     'price': 499, 'image': 'tshirt.jpg'},
        'Track Pants': {'name': 'Track Pants', 'price': 799, 'image': 'trackpants.jpg'},
        'Caps':        {'name': 'Caps',        'price': 299, 'image': 'caps.jpg'},
        'Hoodies':     {'name': 'Hoodies',     'price': 999, 'image': 'hoodie.jpg'},
        'Underwear':   {'name': 'Underwear',   'price': 199, 'image': 'underwear.jpg'},
    }
    item = item_catalog.get(item_name)
    if item:
        cart = session.get('cart', [])
        cart.append(item)
        session['cart'] = cart
    return redirect(url_for('cart'))

# Checkout Route
@app.route('/checkout')
def checkout():
    cart_data = session.get('cart', [])
    return render_template('billing.html', cart_data=cart_data)

# Remove from Cart
@app.route('/remove_from_cart/<item_name>', methods=['POST'])
def remove_from_cart(item_name):
    cart = session.get('cart', [])
    cart = [i for i in cart if i['name'] != item_name]
    session['cart'] = cart
    return redirect(url_for('cart'))

# Clear Cart
@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

# Category Route
@app.route('/category/<category_name>')
def category(category_name):
    products = {
        'tshirts': [
            {'name': 'Classic Tee',     'price': 499, 'image': 'tshirt1.jpg'},
            {'name': 'V-Neck Tee',      'price': 599, 'image': 'tshirt2.jpg'},
        ],
        'trackpants': [
            {'name': 'Slim Trackpant',  'price': 799, 'image': 'trackpant1.jpg'},
            {'name': 'Sport Trackpant', 'price': 899, 'image': 'trackpant2.jpg'},
        ],
        # … other categories …
    }
    items = products.get(category_name, [])
    cart_data = session.get('cart', [])
    return render_template(
        'category.html',
        category_name=category_name.capitalize(),
        items=items,
        cart_data=cart_data
    )

if __name__ == '__main__':
    app.run(debug=True)
