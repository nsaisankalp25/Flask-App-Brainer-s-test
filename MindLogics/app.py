from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
#run_with_ngrok(app)

@app.route("/")
def hello_world():
    return """Hello, World!
    
    Its workinggg!
    """

@app.route("/Home")
def func1():
    return render_template("HomePage.html")
@app.route("/Start")
def func2():
    return render_template("Page1.html")
@app.route("/start")
def func3():
    return render_template("Page2.html")
@app.route("/test")
def func4():
    return render_template("Page3.html")



if __name__ == "__main__":
    app.run(port = 5001)