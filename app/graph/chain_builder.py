from app.ai.features import extract_features
from app.ai.predict import predict_relationship
from app.graph.candidates import find_candidates


def build_attack_chain(events, model, graph, threshold=0.5):

    for event in events:
        graph.add_event(event)
        candidates = find_candidates(events, event)

        for candidate in candidates:
            features = extract_features(event, candidate)
            probability = predict_relationship(model, features)
            if probability >= threshold:
                graph.add_relationship(event, candidate, probability)
