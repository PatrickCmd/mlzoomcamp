from flask import Flask
from flask import request
from flask import jsonify

from predict import predict


app = Flask("Credict Card Service")


@app.route("/predict", methods=["POST"])
def predict_client():
    client = request.get_json()

    pred = predict(client)
    card = pred >= 0.5

    result = {
        "card": bool(card),
        "card_probability": round(float(pred), 4),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
