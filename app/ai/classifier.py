from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def train_model(dataset):

    X = []
    y = []

    for row in dataset:
        features = row["features"]

        X.append([
            features["similarity"],
            features["same_ip"],
            features["time_difference"],
            features["same_target"]
        ])

        y.append(row["label"])

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Create model
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression()
    )

    # Train
    model.fit(X_train, y_train)

    # Test
    predictions = model.predict(X_test)

    print("\n=== MODEL RESULTS ===")
    print(f"Training examples: {len(X_train)}")
    print(f"Testing examples:  {len(X_test)}")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    return model