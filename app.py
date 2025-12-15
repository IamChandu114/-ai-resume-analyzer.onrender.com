import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use a custom template folder 'my_templates'
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "index.html"),
    static_folder=os.path.join(BASE_DIR, "static")
)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)








