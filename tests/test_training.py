import pickle

from app.ai.classifier import train_model


with open("data/training_data.pkl", "rb") as f:
    dataset = pickle.load(f)

print(f"Loaded {len(dataset)} training examples")

model = train_model(dataset)

print("\nModel trained!")

with open("data/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel saved!")

