from flask import Flask, jsonify
import random

app = Flask(__name__)

# Path to the quotes text file
QUOTES_FILE = "quotes.txt"

def get_random_quote():
    """Fetches a random quote from the text file."""
    try:
        with open(QUOTES_FILE, 'r') as file:
            quotes = file.readlines()
            if not quotes:
                return "No quotes available."
            return random.choice(quotes).strip()
    except FileNotFoundError:
        return "Quotes file not found."

@app.route("/get-quote", methods=["GET"])
def get_quote():
    """API endpoint to get a random quote."""
    quote = get_random_quote()
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(debug=True)