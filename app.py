from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sida.html')
def sida():
    return render_template("sida.html")

@app.route("/http.html")
def http():
    return render_template("http.html")

if __name__ == "__main__":
	app.run(debug=True)
