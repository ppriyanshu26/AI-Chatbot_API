from flask import Flask, request, jsonify
import datetime
import pytz 

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello():
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(ist)
    
    today = now.strftime("%A")
    current_hour = now.hour

    if today not in ["Monday", "Friday"]:
        return jsonify({"message": "Server active on Mondays and Fridays only"}), 403

    if current_hour < 9 or current_hour >= 21:
        return jsonify({"message": "Server active today from 9AM to 9PM"}), 403

    data = request.get_json(silent=True) or {}
    name = data.get("name", "world")

    return jsonify({
        "message": f"Hello {name}!",
        "time": now.strftime("%Y-%m-%d %H:%M:%S %Z")
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
