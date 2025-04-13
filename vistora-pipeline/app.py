from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Homepage route

# Route for the billing page
@app.route('/billing')
def billing():
    return render_template('billing.html')  # Billing page route

# Route for the checkout page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')  # Checkout page route

# Route for creating a dummy order (to test order ID)
@app.route('/create-order')
def create_order():
    order_id = "12345"  # Replace with actual logic to generate order ID
    response = {
        "status": "success",
        "message": "Order Created Successfully",
        "order_id": order_id
    }
    return jsonify(response)  # Return a JSON response with the order ID

if __name__ == '__main__':
    app.run(debug=True)