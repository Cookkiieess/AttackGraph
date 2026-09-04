import pickle
from datetime import datetime, timedelta

from app.models.event import SecurityEvent
from app.ai.features import extract_features


# Load trained model
with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)


# =========================
# BRAND NEW ATTACK
# =========================

attack_scan = SecurityEvent(
    event_id="X001",
    event_type="PORT_SCAN",
    timestamp=datetime(2026, 8, 25, 15, 0, 0),
    source_ip="10.10.10.50",
    source_app="nmap",
    target="SSH_SERVICE",
    status="DETECTED"
)

attack_login = SecurityEvent(
    event_id="X002",
    event_type="LOGIN_ATTEMPT",
    timestamp=datetime(2026, 8, 25, 15, 0, 25),
    source_ip="10.10.10.50",
    source_app="ssh",
    target="SSH_SERVICE",
    status="FAILED",
    user="root"
)


# =========================
# BRAND NEW NORMAL ACTIVITY
# =========================

normal_login = SecurityEvent(
    event_id="X003",
    event_type="LOGIN_ATTEMPT",
    timestamp=datetime(2026, 8, 25, 15, 5, 0),
    source_ip="10.10.10.80",
    source_app="ssh",
    target="SSH_SERVICE",
    status="SUCCESS",
    user="alice"
)

normal_file = SecurityEvent(
    event_id="X004",
    event_type="FILE_ACCESS",
    timestamp=datetime(2026, 8, 25, 15, 5, 20),
    source_ip="10.10.10.80",
    source_app="file_system",
    target="USER_HOME",
    status="SUCCESS",
    user="alice"
)


def predict_pair(event1, event2):

    features = extract_features(event1, event2)

    X = [[
        features["similarity"],
        features["same_ip"],
        features["time_difference"],
        features["same_target"]
    ]]

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return prediction, probability, features


# Test attack
prediction, probability, features = predict_pair(
    attack_scan,
    attack_login
)

print("\n=== NEW ATTACK ===")
print("Features:", features)
print("Prediction:", "ATTACK" if prediction == 1 else "NORMAL")
print(f"Attack probability: {probability:.2%}")


# Test normal activity
prediction, probability, features = predict_pair(
    normal_login,
    normal_file
)

print("\n=== NEW NORMAL ACTIVITY ===")
print("Features:", features)
print("Prediction:", "ATTACK" if prediction == 1 else "NORMAL")
print(f"Attack probability: {probability:.2%}")