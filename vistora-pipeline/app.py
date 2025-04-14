from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')  # Explicitly set the template folder

# Check the current working directory to ensure Flask is looking in the right place
print(f"Current working directory: {os.getcwd()}")

# Home route
@app.route('/')
def home():
    print("Home route accessed")  # Debugging print statement
    return render_template("home.html")

# Route for t-shirts
@app.route('/tshirts')
def tshirts():
    print("T-shirts route accessed")  # Debugging print statement
    return render_template("tshirts.html")

# Route for track pants
@app.route('/trackpants')
def trackpants():
    print("Trackpants route accessed")  # Debugging print statement
    return render_template("trackpants.html")

# Route for caps
@app.route('/caps')
def caps():
    print("Caps route accessed")  # Debugging print statement
    return render_template("caps.html")

# Route for hoodies
@app.route('/hoodies')
def hoodies():
    print("Hoodies route accessed")  # Debugging print statement
    return render_template("hoodies.html")

# Route for underwear
@app.route('/underwear')
def underwear():
    print("Underwear route accessed")  # Debugging print statement
    return render_template("underwear.html")

if __name__ == '__main__':
    # Clear Jinja template cache before running the app to ensure fresh templates are used
    app.jinja_env.cache = {}
    app.run(debug=True)