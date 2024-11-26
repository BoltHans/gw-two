from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, World! Welcome to your Flask app on GCP!"})

@app.route('/api')
def api():
    return jsonify({"status": "success", "data": "This is a simple API response!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
