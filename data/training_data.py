from app.ai.features import extract_features
from data.sample_events import SE_1, SE_2, SE_3, SE_4

training_pairs = [
    (SE_1, SE_2, 1),
    (SE_2, SE_3, 1),
    (SE_1, SE_3, 1),

    (SE_1, SE_4, 0),
    (SE_2, SE_4, 0),
    (SE_3, SE_4, 0),
]

for event1, event2, label in training_pairs:
    features = extract_features(event1, event2)

    print(features, label)

