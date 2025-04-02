from flask import Flask, request, redirect, jsonify
import random, string

app = Flask(__name__)
url_mapping = {}  # In-memory key-value store

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    long_url = data.get("long_url")
    short_code = generate_short_code()
    url_mapping[short_code] = long_url
    return jsonify({"short_url": f"http://localhost:5000/{short_code}"})

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    long_url = url_mapping.get(short_code)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
