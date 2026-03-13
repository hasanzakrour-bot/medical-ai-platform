import json
from datetime import datetime

PREDICTION_FILE = "prediction_logs.json"


def log_prediction(data):

    entry = {
        "timestamp": str(datetime.utcnow()),
        "prediction": data
    }

    with open(PREDICTION_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")