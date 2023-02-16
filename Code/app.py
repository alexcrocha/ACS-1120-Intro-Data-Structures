"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, render_template
from helper_functions import read_file
from sample_dict import generate_markov

app = Flask(__name__)

text = read_file("./data/sample.txt")

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    num_of_sentences = int(request.args.get("num")) if request.args.get("num") else 1

    context = {"sentence": generate_markov(text, num_of_sentences)}

    return render_template("index.html", **context)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
    To learn more about Flask's DEBUG mode, visit
    https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True, port=3000)
