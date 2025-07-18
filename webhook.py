from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root_route_handler():
    return jsonify("HUNTER - Let the hunt begin!")

@app.route("/health")
def health_check():
    return jsonify({"status": "OK"})

def start_webhook():
    app.run(host="0.0.0.0", port=8000, threaded=True)
