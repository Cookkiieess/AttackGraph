from app.ai.features import extract_features
from app.ai.predict import predict_relationship


def build_relationship(graph, model, event1, event2):

    graph.add_event(event1)
    graph.add_event(event2)
    
    features = extract_features(event1, event2)
    probability = predict_relationship(model, features)
    graph.add_relationship(event1, event2, probability)
