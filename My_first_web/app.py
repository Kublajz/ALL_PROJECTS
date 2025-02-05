from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/pages/home.html")

@app.route("/about")
def about():
    return render_template("/pages/about.html")

@app.route("/contact")
def contact():
    return render_template("/pages/contact.html")


@app.route("/calc/<int:a>/<int:b>")
def calculator(a, b):
    #a = 10
    #b = 20
    return render_template("/pages/calc.html", a =a, b=b, suma=a+b)
#**kwargs

if __name__ == "__main__":
    app.run(debug=True)