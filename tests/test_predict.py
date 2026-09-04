import pickle

from app.ai.predict import predict_relationship


with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)


features = {
    "similarity": 0.4794,
    "same_ip": 1,
    "time_difference": 25.0,
    "same_target": 1
}


probability = predict_relationship(model, features)

print("Attack probability:", probability)
print("Attack probability (%):", probability * 100)