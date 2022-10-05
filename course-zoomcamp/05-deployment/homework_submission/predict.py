import pickle


dv_file = "dv.bin"
model_file = "model2.bin"

with open(dv_file, "rb") as dv_f:
    dv = pickle.load(dv_f)

with open(model_file, "rb") as mode_f:
    model = pickle.load(mode_f)


def predict(client):
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]

    return y_pred


if __name__ == "__main__":
    client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
    pred = predict(client)
    print(f"Probability that client gets credit card: {round(pred, 4)}")
