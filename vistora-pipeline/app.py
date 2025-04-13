from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")  # You can create a home.html with links to categories

@app.route('/tshirts')
def tshirts():
    return render_template("tshirts.html")

@app.route('/trackpants')
def trackpants():
    return render_template("trackpants.html")

@app.route('/caps')
def caps():
    return render_template("caps.html")

@app.route('/hoodies')
def hoodies():
    return render_template("hoodies.html")

@app.route('/underwear')
def underwear():
    return render_template("underwear.html")

if __name__ == '__main__':
    app.run(debug=True)