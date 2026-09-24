from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/greeting")
def greeting():
    return """
    <h1>👋 Welcome Students!</h1>
    <p>This is a basic Flask route.</p>
    <p>Every URL can be connected to a Python function.</p>
    """


@app.route("/about_flask")
def about_flask():
    return """
    <h1>📚 What is Flask?</h1>

    <p>
        Flask is a lightweight Python web framework.
    </p>

    <h2>Students can learn:</h2>

    <ul>
        <li>Creating web applications using Python</li>
        <li>URL Routing</li>
        <li>HTML Templates</li>
        <li>CSS Styling</li>
        <li>Handling User Input</li>
        <li>Connecting Python with Web Pages</li>
    </ul>
    """


@app.route("/calculate")
def calculate():

    a = 10
    b = 20

    result = a + b

    return f"""
    <h1>🧮 Python Calculation</h1>

    <h2>{a} + {b} = {result}</h2>

    <p>
        Flask can execute Python code and
        display the result in the browser.
    </p>
    """


@app.route("/student")
def student():

    name = request.args.get("name")

    return f"""
    <h1>🎓 Student Information</h1>

    <h2>Hello, {name}!</h2>

    <p>
        This example demonstrates how Flask
        receives data from a URL.
    </p>

    <p>
        Query Parameter:||||
        <strong>name = {name}</strong>
    </p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

