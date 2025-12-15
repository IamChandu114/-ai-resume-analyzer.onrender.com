import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use a custom folder named 'my_templates' instead of the default 'templates'
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),  # <-- custom template folder
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/")
def index():
    return render_template("index.html")  # Flask will now look inside 'my_templates'

if __name__ == "__main__":
    app.run(debug=True)



