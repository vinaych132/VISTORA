from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Route to display products for a specific category
@app.route('/category/<category_name>')
def category(category_name):
    # Hardcoded products for the demo (can be dynamic from a database)
    products = {
        'tshirts': [
            {'name': 'Classic Tee', 'price': 499, 'image': 'tshirt1.jpg'},
            {'name': 'V-Neck Tee', 'price': 599, 'image': 'tshirt2.jpg'}
        ],
        'trackpants': [
            {'name': 'Slim Trackpant', 'price': 799, 'image': 'trackpant1.jpg'},
            {'name': 'Sport Trackpant', 'price': 899, 'image': 'trackpant2.jpg'}
        ],
        'caps': [
            {'name': 'Basic Cap', 'price': 299, 'image': 'cap1.jpg'},
            {'name': 'Snapback Cap', 'price': 399, 'image': 'cap2.jpg'}
        ],
        'hoodies': [
            {'name': 'Classic Hoodie', 'price': 999, 'image': 'hoodie1.jpg'},
            {'name': 'Zipped Hoodie', 'price': 1199, 'image': 'hoodie2.jpg'}
        ],
        'underwear': [
            {'name': 'Cotton Briefs', 'price': 199, 'image': 'underwear1.jpg'},
            {'name': 'Boxer Shorts', 'price': 299, 'image': 'underwear2.jpg'}
        ]
    }

    items = products.get(category_name, [])
    return render_template('category.html', category_name=category_name.capitalize(), items=items, cart_count=len(session.get('cart', [])))


# Add to Cart Route - Add an item to the cart
@app.route('/add_to_cart/<item_name>', methods=['POST'])
def add_to_cart(item_name):
    # Example items (this can be dynamic, e.g., retrieved from a database)
    item_catalog = {
        'Classic Tee': {'name': 'Classic Tee', 'price': 499, 'image': 'tshirt1.jpg'},
        'V-Neck Tee': {'name': 'V-Neck Tee', 'price': 599, 'image': 'tshirt2.jpg'},
        'Slim Trackpant': {'name': 'Slim Trackpant', 'price': 799, 'image': 'trackpant1.jpg'},
        'Sport Trackpant': {'name': 'Sport Trackpant', 'price': 899, 'image': 'trackpant2.jpg'},
        'Basic Cap': {'name': 'Basic Cap', 'price': 299, 'image': 'cap1.jpg'},
        'Snapback Cap': {'name': 'Snapback Cap', 'price': 399, 'image': 'cap2.jpg'},
        'Classic Hoodie': {'name': 'Classic Hoodie', 'price': 999, 'image': 'hoodie1.jpg'},
        'Zipped Hoodie': {'name': 'Zipped Hoodie', 'price': 1199, 'image': 'hoodie2.jpg'},
        'Cotton Briefs': {'name': 'Cotton Briefs', 'price': 199, 'image': 'underwear1.jpg'},
        'Boxer Shorts': {'name': 'Boxer Shorts', 'price': 299, 'image': 'underwear2.jpg'}
    }

    item = item_catalog.get(item_name)
    
    if item:
        cart_data = session.get('cart', [])
        cart_data.append(item)  # Add item to the cart
        session['cart'] = cart_data  # Store updated cart back to session

    return redirect(url_for('cart'))


# Cart Route - Displays the current cart
@app.route('/cart')
def cart():
    # Get the cart data from the session
    cart_data = session.get('cart', [])
    return render_template('cart.html', cart_data=cart_data)


# Checkout Route - Proceed to checkout page
@app.route('/checkout')
def checkout():
    # Get the cart data and send it to the billing page
    cart_data = session.get('cart', [])
    return render_template('billing.html', cart_data=cart_data)


# Remove Item from Cart
@app.route('/remove_from_cart/<item_name>', methods=['POST'])
def remove_from_cart(item_name):
    cart_data = session.get('cart', [])
    cart_data = [item for item in cart_data if item['name'] != item_name]
    session['cart'] = cart_data  # Store updated cart back to session
    return redirect(url_for('cart'))


# Clear Cart Route
@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    session.pop('cart', None)  # Clear the cart from session
    return redirect(url_for('cart'))


if __name__ == '__main__':
    app.run(debug=True)
