from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello():
    today = datetime.datetime.today().strftime("%A")
    
    if today not in ["Monday", "Friday"]:
        return jsonify({"message": "Server inactive"}), 403

    data = request.get_json(silent=True) or {}
    name = data.get("name", "world")

    return jsonify({"message": f"Hello {name}!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
