from flask import Flask, render_template , jsonify
app = Flask(__name__)

products = [
    {
        'id': 1,
        'Robot Type' : "Manual",
        'Price': "50,000",
        'Efficiency': "95%"

    },

    {
        'id': 2,
        'Robot Type' : "Semi-Automatic",
        'Price': "1,00,000",
        'Efficiency': "95%"

    },
    {
        'id': 3,
        'Robot Type' : "Fully Automatic",
        'Price': "1,50,000",
        'Efficiency': "95%"

    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", product = products)

@app.route("/jobs")
def list_jobs():
    return jsonify(products)
if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)

    
    