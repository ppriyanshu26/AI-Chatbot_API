import json
import datetime
import pytz  

def lambda_handler(event, context):
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(ist)
    
    today = now.strftime("%A")
    current_hour = now.hour

    if today not in ["Monday", "Friday"]:
        return {
            "statusCode": 403,
            "body": json.dumps({"message": "Server active on Mondays and Fridays"})
        }

    if current_hour < 9 or current_hour >= 21:
        return {
            "statusCode": 403,
            "body": json.dumps({"message": "Server active today from 9AM to 9PM"})
        }

    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        body = {}

    name = body.get("name", "world")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello {name}!",
            "time": now.strftime("%Y-%m-%d %H:%M:%S %Z")
        })
    }
