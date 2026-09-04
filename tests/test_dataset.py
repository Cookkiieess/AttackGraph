from data.dataset import generate_dataset
import pickle

dataset = generate_dataset(5000)


print("Number of examples:", len(dataset))

with open("data/training_data.pkl", "wb") as f:
    pickle.dump(dataset, f)

print(f"Saved {len(dataset)} examples")


for row in dataset[:10]:
    print(row)