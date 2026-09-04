def predict_relationship(model, features):
    features = [
        features["similarity"],
        features["same_ip"],
        features["time_difference"],
        features["same_target"]
    ]
    prob =model.predict_proba([features])

    attack_index = list(model.classes_).index(1)

    return prob[0][attack_index]