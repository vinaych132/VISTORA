from flask import Flask, render_template
import os

# Absolute path to templates folder
template_path = os.path.join(os.getcwd(), 'templates')
print(f"Template folder being used: {template_path}")
print("Contents of template folder:", os.listdir(template_path))

app = Flask(__name__, template_folder=template_path)

@app.route('/')
def home():
    print("Home route hit")
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)